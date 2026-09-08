
"""
这是一个自定义大模型工具（Function Calling）的示例文件。
你可以参考此模板，在此目录下编写自己的原生 Python 函数。

【编写规范】
1. 零依赖：不需要导入 nonebot 或任何插件依赖，纯 Python 原生写法。
2. 异步函数：工具函数必须是 `async def` 定义的异步函数。
3. 工具描述：将函数的主要用途写在 `docstring`（三重引号注释）中，大模型会据此判断何时调用该工具。
4. 参数描述：引入 Python 原生的 `typing.Annotated`，格式为 `参数名: Annotated[类型, "参数说明"]`，以便大模型准确提取参数。
5. 返回值：最好返回字符串（str），大模型会直接读取此返回结果。
6. 多工具支持：你可以在同一个 .py 脚本中编写多个异步函数，插件会自动扫描并全部加载为独立工具，无需分拆文件。

【生效方式】
编写或修改完后，在群聊中发送管理员指令：`/刷新工具` 或 `/重载工具` 即可即时生效！
"""

import re
import datetime
import aiohttp
from typing import Annotated

# ==========================================
# 示例 1：无参数的工具
# ==========================================
async def get_current_datetime() -> str:
    """
    获取当前的系统日期、时间和星期几。
    当用户询问现在几点、今天几号、今天星期几等与当前时间相关的问题时，调用此工具获取准确时间。
    """
    try:
        now = datetime.datetime.now()
        weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        weekday_str = weekdays[now.weekday()]
        
        return f"当前系统时间是: {now.strftime(f'%Y年%m月%d日 %H:%M:%S {weekday_str}')}"
    except Exception as e:
        return f"获取时间失败: {str(e)}"

# ==========================================
# 示例 2：带参数的工具
# ==========================================
# 【依赖拓扑声明】
# 键为“触发条件”，值为“需要一并注入的工具列表”
# 表示：当大模型被分配了 web_search 工具时，强制将本脚本中的 extract_webpage 工具也提供给它。
TOOL_DEPENDENCIES = {
    "web_search": ["extract_webpage"]
}
async def extract_webpage(
    url: Annotated[str, "需要提取的完整网页链接，必须包含 http:// 或 https://"]
) -> str:
    """
    读取并提取指定URL网页的正文内容。
    当需要深入了解搜索结果中的链接，或用户要求分析某个网页时调用。
    """
    if not url.startswith(("http://", "https://")):
        return "提取失败：请提供有效的URL（以http://或https://开头）"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    timeout = aiohttp.ClientTimeout(total=30)
    
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    return f"提取失败：网页返回状态码 {response.status}"
                html = await response.text()
                
        # 使用正则移除 script 和 style 标签及其内容
        text = re.sub(r'<(script|style).*?>.*?</>', '', html, flags=re.IGNORECASE | re.DOTALL)
        # 移除所有剩余的 HTML 标签
        text = re.sub(r'<[^>]+>', ' ', text)
        
        # 清理多余的空白符和空行
        text = re.sub(r'\n\s*\n', '\n', text).strip()
        text = re.sub(r' {2,}', ' ', text)
        
        max_length = 4000
        if len(text) > max_length:
            text = text[:max_length] + "\n\n...[由于内容过长，为防止上下文超出限制，已自动截断]"
            
        return f"网页提取成功，以下是内容摘要：\n{text}"
    except Exception as e:
        return f"提取网页失败，发生错误：{str(e)}"
