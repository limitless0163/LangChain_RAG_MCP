from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader


# 创建文档加载器
loader = TextLoader(
    file_path="10_rag/textsplit/rag.txt",
    encoding="utf-8"
)
documents = loader.load()

# 定义递归文本分割器
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=30,
    length_function=len
)

# 分割文本
splitter_documents = text_splitter.split_documents(documents)

# 输出分割后的文档信息
print(f"分割文档数量：{len(splitter_documents)}")

for splitter_document in splitter_documents:
    print(f"文档片段：{splitter_document.page_content}")
    print(f"文档片段大小：{len(splitter_document.page_content)}, 文档元数据：{splitter_document.metadata}")

