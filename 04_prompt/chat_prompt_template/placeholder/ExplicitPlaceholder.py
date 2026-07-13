from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# 显式使用MessagesPlaceholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个资深的Python应用开发工程师，请认真回答我提出的Python相关的问题"),
    MessagesPlaceholder("memory"),
    ("human", "{question}")
])

prompt_value = prompt.invoke({
    "memory": [
        HumanMessage("我的名字叫亮仔，是一名程序员"),
        AIMessage("好的，亮仔你好"),
    ],
    "question": "请问我的名字叫什么？"
})

print(prompt_value.to_string())