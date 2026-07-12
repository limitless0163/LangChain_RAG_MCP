import os
from langchain_openai import ChatOpenAI


model = ChatOpenAI(
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com",
    model="deepseek-v4-flash"
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你是谁？"}
]

response = model.invoke(messages)

print(response.content)

