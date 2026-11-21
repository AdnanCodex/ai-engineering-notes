from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

from langchain_community.document_loaders import CSVLoader

docs = CSVLoader(file_path=str(DATA / "sample.csv")).load()
print(len(docs))
print(docs[0].page_content)
