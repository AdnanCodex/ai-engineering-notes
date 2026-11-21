from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

from langchain_community.document_loaders import TextLoader

docs = TextLoader(str(DATA / "sample.txt"), encoding="utf-8").load()
print(len(docs), docs[0].metadata)
print(docs[0].page_content)
