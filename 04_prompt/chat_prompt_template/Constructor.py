import os
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model


messages = ChatPromptTemplate(
    [
        ("system", "你是一个AI开发工程师，你的名字是{name}。"),
        ("human", "你能帮我做什么?"),
        ("ai", "我能开发很多{thing}。"),
        ("human", "{user_input}"),
    ]
)

prompt = messages.format_messages(
    name="小谷AI", thing="AI", user_input="7 + 5等于多少"
)

model = init_chat_model(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

response = model.invoke(prompt)

print(response.content)