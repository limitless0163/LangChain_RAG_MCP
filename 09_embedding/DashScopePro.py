import dashscope
import json
import os
from http import HTTPStatus


# 调用 embedding 模型
resp = dashscope.TextEmbedding.call(
    model="text-embedding-v4",  
    api_key=os.getenv("DASHSCOPE_API_KEY"),  
    input="limitless"
)

result = ""

# 处理模型返回结果，提取关键信息并格式化输出
if resp.status_code == HTTPStatus.OK:
    result = {
        "status_code": resp.status_code,
        "request_id": getattr(resp, "request_id", ""),
        "code": getattr(resp, "code", ""),
        "message": getattr(resp, "message", ""),
        "output": resp.output,
        "usage": resp.usage
    }
    print(json.dumps(result, ensure_ascii=False, indent=4))
else:
    print(f"请求失败: status_code={resp.status_code}, code={resp.code}, message={resp.message}")


