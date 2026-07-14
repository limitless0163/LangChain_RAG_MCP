import json
import os
import httpx
from langchain_core.tools import tool


@tool
def get_weather(loc):
    """
    查询即时天气函数

    :param loc: 必要参数，字符串类型，用于表示查询天气的具体城市名称
                注意中国的城市要用对应城市的英文名称代替
    :return: OpenWeather API 查询即时天气的结果。
             返回结果对象类型为解析之后的 JSON 格式对象，并用字符串形式进行表示
             其中包含了全部重要的天气信息
    """
    # 1.构建请求URL
    url = "https://api.openweathermap.org/data/2.5/weather"

    # 2.设置查询参数
    params = {
        "q": loc,
        "appid": os.getenv("OPENWEATHER_API_KEY"),  # 从环境变量中读取 API Key, 在 https://home.openweathermap.org/users/sign_in 上申请
        "units": "metric",  # 使用摄氏度
        "lang": "zh_cn"  # 输出语言为简体中文
    }

    # 3.发送 GET 请求获取天气数据
    response = httpx.get(url, params=params, timeout=30)

    # 4.解析响应内容为 JSON 并序列化为字符串返回
    data = response.json()

    return json.dumps(data)

# 测试
result = get_weather.invoke("beijing")
print(result)

