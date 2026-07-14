import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory, RunnableConfig
from langchain.chat_models import init_chat_model
from langchain_core.chat_history import InMemoryChatMessageHistory
from loguru import logger


# 初始化模型
model = init_chat_model(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

# 定义提示词模板
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

parser = StrOutputParser()

# 构建处理链
chain = prompt | model | parser

# 创建内存聊天历史记录实例
history = InMemoryChatMessageHistory()

# 创建带消息历史的可运行对象
runnable = RunnableWithMessageHistory(
    chain,
    get_session_history= lambda session_id: history,
    input_messages_key="input", # 指定输入键
    history_messages_key="history"  # 指定历史消息键
)

# 清空历史记录
history.clear()

# 配置参数
config = RunnableConfig(configurable={"session_id": "user-001"})

logger.info(runnable.invoke({"input": "我叫张三，我爱好学习。"}, config))
logger.info(runnable.invoke({"input": "我叫什么？我的爱好是什么？"}, config))

