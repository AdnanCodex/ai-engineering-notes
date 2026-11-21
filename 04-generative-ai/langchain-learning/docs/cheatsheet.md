# LangChain Cheat Sheet

```python
# Model
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4o-mini")

# Prompt -> model -> parser chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
chain = ChatPromptTemplate.from_template("Explain {x}") | model | StrOutputParser()
chain.invoke({"x": "RAG"})

# Structured output
model.with_structured_output(MyPydanticModel).invoke("...")

# Split -> embed -> store -> retrieve
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)
retriever = FAISS.from_documents(chunks, OpenAIEmbeddings()).as_retriever(search_kwargs={"k": 4})

# Tool
from langchain_core.tools import tool
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b
```

| Concept | Rule of thumb |
|---------|---------------|
| `chunk_size` | 500-1000 chars; `chunk_overlap` about 10-20% |
| Retriever `k` | Start at 3-5 |
| MMR | Use when results are repetitive (`lambda_mult` 0.5) |
| `temperature` | 0 for tools/extraction, 0.2-0.7 for writing |
