# -*- coding: utf-8 -*-
"""Configuration field metadata registry.

This module is the single source of truth for configuration UI metadata,
validation hints, and category grouping.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List, Optional

SCHEMA_VERSION = "2026-02-09"

_CATEGORY_DEFINITIONS: List[Dict[str, Any]] = [
    {
        "category": "base",
        "title": "Base Settings",
        "description": "Watchlist and foundational application settings.",
        "display_order": 10,
    },
    {
        "category": "ai_model",
        "title": "AI Model",
        "description": "Model providers, model names, and inference parameters.",
        "display_order": 20,
    },
    {
        "category": "data_source",
        "title": "Data Source",
        "description": "Market data provider credentials and priority settings.",
        "display_order": 30,
    },
    {
        "category": "notification",
        "title": "Notification",
        "description": "Bot, webhook, and push channel related settings.",
        "display_order": 40,
    },
    {
        "category": "system",
        "title": "System",
        "description": "Runtime and scheduling controls.",
        "display_order": 50,
    },
    {
        "category": "backtest",
        "title": "Backtest",
        "description": "Backtest engine behavior and evaluation parameters.",
        "display_order": 60,
    },
    {
        "category": "uncategorized",
        "title": "Uncategorized",
        "description": "Keys not mapped in the field registry.",
        "display_order": 99,
    },
]

_FIELD_DEFINITIONS: Dict[str, Dict[str, Any]] = {
    "STOCK_LIST": {
        "title": "Stock List",
        "description": "Comma-separated watchlist stock codes.",
        "category": "base",
        "data_type": "array",
        "ui_control": "textarea",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "600519,300750,002594",
        "options": [],
        "validation": {"min_items": 1},
        "display_order": 10,
    },
    "TUSHARE_TOKEN": {
        "title": "Tushare Token",
        "description": "Token for Tushare Pro API.",
        "category": "data_source",
        "data_type": "string",
        "ui_control": "password",
        "is_sensitive": True,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {},
        "display_order": 10,
    },
    "REALTIME_SOURCE_PRIORITY": {
        "title": "Realtime Source Priority",
        "description": "Comma-separated priority for realtime quote providers.",
        "category": "data_source",
        "data_type": "string",
        "ui_control": "text",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "tencent,akshare_sina,efinance,akshare_em",
        "options": [],
        "validation": {},
        "display_order": 20,
    },
    "TAVILY_API_KEYS": {
        "title": "Tavily API Keys",
        "description": "Comma-separated Tavily API keys.",
        "category": "data_source",
        "data_type": "string",
        "ui_control": "password",
        "is_sensitive": True,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {"multi_value": True, "delimiter": ","},
        "display_order": 30,
    },
    "SERPAPI_API_KEYS": {
        "title": "SerpAPI Keys",
        "description": "Comma-separated SerpAPI keys.",
        "category": "data_source",
        "data_type": "string",
        "ui_control": "password",
        "is_sensitive": True,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {"multi_value": True, "delimiter": ","},
        "display_order": 40,
    },
    "BRAVE_API_KEYS": {
        "title": "Brave API Keys",
        "description": "Comma-separated Brave Search API keys.",
        "category": "data_source",
        "data_type": "string",
        "ui_control": "password",
        "is_sensitive": True,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {"multi_value": True, "delimiter": ","},
        "display_order": 50,
    },
    "GEMINI_API_KEY": {
        "title": "Gemini API Key",
        "description": "API key for Gemini service.",
        "category": "ai_model",
        "data_type": "string",
        "ui_control": "password",
        "is_sensitive": True,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {},
        "display_order": 10,
    },
    "GEMINI_MODEL": {
        "title": "Gemini Model",
        "description": "Gemini model name.",
        "category": "ai_model",
        "data_type": "string",
        "ui_control": "text",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "gemini-3-flash-preview",
        "options": [],
        "validation": {},
        "display_order": 20,
    },
    "GEMINI_TEMPERATURE": {
        "title": "Gemini Temperature",
        "description": "Temperature in range [0.0, 2.0].",
        "category": "ai_model",
        "data_type": "number",
        "ui_control": "number",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "0.7",
        "options": [],
        "validation": {"min": 0.0, "max": 2.0},
        "display_order": 30,
    },
    "OPENAI_API_KEY": {
        "title": "OpenAI API Key",
        "description": "API key for OpenAI-compatible service.",
        "category": "ai_model",
        "data_type": "string",
        "ui_control": "password",
        "is_sensitive": True,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {},
        "display_order": 40,
    },
    "OPENAI_BASE_URL": {
        "title": "OpenAI Base URL",
        "description": "Base URL for OpenAI-compatible endpoint.",
        "category": "ai_model",
        "data_type": "string",
        "ui_control": "text",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {},
        "display_order": 50,
    },
    "OPENAI_MODEL": {
        "title": "OpenAI Model",
        "description": "Model name for OpenAI-compatible endpoint.",
        "category": "ai_model",
        "data_type": "string",
        "ui_control": "text",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "gpt-4o-mini",
        "options": [],
        "validation": {},
        "display_order": 60,
    },
    "AI_SANDBOX_KEY": {
        "title": "AI Sandbox Key",
        "description": "API key for AI Sandbox (Portkey gateway).",
        "category": "ai_model",
        "data_type": "string",
        "ui_control": "password",
        "is_sensitive": True,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {},
        "display_order": 70,
    },
    "AI_SANDBOX_MODEL": {
        "title": "AI Sandbox Model",
        "description": "Model name for AI Sandbox.",
        "category": "ai_model",
        "data_type": "string",
        "ui_control": "text",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "gemini-3-flash-preview",
        "options": [],
        "validation": {},
        "display_order": 80,
    },
    "AI_SANDBOX_TEMPERATURE": {
        "title": "AI Sandbox Temperature",
        "description": "Temperature in range [0.0, 2.0] for AI Sandbox.",
        "category": "ai_model",
        "data_type": "number",
        "ui_control": "number",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "0.7",
        "options": [],
        "validation": {"min": 0.0, "max": 2.0},
        "display_order": 90,
    },
    "WECHAT_WEBHOOK_URL": {
        "title": "WeChat Webhook URL",
        "description": "Webhook URL for enterprise WeChat bot.",
        "category": "notification",
        "data_type": "string",
        "ui_control": "password",
        "is_sensitive": True,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {},
        "display_order": 10,
    },
    "DINGTALK_APP_KEY": {
        "title": "DingTalk App Key",
        "description": "DingTalk app key.",
        "category": "notification",
        "data_type": "string",
        "ui_control": "password",
        "is_sensitive": True,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {},
        "display_order": 20,
    },
    "DINGTALK_APP_SECRET": {
        "title": "DingTalk App Secret",
        "description": "DingTalk app secret.",
        "category": "notification",
        "data_type": "string",
        "ui_control": "password",
        "is_sensitive": True,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {},
        "display_order": 30,
    },
    "PUSHPLUS_TOKEN": {
        "title": "PushPlus Token",
        "description": "Token for PushPlus notifications.",
        "category": "notification",
        "data_type": "string",
        "ui_control": "password",
        "is_sensitive": True,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {},
        "display_order": 40,
    },
    "CUSTOM_WEBHOOK_URLS": {
        "title": "Custom Webhook URLs",
        "description": "Comma-separated webhook URLs for custom notifications (DingTalk, Discord, Slack, etc.).",
        "category": "notification",
        "data_type": "array",
        "ui_control": "textarea",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {"multi_value": True, "delimiter": ","},
        "display_order": 50,
    },
    "CUSTOM_WEBHOOK_BEARER_TOKEN": {
        "title": "Custom Webhook Bearer Token",
        "description": "Bearer token for authenticated custom webhooks.",
        "category": "notification",
        "data_type": "string",
        "ui_control": "password",
        "is_sensitive": True,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {},
        "display_order": 51,
    },
    "SCHEDULE_TIME": {
        "title": "Schedule Time",
        "description": "Daily schedule time in HH:MM format.",
        "category": "system",
        "data_type": "time",
        "ui_control": "time",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "18:00",
        "options": [],
        "validation": {"pattern": r"^([01]\d|2[0-3]):[0-5]\d$"},
        "display_order": 10,
    },
    "HTTP_PROXY": {
        "title": "HTTP Proxy",
        "description": "Optional HTTP proxy endpoint.",
        "category": "system",
        "data_type": "string",
        "ui_control": "text",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {},
        "display_order": 20,
    },
    "LOG_LEVEL": {
        "title": "Log Level",
        "description": "Application log level.",
        "category": "system",
        "data_type": "string",
        "ui_control": "select",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "INFO",
        "options": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        "validation": {"enum": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]},
        "display_order": 30,
    },
    "WEBUI_PORT": {
        "title": "Web UI Port",
        "description": "Port for Web UI service.",
        "category": "system",
        "data_type": "integer",
        "ui_control": "number",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "8000",
        "options": [],
        "validation": {"min": 1, "max": 65535},
        "display_order": 40,
    },
    "BACKTEST_ENABLED": {
        "title": "Backtest Enabled",
        "description": "Whether backtest is enabled.",
        "category": "backtest",
        "data_type": "boolean",
        "ui_control": "switch",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "true",
        "options": [],
        "validation": {},
        "display_order": 10,
    },
    "BACKTEST_EVAL_WINDOW_DAYS": {
        "title": "Backtest Eval Window Days",
        "description": "Backtest evaluation window in trading days.",
        "category": "backtest",
        "data_type": "integer",
        "ui_control": "number",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "10",
        "options": [],
        "validation": {"min": 1, "max": 365},
        "display_order": 20,
    },
    "BACKTEST_MIN_AGE_DAYS": {
        "title": "Backtest Min Age Days",
        "description": "Only evaluate analysis records older than this threshold.",
        "category": "backtest",
        "data_type": "integer",
        "ui_control": "number",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "14",
        "options": [],
        "validation": {"min": 0, "max": 3650},
        "display_order": 30,
    },
    "BACKTEST_ENGINE_VERSION": {
        "title": "Backtest Engine Version",
        "description": "Backtest engine version label.",
        "category": "backtest",
        "data_type": "string",
        "ui_control": "text",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "v1",
        "options": [],
        "validation": {},
        "display_order": 40,
    },
    "BACKTEST_NEUTRAL_BAND_PCT": {
        "title": "Backtest Neutral Band Pct",
        "description": "Neutral return band percentage for outcome labeling.",
        "category": "backtest",
        "data_type": "number",
        "ui_control": "number",
        "is_sensitive": False,
        "is_required": False,
        "is_editable": True,
        "default_value": "2.0",
        "options": [],
        "validation": {"min": 0.0, "max": 100.0},
        "display_order": 50,
    },
}


def get_category_definitions() -> List[Dict[str, Any]]:
    """Return deep-copied category metadata."""
    return deepcopy(_CATEGORY_DEFINITIONS)


def get_registered_field_keys() -> List[str]:
    """Return all explicitly registered keys."""
    return list(_FIELD_DEFINITIONS.keys())


def get_field_definition(key: str, value_hint: Optional[str] = None) -> Dict[str, Any]:
    """Return field definition for key, including inferred fallback metadata."""
    key_upper = key.upper()
    if key_upper in _FIELD_DEFINITIONS:
        field = deepcopy(_FIELD_DEFINITIONS[key_upper])
        field["key"] = key_upper
        return field

    category = _infer_category(key_upper)
    data_type = _infer_data_type(key_upper, value_hint)
    field = {
        "key": key_upper,
        "title": key_upper.replace("_", " ").title(),
        "description": "Auto-inferred field metadata.",
        "category": category,
        "data_type": data_type,
        "ui_control": _infer_ui_control(data_type, key_upper),
        "is_sensitive": _is_sensitive_key(key_upper),
        "is_required": False,
        "is_editable": True,
        "default_value": None,
        "options": [],
        "validation": {},
        "display_order": 9000,
    }
    return field


def build_schema_response() -> Dict[str, Any]:
    """Build schema payload grouped by category."""
    category_map: Dict[str, Dict[str, Any]] = {}
    for category in get_category_definitions():
        category_map[category["category"]] = {**category, "fields": []}

    for key in sorted(_FIELD_DEFINITIONS.keys()):
        field = get_field_definition(key)
        category_map[field["category"]]["fields"].append(field)

    categories = sorted(category_map.values(), key=lambda item: item["display_order"])
    for category in categories:
        category["fields"] = sorted(
            category["fields"],
            key=lambda item: (item.get("display_order", 9999), item["key"]),
        )

    return {
        "schema_version": SCHEMA_VERSION,
        "categories": categories,
    }


def _is_sensitive_key(key: str) -> bool:
    markers = ("KEY", "TOKEN", "SECRET", "PASSWORD")
    return any(marker in key for marker in markers)


def _infer_category(key: str) -> str:
    if key == "STOCK_LIST":
        return "base"
    if key.startswith("BACKTEST_"):
        return "backtest"
    if key.startswith(("GEMINI_", "OPENAI_", "AI_SANDBOX_")):
        return "ai_model"
    if key.endswith("_PRIORITY") or key.startswith(
        (
            "TUSHARE",
            "AKSHARE",
            "EFINANCE",
            "PYTDX",
            "BAOSTOCK",
            "YFINANCE",
            "TAVILY",
            "SERPAPI",
            "BRAVE",
        )
    ):
        return "data_source"
    if key.startswith((
        "WECHAT",
        "FEISHU",
        "TELEGRAM",
        "EMAIL",
        "PUSHOVER",
        "PUSHPLUS",
        "SERVERCHAN",
        "DINGTALK",
        "DISCORD",
        "CUSTOM_WEBHOOK",
        "WECOM",
        "ASTRBOT",
    )) or "WEBHOOK" in key:
        return "notification"
    if key.startswith(("LOG_", "SCHEDULE_", "WEBUI_", "HTTP_", "HTTPS_", "MAX_", "DEBUG")):
        return "system"
    return "uncategorized"


def _infer_data_type(key: str, value_hint: Optional[str]) -> str:
    if key.endswith("_TIME"):
        return "time"
    if value_hint is None:
        return "string"

    lowered = value_hint.strip().lower()
    if lowered in {"true", "false"}:
        return "boolean"

    try:
        int(value_hint)
        return "integer"
    except (TypeError, ValueError):
        pass

    try:
        float(value_hint)
        return "number"
    except (TypeError, ValueError):
        pass

    if key in {"STOCK_LIST", "EMAIL_RECEIVERS", "CUSTOM_WEBHOOK_URLS"}:
        return "array"
    return "string"


def _infer_ui_control(data_type: str, key: str) -> str:
    if _is_sensitive_key(key):
        return "password"
    if data_type == "boolean":
        return "switch"
    if data_type in {"integer", "number"}:
        return "number"
    if data_type == "time":
        return "time"
    if data_type == "array":
        return "textarea"
    return "text"
