import logging
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.exceptions import LangChainException


# 加载环境变量
load_dotenv(encoding='utf-8')

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def init_llm_client() -> ChatOpenAI:
    """初始化LLM客户端"""
    # 1.读取环境变量并做非空校验
    api_key = os.getenv("deepseek-api")
    if not api_key:
        raise ValueError("环境变量 deepseek-api 未配置，请检查 .env 文件")

    # 2.初始化LLM客户端
    llm = ChatOpenAI(
        model="deepseek-v4-flash",  # 模型名称
        api_key=api_key,    # API密钥
        base_url="https://api.deepseek.com",    # 接口地址
        temperature=0.7,    # 温度参数
        max_completion_tokens=2048  # 限制输出长度
    )
    return llm

def main():
    """主函数：封装核心逻辑"""
    try:
        # 初始化客户端
        llm = init_llm_client()
        logger.info("LLM客户端初始化成功")

        # 调用模型
        question = "你是谁"
        response = llm.invoke(question)

        # 格式化输出结果
        logger.info(f"问题：{question}")
        logger.info(f"回答：{response.content}")

        print("=" * 20 + "以下是流式输出" + "=" * 20)

        responseStream = llm.stream("介绍下langchain，300字以内")
        for chunk in responseStream:
            print(chunk.content, end="")
    except ValueError as e:
        logger.error(f"配置错误：{str(e)}")
    except LangChainException as e:
        logger.error(f"模型调用失败：{str(e)}")
    except Exception as e:
        logger.error(f"未知错误：{str(e)}")

if __name__ == "__main__":
    main()