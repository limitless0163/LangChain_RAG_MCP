import os
from typing import TypedDict, Annotated
from langchain.chat_models import init_chat_model


model = init_chat_model(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com",
    extra_body={"thinking": {"type": "disabled"}}   # with_structured_output()底层通过function calling/tool_choice来强制LLM输出指定格式，与Deepseek的Thinking模式互斥 
)

class Animal(TypedDict):
    animal: Annotated[str, "动物"]
    emoji: Annotated[str, "表情"]

class AnimalList(TypedDict):
    animals: Annotated[list[Animal], "动物与表情列表"]

messages = [{"role": "user", "content": "任意生成三种动物，以及他们的 emoji 表情"}]

model_with_structured_output = model.with_structured_output(AnimalList)
response = model_with_structured_output.invoke(messages)
print(response)
