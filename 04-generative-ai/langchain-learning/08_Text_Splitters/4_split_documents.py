from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

TEXT = (
    "LangChain is a framework for building LLM applications. "
    "Text splitters break large documents into smaller chunks. "
    "Chunk overlap preserves context between neighbouring chunks.\n\n"
) * 5

docs = [Document(page_content=TEXT, metadata={"source": "demo"})]
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=40)
split_docs = splitter.split_documents(docs)  # metadata is kept on every chunk
print(len(split_docs), split_docs[0].metadata)
