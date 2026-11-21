from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

from langchain_community.document_loaders import PyPDFLoader

pdf_path = DATA / "your_file.pdf"  # put any PDF in data/ and change the name
if pdf_path.exists():
    pages = PyPDFLoader(str(pdf_path)).load()  # use lazy_load() for large files
    print(len(pages), pages[0].metadata)
else:
    print("Add a PDF to data/ to try this script.")
