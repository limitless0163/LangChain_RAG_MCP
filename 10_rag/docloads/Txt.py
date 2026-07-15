from langchain_community.document_loaders import TextLoader


loader = TextLoader(
    file_path="10_rag/docloads/assets/sample.txt",
    encoding = "utf-8",
)
docs = loader.load()

print(docs)