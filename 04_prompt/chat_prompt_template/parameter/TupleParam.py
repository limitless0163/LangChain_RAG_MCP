from langchain_core.prompts import ChatPromptTemplate


chat_prompt = ChatPromptTemplate(
    [
        ("system", "你是一个AI开发工程师，你的名字是{name}。"),
        ("human", "你能帮我做什么?"),
        ("ai", "我能开发很多{thing}。"),
        ("human", "{user_input}"),
    ]
)

messages = chat_prompt.format_messages(name="小谷AI", thing="AI", user_input="7 + 5等于多少")

print(messages)