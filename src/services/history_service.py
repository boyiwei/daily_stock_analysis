# -*- coding: utf-8 -*-
"""
===================================
历史查询服务层
===================================

职责：
1. 封装历史记录查询逻辑
2. 提供分页和筛选功能
"""

import json
import logging
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List

from src.storage import DatabaseManager

logger = logging.getLogger(__name__)


class HistoryService:
    """
    历史查询服务
    
    封装历史分析记录的查询逻辑
    """
    
    def __init__(self, db_manager: Optional[DatabaseManager] = None):
        """
        初始化历史查询服务
        
        Args:
            db_manager: 数据库管理器（可选，默认使用单例）
        """
        self.db = db_manager or DatabaseManager.get_instance()
    
    def get_history_list(
        self,
        stock_code: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        page: int = 1,
        limit: int = 20
    ) -> Dict[str, Any]:
        """
        获取历史分析列表
        
        Args:
            stock_code: 股票代码筛选
            start_date: 开始日期 (YYYY-MM-DD)
            end_date: 结束日期 (YYYY-MM-DD)
            page: 页码
            limit: 每页数量
            
        Returns:
            包含 total, items 的字典
        """
        try:
            # 解析日期参数
            start_dt = None
            end_dt = None
            
            if start_date:
                try:
                    start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
                except ValueError:
                    logger.warning(f"无效的 start_date 格式: {start_date}")
            
            if end_date:
                try:
                    end_dt = datetime.strptime(end_date, "%Y-%m-%d").date()
                except ValueError:
                    logger.warning(f"无效的 end_date 格式: {end_date}")
            
            # 计算 offset
            offset = (page - 1) * limit
            
            # 使用新的分页查询方法
            records, total = self.db.get_analysis_history_paginated(
                code=stock_code,
                start_date=start_dt,
                end_date=end_dt,
                offset=offset,
                limit=limit
            )
            
            # 转换为响应格式
            items = []
            for record in records:
                items.append({
                    "query_id": record.query_id,
                    "stock_code": record.code,
                    "stock_name": record.name,
                    "report_type": record.report_type,
                    "sentiment_score": record.sentiment_score,
                    "operation_advice": record.operation_advice,
                    "created_at": record.created_at.isoformat() if record.created_at else None,
                })
            
            return {
                "total": total,
                "items": items,
            }
            
        except Exception as e:
            logger.error(f"查询历史列表失败: {e}", exc_info=True)
            return {"total": 0, "items": []}
    
    def get_history_detail(self, query_id: str) -> Optional[Dict[str, Any]]:
        """
        获取历史报告详情
        
        Args:
            query_id: 分析记录唯一标识
            
        Returns:
            完整的分析报告字典，不存在返回 None
        """
        try:
            # 查询数据库
            records = self.db.get_analysis_history(query_id=query_id, limit=1)
            
            if not records:
                return None
            
            record = records[0]
            
            # 解析 raw_result JSON
            raw_result = None
            if record.raw_result:
                try:
                    raw_result = json.loads(record.raw_result)
                except json.JSONDecodeError:
                    raw_result = record.raw_result
            
            # 解析 context_snapshot JSON
            context_snapshot = None
            if record.context_snapshot:
                try:
                    context_snapshot = json.loads(record.context_snapshot)
                except json.JSONDecodeError:
                    context_snapshot = record.context_snapshot
            
            # 计算情绪标签
            sentiment_label = self._get_sentiment_label(record.sentiment_score or 50)
            
            return {
                "query_id": record.query_id,
                "stock_code": record.code,
                "stock_name": record.name,
                "report_type": record.report_type,
                "created_at": record.created_at.isoformat() if record.created_at else None,
                "analysis_summary": record.analysis_summary,
                "operation_advice": record.operation_advice,
                "trend_prediction": record.trend_prediction,
                "sentiment_score": record.sentiment_score,
                "sentiment_label": sentiment_label,
                "ideal_buy": str(record.ideal_buy) if record.ideal_buy else None,
                "secondary_buy": str(record.secondary_buy) if record.secondary_buy else None,
                "stop_loss": str(record.stop_loss) if record.stop_loss else None,
                "take_profit": str(record.take_profit) if record.take_profit else None,
                "news_content": record.news_content,
                "raw_result": raw_result,
                "context_snapshot": context_snapshot,
            }
            
        except Exception as e:
            logger.error(f"查询历史详情失败: {e}", exc_info=True)
            return None

    def get_news_intel(self, query_id: str, limit: int = 20) -> List[Dict[str, str]]:
        """
        获取指定 query_id 关联的新闻情报

        Args:
            query_id: 分析记录唯一标识
            limit: 返回数量限制

        Returns:
            新闻情报列表（包含 title、snippet、url）
        """
        try:
            records = self.db.get_news_intel_by_query_id(query_id=query_id, limit=limit)

            if not records:
                records = self._fallback_news_by_analysis_context(query_id=query_id, limit=limit)

            items: List[Dict[str, str]] = []
            for record in records:
                snippet = (record.snippet or "").strip()
                if len(snippet) > 200:
                    snippet = f"{snippet[:197]}..."
                items.append({
                    "title": record.title,
                    "snippet": snippet,
                    "url": record.url,
                })

            return items

        except Exception as e:
            logger.error(f"查询新闻情报失败: {e}", exc_info=True)
            return []

    def _fallback_news_by_analysis_context(self, query_id: str, limit: int) -> List[Any]:
        """
        Fallback by analysis context when direct query_id lookup returns no news.

        Typical scenarios:
        - URL-level dedup keeps one canonical news row across repeated analyses.
        - Legacy records may have different historical query_id strategies.
        """
        records = self.db.get_analysis_history(query_id=query_id, limit=1)
        if not records:
            return []

        analysis = records[0]
        if not analysis.code or not analysis.created_at:
            return []

        # Narrow down to same-stock recent news, then filter by analysis time window.
        days = max(1, (datetime.now() - analysis.created_at).days + 1)
        candidates = self.db.get_recent_news(code=analysis.code, days=days, limit=max(limit * 5, 50))

        start_time = analysis.created_at - timedelta(hours=6)
        end_time = analysis.created_at + timedelta(hours=6)
        matched = [
            item for item in candidates
            if item.fetched_at and start_time <= item.fetched_at <= end_time
        ]

        return matched[:limit]
    
    def _get_sentiment_label(self, score: int) -> str:
        """
        根据评分获取情绪标签
        
        Args:
            score: 情绪评分 (0-100)
            
        Returns:
            情绪标签
        """
        if score >= 80:
            return "极度乐观"
        elif score >= 60:
            return "乐观"
        elif score >= 40:
            return "中性"
        elif score >= 20:
            return "悲观"
        else:
            return "极度悲观"
