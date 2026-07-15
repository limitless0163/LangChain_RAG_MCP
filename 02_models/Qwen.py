import os
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage

model = ChatTongyi(
    model="qwen-plus",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
)

print(model.invoke("你是谁"))

print("*" * 60)

res = model.stream([HumanMessage(content="你好，你是谁")], streaming=True)

for r in res:
    print("chat resp:", r.content)
