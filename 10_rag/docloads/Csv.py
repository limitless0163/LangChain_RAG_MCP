from langchain_community.document_loaders.csv_loader import CSVLoader


# 加载所有列
loader = CSVLoader(
    file_path="10_rag/docloads/assets/sample.csv",
    encoding="utf-8",
)
docs = loader.load()

print(docs)

# 加载部分列
loader = CSVLoader(
    file_path="10_rag/docloads/assets/sample.csv",
    metadata_columns=["title", "author"],
    content_columns=["content"],
)
docs = loader.load()

print(docs)

