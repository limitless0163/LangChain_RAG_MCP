import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# 读取环境变量
load_dotenv()

# 实例化模型
model = init_chat_model(
    model="deepseek-v4-flash",
    model_provider="deepseek",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

# 消息列表
messages = "你是谁"

# 调用模型
response = model.invoke(messages)

# 打印结果
print(response.content)

