import json
import httpx
from langchain_core.tools import tool


@tool
def get_weather(loc):
    """
    查询即时天气函数

    :param loc: 必要参数，字符串类型，用于表示查询天气的具体城市名称
                注意中国的城市要用对应城市的英文名称代替
    :return: wttr.in 天气 API 查询结果，JSON 格式字符串。
             包含温度、湿度、天气描述等关键信息。
    """
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

# 测试
result = get_weather.invoke("beijing")
print(result)

