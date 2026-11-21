from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

from langchain_community.document_loaders import DirectoryLoader, TextLoader

docs = DirectoryLoader(str(DATA), glob="*.txt", loader_cls=TextLoader).load()
print(len(docs), [d.metadata["source"] for d in docs])
