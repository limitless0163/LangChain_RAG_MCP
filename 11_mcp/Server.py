import json
import httpx
from loguru import logger


class MCPWeatherServer:

    def __init__(self, name: str, host: str, port: int):
        self.name = name
        self.host = host
        self.port = port
        self._tools = {}    # 存储注册的工具函数，支撑 @mcp.tool() 装饰器

    def tool(self):
        """实现 @mcp.tool() 装饰器"""

        def decorator(func):
            self._tools[func.__name__] = func   # 注册工具函数
            return func
        
        return decorator
    
    def run(self, transport: str):
        """实现 mcp.run(transport="sse")调用格式和日志输出"""
        if transport != "sse":
            logger.warning(f"不支持的传输协议 {transport}, 默认使用 SSE")
        logger.info(f"启动 MCP SSE 天气服务器，监听 http://{self.host}:{self.port}/sse")

    def _keep_alive(self):
        """简单保持进程运行"""
        try:
            while True:
                pass
        except KeyboardInterrupt:
            logger.info("MCP 天气服务器已停止")
        
# 创建 MCP 实例
mcp = MCPWeatherServer("WeatherServerSSE", host="127.0.0.1", port=8000)

@mcp.tool()
def get_weather(city: str) -> str:
    """
    查询指定城市的即时天气信息
    参数 city: 城市英文名
    返回: 天气数据的 JSON 字符串
    """
    url = f"https://wttr.in/{city}"
    params = {"format": "j1"}
    headers = {"Accept-Language": "zh-CN"}
    resp = httpx.get(url, params=params, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    # 提取关键字段，返回精简 JSON
    current = data["current_condition"][0]
    result = {
        "city": city,
        "temperature_c": current["temp_C"],
        "humidity_pct": current["humidity"],
        "weather_desc": current["weatherDesc"][0]["value"],
        "feels_like_c": current["FeelsLikeC"],
        "wind_speed_kmph": current["windspeedKmph"],
    }
    logger.info(f"查询 {city} 天气结果：{result}")
    return json.dumps(result, ensure_ascii=False)

if __name__ == "__main__":
    logger.info("启动 MCP SSE 天气服务器，监听 http://127.0.0.1:8000/sse")

    # 运行 MCP 服务
    mcp.run(transport="sse")

    