import os
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from loguru import logger


# 创建聊天提示模板，定义系统角色和用户输入格式
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}，请简短回答我提出的问题，结果返回json格式，q字段表示问题，a字段表示答案。"),
    ("human", "请回答:{question}")
])

# 格式化提示词，填入具体主题和格式化指令
prompt = chat_prompt.invoke({"role": "AI助手", "question": "什么是LangChain，简洁回答100字以内"})

# 记录格式化后的提示词信息
logger.info(prompt)

# 初始化模型
model = init_chat_model(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

# 调用模型获取响应结果
result = model.invoke(prompt)

# 记录模型返回结果
logger.info(f"模型原始输出：\n{result}")

# 创建JSON输出解析器实例
parser = JsonOutputParser()

# 调用解析器处理结果数据，将输入转换为JSON格式的响应
response = parser.invoke(result)
logger.info(f"解析后的结构化结果：\n{response}")
