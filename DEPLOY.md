# 部署指南

本文档以 Ubuntu / Debian 为例，其他发行版把 `apt` 换成对应包管理器即可。

## 1. 安装系统依赖

```bash
sudo apt update
sudo apt install -y python3.12 python3.12-venv git fluidsynth ffmpeg
```

- `fluidsynth`：`nonebot_plugin_makemidi` 生成音频需要
- `ffmpeg`：`pydub` 音频转码需要

## 2. 获取代码

```bash
git clone <你的仓库地址> /home/goat
cd /home/goat
```

## 3. 创建虚拟环境并安装依赖

```bash
python3.12 -m venv .venv
source .venv/bin/activate

pip install -U pip
pip install -r requirements.txt

playwright install chromium
# 若提示缺少系统库，再执行：
# playwright install-deps chromium
```

## 4. 配置 .env

```bash
cp .env.example .env
vim .env
```

至少需要填写：

- `SUPERUSERS=["你的QQ号"]`
- `ONEBOT_ACCESS_TOKEN=<与 OneBot 实现端一致>`
- `HOST` / `PORT`（建议 `127.0.0.1` + 一个高位端口，不要直接暴露公网）
- 其余按 `.env.example` 中的注释按需填写；不用的插件项留空即可

> `.env` 含真实密钥，**不要提交到 git**（已在 `.gitignore` 中排除）。
>
> 多行 JSON 配置（`aitalk_*`、`LLMCHAT__API_PRESETS`、`LLMCHAT__MCP_SERVERS`）请参考对应插件文档填写。

## 5. 配置 OneBot 实现端

以 NapCat 为例，在其 WebUI 里配置：

- 反向 WebSocket 连接到 `ws://127.0.0.1:<PORT>/onebot/v11/ws`
- 或正向连接，与 `.env` 中的 `HOST` / `PORT` 保持一致
- Access Token 与 `.env` 的 `ONEBOT_ACCESS_TOKEN` 相同

## 6. 启动

```bash
cd /home/goat
source .venv/bin/activate
python bot.py
```

## 7. 用 systemd 常驻（推荐）

新建 `/etc/systemd/system/goat.service`：

```ini
[Unit]
Description=goat NoneBot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/goat
ExecStart=/home/goat/.venv/bin/python bot.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now goat
sudo systemctl status goat
sudo journalctl -u goat -f
```

## 8. 更新

```bash
cd /home/goat
git pull
source .venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart goat
```

## 9. 常见问题

- `playwright` 报找不到浏览器：执行 `playwright install chromium`
- `makemidi` 报错：确认系统已安装 `fluidsynth`
- `ModuleNotFoundError: nonebot` 或版本冲突：卸载 NoneBot v1 —— `pip uninstall nonebot`（保留 `nonebot2`）
- 机器人收不到消息：检查 `HOST` / `PORT`、防火墙、以及 OneBot 实现端的连接方向与 Access Token
- `.env` 不生效：确认在项目根目录、变量名大小写正确、没有多余空格
