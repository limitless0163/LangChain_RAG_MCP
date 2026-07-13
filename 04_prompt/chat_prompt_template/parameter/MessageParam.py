from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate


chat_prompt = ChatPromptTemplate(
    [
        SystemMessagePromptTemplate.from_template("你是AI助手，你的名字叫{name}"),
        HumanMessagePromptTemplate.from_template("请问：{question}")
    ]
)

message = chat_prompt.format_messages(name="亮仔", question="什么是LangChain")

print(message)