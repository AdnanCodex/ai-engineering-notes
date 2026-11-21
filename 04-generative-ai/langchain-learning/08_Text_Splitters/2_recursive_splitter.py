from langchain_text_splitters import RecursiveCharacterTextSplitter

TEXT = (
    "LangChain is a framework for building LLM applications. "
    "Text splitters break large documents into smaller chunks. "
    "Chunk overlap preserves context between neighbouring chunks.\n\n"
) * 5

splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=40)
chunks = splitter.split_text(TEXT)
print(len(chunks))
print(chunks[0])
