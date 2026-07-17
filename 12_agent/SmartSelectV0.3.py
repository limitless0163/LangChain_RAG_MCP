import os
import json
import httpx
from langchain_openai import ChatOpenAI
from langchain_classic.agents import create_tool_calling_agent
from langchain_classic.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool


@tool
def get_weather(loc):
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
    print(json.dumps(result, ensure_ascii=False))
    return json.dumps(result, ensure_ascii=False)

# 初始化模型
model = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

# 创建聊天提示模板
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是天气助手，请根据用户的问题，给出相应的天气信息"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

# 定义可用工具列表
tools = [get_weather]

# 创建调用工具Agent
agent = create_tool_calling_agent(model, tools, prompt)

# 创建agent执行器
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 执行agent
result = agent_executor.invoke({"input": "请问今天北京和上海的天气怎么样，哪个城市更热？"})

# 输出执行结果
print(result)

