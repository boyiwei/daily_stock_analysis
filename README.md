<div align="center">

# 📈 股票智能分析系统

[![GitHub stars](https://img.shields.io/github/stars/ZhuLinsen/daily_stock_analysis?style=social)](https://github.com/ZhuLinsen/daily_stock_analysis/stargazers)
[![CI](https://github.com/ZhuLinsen/daily_stock_analysis/actions/workflows/ci.yml/badge.svg)](https://github.com/ZhuLinsen/daily_stock_analysis/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Ready-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://hub.docker.com/)

> 🤖 基于 AI 大模型的 A股/港股/美股自选股智能分析系统，每日自动分析并推送「决策仪表盘」到企业微信/飞书/Telegram/邮箱

[**功能特性**](#-功能特性) · [**快速开始**](#-快速开始) · [**推送效果**](#-推送效果) · [**完整指南**](docs/full-guide.md) · [**常见问题**](docs/FAQ.md) · [**更新日志**](docs/CHANGELOG.md)

简体中文 | [English](docs/README_EN.md) | [繁體中文](docs/README_CHT.md)

</div>

## 💖 赞助商 (Sponsors)
<div align="center">
  <a href="https://serpapi.com/baidu-search-api?utm_source=github_daily_stock_analysis" target="_blank">
    <img src="./sources/serpapi_banner_zh.png" alt="轻松抓取搜索引擎上的实时金融新闻数据 - SerpApi" height="160">
  </a>
</div>
<br>


## ✨ 功能特性

| 模块 | 功能 | 说明 |
|------|------|------|
| AI | 决策仪表盘 | 一句话核心结论 + 精确买卖点位 + 操作检查清单 |
| 分析 | 多维度分析 | 技术面 + 筹码分布 + 舆情情报 + 实时行情 |
| 市场 | 全球市场 | 支持 A股、港股、美股 |
| 复盘 | 大盘复盘 | 每日市场概览、板块涨跌、北向资金 |
| 回测 | AI 回测验证 | 自动评估历史分析准确率，方向胜率、止盈止损命中率 |
| 推送 | 多渠道通知 | 企业微信、飞书、Telegram、钉钉、邮件、Pushover |
| 自动化 | 定时运行 | GitHub Actions 定时执行，无需服务器 |

### 技术栈与数据来源

| 类型 | 支持 |
|------|------|
| AI 模型 | Gemini（免费）、OpenAI 兼容、DeepSeek、通义千问、Claude、Ollama |
| 行情数据 | AkShare、Tushare、Pytdx、Baostock、YFinance |
| 新闻搜索 | Tavily、SerpAPI、Bocha、Brave |

### 内置交易纪律

| 规则 | 说明 |
|------|------|
| 严禁追高 | 乖离率 > 5% 自动提示风险 |
| 趋势交易 | MA5 > MA10 > MA20 多头排列 |
| 精确点位 | 买入价、止损价、目标价 |
| 检查清单 | 每项条件以「满足 / 注意 / 不满足」标记 |

## 🚀 快速开始

### 方式一：GitHub Actions（推荐）

> 5 分钟完成部署，零成本，无需服务器。


#### 1. Fork 本仓库

点击右上角 `Fork` 按钮（顺便点个 Star⭐ 支持一下）

#### 2. 配置 Secrets

`Settings` → `Secrets and variables` → `Actions` → `New repository secret`

**AI 模型配置（二选一）**

| Secret 名称 | 说明 | 必填 |
|------------|------|:----:|
| `GEMINI_API_KEY` | [Google AI Studio](https://aistudio.google.com/) 获取免费 Key | ✅* |
| `OPENAI_API_KEY` | OpenAI 兼容 API Key（支持 DeepSeek、通义千问等） | 可选 |
| `OPENAI_BASE_URL` | OpenAI 兼容 API 地址（如 `https://api.deepseek.com/v1`） | 可选 |
| `OPENAI_MODEL` | 模型名称（如 `deepseek-chat`） | 可选 |

> 注：`GEMINI_API_KEY` 和 `OPENAI_API_KEY` 至少配置一个

<details>
<summary><b>通知渠道配置</b>（点击展开，至少配置一个）</summary>


| Secret 名称 | 说明 | 必填 |
|------------|------|:----:|
| `WECHAT_WEBHOOK_URL` | 企业微信 Webhook URL | 可选 |
| `FEISHU_WEBHOOK_URL` | 飞书 Webhook URL | 可选 |
| `TELEGRAM_BOT_TOKEN` | Telegram Bot Token（@BotFather 获取） | 可选 |
| `TELEGRAM_CHAT_ID` | Telegram Chat ID | 可选 |
| `TELEGRAM_MESSAGE_THREAD_ID` | Telegram Topic ID (用于发送到子话题) | 可选 |
| `EMAIL_SENDER` | 发件人邮箱（如 `xxx@qq.com`） | 可选 |
| `EMAIL_PASSWORD` | 邮箱授权码（非登录密码） | 可选 |
| `EMAIL_RECEIVERS` | 收件人邮箱（多个用逗号分隔，留空则发给自己） | 可选 |
| `EMAIL_SENDER_NAME` | 邮件发件人显示名称（默认：daily_stock_analysis股票分析助手） | 可选 |
| `STOCK_GROUP_N` / `EMAIL_GROUP_N` | 股票分组发往不同邮箱（如 `STOCK_GROUP_1=600519,300750` `EMAIL_GROUP_1=user1@example.com`） | 可选 |
| `PUSHPLUS_TOKEN` | PushPlus Token（[获取地址](https://www.pushplus.plus)，国内推送服务） | 可选 |
| `SERVERCHAN3_SENDKEY` | Server酱³ Sendkey（[获取地址](https://sc3.ft07.com/)，手机APP推送服务） | 可选 |
| `CUSTOM_WEBHOOK_URLS` | 自定义 Webhook（支持钉钉等，多个用逗号分隔） | 可选 |
| `CUSTOM_WEBHOOK_BEARER_TOKEN` | 自定义 Webhook 的 Bearer Token（用于需要认证的 Webhook） | 可选 |
| `WEBHOOK_VERIFY_SSL` | Webhook HTTPS 证书校验（默认 true）。设为 false 可支持自签名证书。警告：关闭有严重安全风险，仅限可信内网 | 可选 |
| `SINGLE_STOCK_NOTIFY` | 单股推送模式：设为 `true` 则每分析完一只股票立即推送 | 可选 |
| `REPORT_TYPE` | 报告类型：`simple`(精简) 或 `full`(完整)，Docker环境推荐设为 `full` | 可选 |
| `ANALYSIS_DELAY` | 个股分析和大盘分析之间的延迟（秒），避免API限流，如 `10` | 可选 |

> 至少配置一个渠道，配置多个则同时推送。更多配置请参考 [完整指南](docs/full-guide.md)

</details>

**其他配置**

| Secret 名称 | 说明 | 必填 |
|------------|------|:----:|
| `STOCK_LIST` | 自选股代码，如 `600519,hk00700,AAPL,TSLA` | ✅ |
| `TAVILY_API_KEYS` | [Tavily](https://tavily.com/) 搜索 API（新闻搜索） | 推荐 |
| `SERPAPI_API_KEYS` | [SerpAPI](https://serpapi.com/baidu-search-api?utm_source=github_daily_stock_analysis) 全渠道搜索 | 可选 |
| `BOCHA_API_KEYS` | [博查搜索](https://open.bocha.cn/) Web Search API（中文搜索优化，支持AI摘要，多个key用逗号分隔） | 可选 |
| `BRAVE_API_KEYS` | [Brave Search](https://brave.com/search/api/) API（隐私优先，美股优化，多个key用逗号分隔） | 可选 |
| `TUSHARE_TOKEN` | [Tushare Pro](https://tushare.pro/weborder/#/login?reg=834638 ) Token | 可选 |
| `WECHAT_MSG_TYPE` | 企微消息类型，默认 markdown，支持配置 text 类型，发送纯 markdown 文本 | 可选 |

#### 3. 启用 Actions

`Actions` 标签 → `I understand my workflows, go ahead and enable them`

#### 4. 手动测试

`Actions` → `每日股票分析` → `Run workflow` → `Run workflow`

#### 完成

默认每个**工作日 18:00（北京时间）**自动执行，也可手动触发

### 方式二：本地运行 / Docker 部署

```bash
# 克隆项目
git clone https://github.com/ZhuLinsen/daily_stock_analysis.git && cd daily_stock_analysis

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env && vim .env

# 运行分析
python main.py
```

> Docker 部署、定时任务配置请参考 [完整指南](docs/full-guide.md)

## 📱 推送效果

### 决策仪表盘
```
🎯 2026-02-08 决策仪表盘
共分析3只股票 | 🟢买入:0 🟡观望:2 🔴卖出:1

📊 分析结果摘要
⚪ 中钨高新(000657): 观望 | 评分 65 | 看多
⚪ 永鼎股份(600105): 观望 | 评分 48 | 震荡
🟡 新莱应材(300260): 卖出 | 评分 35 | 看空

⚪ 中钨高新 (000657)
📰 重要信息速览
💭 舆情情绪: 市场关注其AI属性与业绩高增长，情绪偏积极，但需消化短期获利盘和主力流出压力。
📊 业绩预期: 基于舆情信息，公司2025年前三季度业绩同比大幅增长，基本面强劲，为股价提供支撑。

🚨 风险警报:

风险点1：2月5日主力资金大幅净卖出3.63亿元，需警惕短期抛压。
风险点2：筹码集中度高达35.15%，表明筹码分散，拉升阻力可能较大。
风险点3：舆情中提及公司历史违规记录及重组相关风险提示，需保持关注。
✨ 利好催化:

利好1：公司被市场定位为AI服务器HDI核心供应商，受益于AI产业发展。
利好2：2025年前三季度扣非净利润同比暴涨407.52%，业绩表现强劲。
📢 最新动态: 【最新消息】舆情显示公司是AI PCB微钻领域龙头，深度绑定全球头部PCB/载板厂。2月5日主力资金净卖出3.63亿元，需关注后续资金流向。

---
生成时间: 18:00
```

### 大盘复盘
```
🎯 2026-01-10 大盘复盘

📊 主要指数
- 上证指数: 3250.12 (🟢+0.85%)
- 深证成指: 10521.36 (🟢+1.02%)
- 创业板指: 2156.78 (🟢+1.35%)

📈 市场概况
上涨: 3920 | 下跌: 1349 | 涨停: 155 | 跌停: 3

🔥 板块表现
领涨: 互联网服务、文化传媒、小金属
领跌: 保险、航空机场、光伏设备
```
## ⚙️ 配置说明

> 📖 完整环境变量、定时任务配置请参考 [完整配置指南](docs/full-guide.md)


## 🖥️ Web 界面

![img.png](sources/fastapi_server.png)

包含完整的配置管理、任务监控和手动分析功能。

### 启动方式

1. **编译前端** (首次运行需要)
   ```bash
   cd ./apps/dsa-web
   npm install && npm run build
   cd ../..
   ```

2. **启动服务**
   ```bash
   python main.py --webui       # 启动 Web 界面 + 执行定时分析
   python main.py --webui-only  # 仅启动 Web 界面
   ```

访问 `http://127.0.0.1:8000` 即可使用。

> 也可以使用 `python main.py --serve` (等效命令)

## 🗺️ Roadmap

查看已支持的功能和未来规划：[更新日志](docs/CHANGELOG.md)

> 有建议？欢迎 [提交 Issue](https://github.com/ZhuLinsen/daily_stock_analysis/issues)


---

## ☕ 支持项目

如果本项目对你有帮助，欢迎支持项目的持续维护与迭代，感谢支持 🙏  
赞赏可备注联系方式，祝股市长虹

| 支付宝 (Alipay) | 微信支付 (WeChat) | Ko-fi |
| :---: | :---: | :---: |
| <img src="./sources/alipay.jpg" width="200" alt="Alipay"> | <img src="./sources/wechatpay.jpg" width="200" alt="WeChat Pay"> | <a href="https://ko-fi.com/mumu157" target="_blank"><img src="./sources/ko-fi.png" width="200" alt="Ko-fi"></a> |

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

详见 [贡献指南](docs/CONTRIBUTING.md)

## 📄 License
[MIT License](LICENSE) © 2026 ZhuLinsen

如果你在项目中使用或基于本项目进行二次开发，
非常欢迎在 README 或文档中注明来源并附上本仓库链接。
这将有助于项目的持续维护和社区发展。

## 📬 联系与合作
- GitHub Issues：[提交 Issue](https://github.com/ZhuLinsen/daily_stock_analysis/issues)

## ⭐ Star History
**如果觉得有用，请给个 ⭐ Star 支持一下！**

<a href="https://star-history.com/#ZhuLinsen/daily_stock_analysis&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ZhuLinsen/daily_stock_analysis&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ZhuLinsen/daily_stock_analysis&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ZhuLinsen/daily_stock_analysis&type=Date" />
 </picture>
</a>

## ⚠️ 免责声明

本项目仅供学习和研究使用，不构成任何投资建议。股市有风险，投资需谨慎。作者不对使用本项目产生的任何损失负责。

---
