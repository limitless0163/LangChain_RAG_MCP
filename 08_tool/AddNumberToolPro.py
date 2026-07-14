from langchain_core.tools import tool
from loguru import logger
from pydantic import BaseModel, Field


class FieldInfo(BaseModel):
    """定义加法运算所需的参数信息"""
    a: int = Field(description="第一个参数")
    b: int = Field(description="第二个参数")

# 通过args_schema定义参数信息
@tool(args_schema=FieldInfo)
def add_number(a: int, b: int) -> int:
    return a + b

# 打印工具的基本信息
logger.info(f"name = {add_number.name}")
logger.info(f"args = {add_number.args}")
logger.info(f"description = {add_number.description}")
logger.info(f"return_direct = {add_number.return_direct}")

# 调用工具执行加法运算
response = add_number.invoke({"a": 1, "b": 2})
logger.info(response)

