from langchain_community.document_loaders import PyMuPDFLoader


loader = PyMuPDFLoader(
    file_path="10_rag/docloads/assets/sample.pdf",
)
docs = loader.load()

print(docs)