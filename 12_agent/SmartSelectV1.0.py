import json
import os
import httpx
from typing_extensions import TypedDict
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


# Tool 定义
@tool
def get_weather(loc: str) -> str:
    """查询即时天气函数"""
    
    url = f"https://wttr.in/{loc}"
    params = {"format": "j1"}
    headers = {"Accept-Language": "zh-CN"}
    response = httpx.get(url, params=params, headers=headers, timeout=30)
    response.raise_for_status()
    data = response.json()

    # 提取关键字段，返回精简 JSON
    current = data["current_condition"][0]
    result = {
        "city": loc,
        "temperature_c": current["temp_C"],
        "humidity_pct": current["humidity"],
        "weather_desc": current["weatherDesc"][0]["value"],
        "feels_like_c": current["FeelsLikeC"],
        "wind_speed_kmph": current["windspeedKmph"],
    }
    return json.dumps(result, ensure_ascii=False)

# 结构化输出
class WeatherCompareOutput(TypedDict):
    beijing_temp: float
    shanghai_temp: float
    hotter_city: str
    summary: str

# 初始化模型
model = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com",
    extra_body={"thinking": {"type": "disabled"}},   # 禁用思考模式
)

# 创建 Agent
agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt=(
        "你是天气助手。"
        "当用户询问多个城市天气时，"
        "你需要分别调用工具获取数据，并进行比较分析。"
    ),
    response_format=WeatherCompareOutput,
)

# 调用Agent
result = agent.invoke(
    {"input": "请问今天北京和上海的天气怎么样，哪个城市更热？"}
)

print(result)

print()

print(json.dumps(result["structured_response"], ensure_ascii=False, indent=2))