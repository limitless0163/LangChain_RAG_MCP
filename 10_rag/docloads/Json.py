from langchain_community.document_loaders import JSONLoader


loader = JSONLoader(
    file_path="10_rag/docloads/assets/sample.json",
    jq_schema=".",  # 提取所有字段
    text_content=False, # 提取内容是否为字符串格式
)
docs = loader.load()

print(docs)

