import os
import redis    # 版本5.3.1
from langchain.chat_models import init_chat_model
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableConfig
from loguru import logger


REDIS_URL = "redis://localhost:6379"

# 创建原生Redis客户端, decode_responses 控制 Redis 返回数据的类型：False 返字节串，True 返字符串
redis_client = redis.Redis.from_url(REDIS_URL, decode_response=True)

# 初始化模型
model = init_chat_model(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

# 创建提示词模板
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder("history"),
    ("human", "{question}")
])

def get_session_history(session_id: str) -> RedisChatMessageHistory:
    """获取或创建会话历史（使用Redis）"""
    history = RedisChatMessageHistory(
        session_id=session_id,
        url=REDIS_URL,
        ttl=3600    # 关闭自动过期，避免重启后数据被清理
    )

    return history

# 创建带历史记录的链
chain = RunnableWithMessageHistory(
    prompt | model,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

# 配置
config = RunnableConfig(configurable={"session_id": "user-001"})

# 主循环流程
while True:
    question = input("输入问题：")
    if question.lower() in ['quit', 'exit', 'q']:
        break

    response = chain.invoke({"question": question}, config)
    logger.info(f"AI回答：{response.content}")

    redis_client.save()