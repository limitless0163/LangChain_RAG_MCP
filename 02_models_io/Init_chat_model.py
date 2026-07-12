import os
from langchain.chat_models import init_chat_model


model = init_chat_model(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

messages = "你是谁"

response = model.invoke(messages)

print(response.content)