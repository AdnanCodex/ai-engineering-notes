from langchain_community.document_loaders import WebBaseLoader

docs = WebBaseLoader("https://example.com").load()
print(docs[0].page_content[:200])
