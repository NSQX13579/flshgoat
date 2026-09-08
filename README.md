# goat（梵高）

一个基于 [NoneBot2](https://nonebot.dev/) + OneBot V11 的 QQ 群聊机器人。

## 功能

- 群聊互动：猜成语、扫雷、猜单词、疯狂星期四、复读、抽象文本、反嘴臭、emoji 合成、表情包制作等
- 查询工具：天气、60s 读世界、VTuber 成分、MediaWiki、B 站视频解析、词云、运行状态
- 媒体：点歌、字符画、JM 下载
- AI：多模型调度（`nonebot-plugin-moellmchats`）
- 本地插件（`src/plugins/`）：
  - `reply`：群内自定义问答
  - `saying`：“名人名言”图片收集与复读
  - `nonebot_plugin_ygo`：游戏王卡查
  - `nonebot_plugin_makemidi`：文字转 MIDI
  - `nonebot-plugin-bangumi-search`：番剧搜索

完整启用列表见 `bot.py`。

## 环境要求

- Python 3.12
- 任意 OneBot V11 实现（如 [NapCat](https://github.com/NapNeko/NapCatQQ)、go-cqhttp、Lagrange.Core）
- 系统依赖：
  - `fluidsynth`：`nonebot_plugin_makemidi` 需要
  - `ffmpeg`：`pydub` 音频转码需要

## 快速开始

```bash
git clone <你的仓库地址> goat
cd goat

python3.12 -m venv .venv
source .venv/bin/activate

pip install -U pip
pip install -r requirements.txt
playwright install chromium        # bangumi-search / htmlrender 需要

cp .env.example .env               # 然后按注释填写
python bot.py
```

> 完整部署步骤见 [DEPLOY.md](./DEPLOY.md)。

## 配置说明

- `.env`：核心与各插件配置，以 `.env.example` 为模板。**含密钥，已在 `.gitignore` 中排除，切勿提交。**
- `config/`：部分插件的持久化配置，随仓库分发。
- `data/`：运行数据（图片、数据库、RSS 缓存等），**不提交**，由机器人在运行时生成。
- `requirements.txt`：精简依赖清单；`requirements.lock.txt`：服务器环境的完整快照。

## 目录结构

```
.
├── bot.py                 # 入口，注册适配器并加载插件
├── pyproject.toml         # 项目与 NoneBot 配置
├── requirements.txt       # 依赖（锁定版本）
├── requirements.lock.txt  # 服务器完整依赖快照
├── .env.example           # 配置模板
├── src/plugins/           # 本地插件
├── config/                # 插件持久化配置
├── pm_config/             # 插件管理元数据
└── data/                  # 运行数据（不提交）
```

## 说明

- 实测环境：Python 3.12.11 / nonebot2 2.4.4 / nonebot-adapter-onebot 2.4.6。
- 若系统里同时装了 `nonebot`（NoneBot v1），会与 `nonebot2` 抢占 `nonebot` 包名，请卸载：`pip uninstall nonebot`。
