from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

py_code = '''
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"
'''

splitter = RecursiveCharacterTextSplitter.from_language(Language.PYTHON, chunk_size=80, chunk_overlap=0)
for chunk in splitter.split_text(py_code):
    print("---")
    print(chunk)
