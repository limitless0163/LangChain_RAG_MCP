import os
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.prompts import PromptTemplate
from langchain_classic.text_splitter import CharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Redis


model = init_chat_model(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

prompt_template = """
    请使用以下提供的文本内容来回答问题。仅使用提供的文本信息，
    如果文本中没有相关信息，请回答"抱歉，提供的文本中没有这个信息"。

    文本内容：{context}

    问题：{question}

    回答：
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# 初始化 Embedding 模型
embeddings = DashScopeEmbeddings(
    model="text-embedding-v4",
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
)

# 加载文档
loader = Docx2txtLoader("10_rag/alibaba-java.docx")
documents = loader.load()

# 分割文档
text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0,
    length_function=len
)
texts = text_splitter.split_documents(documents)

print(f"文档个数：{len(texts)}")

# 创建向量存储
vector_store = Redis.from_documents(
    documents=documents,
    embedding=embeddings,
    redis_url="redis://localhost:6379",
    index_name="my_index3",
)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# 创建Runnable链
rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | model
)

# 提问
question = "00000和A0001分别是什么意思"
result = rag_chain.invoke(question)
print("\n问题:", question)
print("\n回答:", result.content)


