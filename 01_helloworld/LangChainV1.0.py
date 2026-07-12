# langchain 1.0+ 版本使用方式，目前主流，多模型共存

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os


# .env文件读取
load_dotenv()

# 实例化模型
model = init_chat_model(
    model="deepseek-v4-flash",
    model_provider="deepseek",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

# 调用模型
print(model.__dict__)
print(model.invoke("你是谁").content)

