from langchain_community.document_loaders import Docx2txtLoader


loader = Docx2txtLoader(
    file_path="10_rag/docloads/assets/sample.docx",
)
docs = loader.load()

print(docs)