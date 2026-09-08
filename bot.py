import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#rotation="00:00",
#diagnose=False,
#level="ERROR",
#format=default_format)

# You can pass some keyword args config to init function
nonebot.init(driver="~fastapi+~websockets+~httpx")
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

#if __name__ == "__mp_main__":
nonebot.load_builtin_plugins("echo")
#nonebot.load_plugin('nonebot_plugin_gocqhttp')
nonebot.load_plugin('nonebot_plugin_apscheduler')#定时任务
nonebot.load_plugin('nonebot_plugin_htmlrender')#浏览器渲染图片
nonebot.load_plugin('nonebot_plugin_heweather')#天气查询
#nonebot.load_plugin('nonebot_plugin_chess')#国际象棋
nonebot.load_plugin('nonebot_plugin_handle')#猜成语
nonebot.load_plugin('nonebot_plugin_minesweeper')#扫雷
nonebot.load_plugin('nonebot_plugin_giyf')#快速搜索
#nonebot.load_plugin('nonebot_plugin_sentry')#日志监控
#nonebot.load_plugin('nonebot_plugin_covid19_news')#新冠查询
nonebot.load_plugin('nonebot_plugin_wordle')#猜单词
#nonebot.load_plugin('nonebot_plugin_caiyunai')#彩云小梦
nonebot.load_plugin('nonebot_plugin_analysis_bilibili')#b站视频自动解析
#nonebot.load_plugin('haruka_bot')#b站机器人
nonebot.load_plugins("src/plugins")#自定义插件文件夹路径
nonebot.load_plugin('nonebot_plugin_memes')#表情包制作
nonebot.load_plugin('nonebot_plugin_wordcloud')#词云
nonebot.load_plugin('nonebot_plugin_simplemusic')#点歌
#nonebot.load_plugin('nonebot_plugin_petpet')#头像表情包（已被合并）
nonebot.load_plugin('nonebot_plugin_crazy_thursday')#疯狂星期四
#nonebot.load_plugin("nonebot_plugin_todo_nlp")#自识别todo
nonebot.load_plugin("nonebot_plugin_ddcheck")#查VTuber成分
#nonebot.load_plugin("nonebot_plugin_cchess")#象棋
nonebot.load_plugin("nonebot_plugin_mediawiki")#wiki查询
#nonebot.load_plugin("nonebot_plugin_boardgame")#五子棋、黑白棋、围棋
nonebot.load_plugin("nonebot_plugin_remake")#重开模拟器
#nonebot.load_plugin('nonebot_plugin_bawiki')#蔚蓝档案wiki
nonebot.load_plugin("nonebot_plugin_charpic")#合成字符画
nonebot.load_plugin("nonebot_plugin_60s")#60s日历
nonebot.load_plugin("nonebot_plugin_morning")#作息记录
nonebot.load_plugin('nonebot_plugin_picstatus')#运行状态显示
#nonebot.load_plugin('nonebot_plugin_mockingbird')#MockingBird语音生成
#nonebot.load_plugin('nonebot_plugin_pixiv')#p站搜图
#nonebot.load_plugin('nonebot_plugin_aidraw')#novelai绘画
#nonebot.load_plugin('nonebot_plugin_RealESRGAN')#图像超分辨率重建
#nonebot.load_plugin('nonebot_plugin_drawer')#AI绘画
#nonebot.load_plugin('nonebot_plugin_savor')#二刺螈图像分析（提取图片标签）
nonebot.load_plugin('nonebot_plugin_withdraw')#自动撤回
#nonebot.load_plugin("nonebot_plugin_youthstudy")#青年大学习
nonebot.load_plugin("nonebot_plugin_repeater")#复读+1
#nonebot.load_plugin("nonebot_plugin_pmhelp")#插件管理器,（pydantic版本过低）
#nonebot.load_plugin("nonebot_plugin_animeres")#二刺螈资源获取
nonebot.load_plugin("nonebot_plugin_alias")#指令别名
nonebot.load_plugin("nonebot_plugin_oddtext")#抽象文本生成
#nonebot.load_plugin("ayaka_prevent_bad_words")#坏词撤回
#nonebot.load_plugin("nonebot_plugin_flexperm")#权限管理
#nonebot.load_plugin("nonebot_plugin_who_at_me")#谁艾特我
nonebot.load_plugin('nonebot_plugin_antiinsult')#反嘴臭
#nonebot.load_plugin('nonebot_plugin_hikarisearch')#搜图
#nonebot.load_plugin('nonebot_plugin_chatgpt_turbo')#chatgpt
#nonebot.load_plugin('nonebot_plugin_bing_chat')#bing chat
#nonebot.load_plugin('nonebot_plugin_zyk_music')#下载文件式点歌
#nonebot.load_plugin('criminal_dance')#文字版桌游，犯人在跳舞
#nonebot.load_plugin('nonebot-plugin-wolf-kill')#狼人杀
#nonebot.load_plugin('nonebot_plugin_report_manager')#对话超管
#nonebot.load_plugin('nonebot_plugin_error_alert')#似乎是报错
#nonebot.load_plugin('nonebot_plugin_manga_translator')#图片翻译
nonebot.load_plugin('nonebot_plugin_emojimix')#emoji合成
nonebot.load_plugin('nonebot_plugin_essence_message')#精华消息整理
#nonebot.load_plugin('nonebot_plugin_deepseek')#DeepSeek对话
#nonebot.load_plugin('nonebot_plugin_summary')#聊天记录总结（pydantic版本需V2，与其他插件有冲突//已升级）
nonebot.load_plugin('nonebot_plugin_remind')#定时提醒
nonebot.load_plugin('nonebot_plugin_water_geoup_stats')#发言统计
#nonebot.load_plugin('nonebot_plugin_aitalk')#AI聊天
#nonebot.load_plugin('nonebot_plugin_llmchat')#AI聊天（会自己发消息）
nonebot.load_plugin('nonebot_plugin_jmdownloader')#jm下载
nonebot.load_plugin('nonebot_plugin_fix_qq_img_ssl')#修复访问 QQ 图床的 SSL 错误
nonebot.load_plugin('nonebot_plugin_picmenu_next')#图片插件帮助
nonebot.load_plugin('nonebot_plugin_moellmchats')#混合专家模型调度LLM插件

# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    #nonebot.load_plugin("nonebot_plugin_reboot")
    nonebot.run(app="__mp_main__:app")
