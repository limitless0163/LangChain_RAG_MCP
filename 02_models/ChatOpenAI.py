import os
from langchain_openai import ChatOpenAI


model = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你是谁？"}
]

response = model.invoke(messages)

print(response.content)

