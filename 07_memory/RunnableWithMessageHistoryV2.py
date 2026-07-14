import os
from langchain.chat_models import init_chat_model
from langchain_core.chat_history import InMemoryChatMessageHistory  # 内存型消息记录
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser


# 初始化模型
model = init_chat_model(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

# 定义全局的“会话存储”，实际项目中可改成Redis,SQLite等
store = {}

def get_session_history(session_id: str):
    """
    根据 session_id 获取对应的历史消息对象
    如果不存在则创建一个新的 InMemoryChatMessageHistory
    """
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 创建提示词模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个友好的中文助理，会根据上下文回答问题。"),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])

# 构建基本链
memory_chain = prompt | model | StrOutputParser()

# 将链包装为支持记忆的版本
with_history = RunnableWithMessageHistory(
    memory_chain,           # 原始链
    get_session_history,    # 获取历史函数
    input_messages_key="question",  # 对应 prompt 输入的key
    history_messages_key="history", # 对应 MessagesPlaceholder 的变量名
)

# 模拟对话，用 session_id 区分不同用户
config = {"configurable": {"session_id": "user-001"}}

# 第一次提问
print("用户：我叫张三。")
print("AI：", with_history.invoke({"question": "我叫张三。"}, config))

# 第二次提问：让模型回忆前面的对话
print("\n用户：我叫什么？")
print("AI：", with_history.invoke({"question": "我叫什么？"}, config))