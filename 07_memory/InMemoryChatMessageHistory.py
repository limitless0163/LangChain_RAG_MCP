import os
from langchain.chat_models import init_chat_model
from langchain_core.chat_history import InMemoryChatMessageHistory
from loguru import logger


# 初始化模型
model = init_chat_model(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

# 创建内存聊天历史记录
history = InMemoryChatMessageHistory()

# 添加用户消息到聊天历史记录
history.add_user_message("我叫张三，我的爱好是学习")

# 调用模型处理聊天历史记录信息
ai_message = model.invoke(history.messages)

# 输出AI回复的内容
logger.info(f"第一次回答\n{ai_message.content}")

# 将AI回复添加到聊天历史记录中
history.add_message(ai_message)

# 添加新的用户消息到聊天历史记录
history.add_user_message("我叫什么？我的爱好是什么？")

# 再次调用模型处理聊天历史记录信息
ai_message2 = model.invoke(history.messages)

# 输出第二次AI回复的内容
logger.info(f"第二次回答\n{ai_message2.content}")

# 将第二次AI回复添加到聊天历史记录中
history.add_message(ai_message2)

# 遍历并输出所有聊天历史记录中的消息内容
for message in history.messages:
    logger.info(message.content)