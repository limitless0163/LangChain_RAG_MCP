import os
from langchain_deepseek import ChatDeepSeek


model = ChatDeepSeek(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

messages = "什么是LangChain?100字以内回答，简洁"

response = model.invoke(messages)

print(response.content)

