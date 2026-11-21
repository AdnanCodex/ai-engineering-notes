<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1026,50:123524,100:0E7C66&height=180&section=header&text=LangChain%20Learning&fontSize=42&fontColor=F5C542&animation=fadeIn&fontAlignY=38&desc=From%20LLMs%20%26%20Prompts%20to%20RAG%20%26%20AI%20Agents%20%E2%80%94%20hands-on%2C%20one%20concept%20at%20a%20time&descAlignY=58&descSize=14" alt="LangChain Learning banner"/>

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.x-0E7C66?style=for-the-badge)](https://python.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?style=for-the-badge&logo=openai&logoColor=white)](https://platform.openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-F5C542?style=for-the-badge)](LICENSE)

**Part of [AI Engineering Notes](https://github.com/AdnanCodex/ai-engineering-notes) · Section 04 — Generative AI**

</div>

---

## 📖 About

A complete, hands-on **LangChain** learning series — **13 topics, 33 Python scripts and 5 Jupyter notebooks** — built step by step from the fundamentals to a working **RAG pipeline** and a **ReAct AI Agent**.

Every file teaches **one concept only**, is short, self-contained, and runnable top to bottom. Topics `01–08` are standalone Python scripts; topics `09–13` are notebooks.

> 🎯 **Learning rule used throughout:** no topic moves ahead until the previous one runs. Scripts first, notebooks second, projects last.

---

## 🗺️ Learning Roadmap

```text
Models → Prompts → Structured Output → Parsers → Chains → Runnables
   ↓
Document Loaders → Text Splitters → Vector Stores → Retrievers
   ↓
        RAG Pipeline → Tools → AI Agents 🤖
```

---

## 📚 Contents

| # | Topic | What You Learn | Format |
|---|-------|----------------|--------|
| 01 | [LangChain Models](01_Langchain_Models/) | LLMs, chat models, embeddings, document similarity | 5 scripts |
| 02 | [Prompts](02_Prompts/) | Prompt templates, chat templates, message placeholders, a working chatbot | 4 scripts |
| 03 | [Structured Output](03_Structured_Output/) | TypedDict, Pydantic models, JSON Schema | 3 scripts |
| 04 | [Output Parsers](04_Output_Parsers/) | String, JSON and Pydantic output parsers | 3 scripts |
| 05 | [Chains](05_Chains/) | Simple, sequential, parallel and conditional chains | 4 scripts |
| 06 | [Runnables](06_Runnables/) | Lambda, Sequence, Parallel, Passthrough, Branch — *no API key needed* | 5 scripts |
| 07 | [Document Loaders](07_Document_Loaders/) | Text, CSV, directory, web and PDF loaders | 5 scripts |
| 08 | [Text Splitters](08_Text_Splitters/) | Length-based, recursive, code splitters — *no API key needed* | 4 scripts |
| 09 | [Vector Stores](09_Vector_Stores/vector_stores.ipynb) | Chroma DB — create, read, update, delete, metadata filtering | Notebook |
| 10 | [Retrievers](10_Retrievers/retrievers.ipynb) | Wikipedia, MMR, multi-query and contextual compression retrievers | Notebook |
| 11 | [RAG](11_RAG/rag_with_langchain.ipynb) | Full Retrieval-Augmented Generation pipeline — YouTube transcript Q&A | Notebook |
| 12 | [Tools](12_Tools/tools.ipynb) | Built-in tools, custom tools and toolkits | Notebook |
| 13 | [Agents](13_Agents/agents.ipynb) | ReAct agent with search and weather tools | Notebook |

---

## 🚀 Quick Start

```bash
# 1 — Clone the full notes repository
git clone https://github.com/AdnanCodex/ai-engineering-notes.git
cd ai-engineering-notes/04-generative-ai/langchain-learning

# 2 — Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 3 — Install dependencies
pip install -r requirements.txt

# 4 — Add your API keys
cp .env.example .env               # then paste your keys inside .env

# 5 — Run any script
python 01_Langchain_Models/2_chat_model.py
```

For the notebooks (topics `09–13`):

```bash
jupyter lab
```

### ☁️ Open the Notebooks in Google Colab

| Notebook | Colab |
|----------|-------|
| Vector Stores | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/04-generative-ai/langchain-learning/09_Vector_Stores/vector_stores.ipynb) |
| Retrievers | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/04-generative-ai/langchain-learning/10_Retrievers/retrievers.ipynb) |
| RAG with LangChain | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/04-generative-ai/langchain-learning/11_RAG/rag_with_langchain.ipynb) |
| Tools | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/04-generative-ai/langchain-learning/12_Tools/tools.ipynb) |
| Agents | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/04-generative-ai/langchain-learning/13_Agents/agents.ipynb) |

---

## 📂 Project Structure

```text
langchain-learning/
├── 01_Langchain_Models/     # LLMs, chat models, embeddings
├── 02_Prompts/              # Templates, placeholders, chatbot
├── 03_Structured_Output/    # TypedDict, Pydantic, JSON Schema
├── 04_Output_Parsers/       # Str, JSON, Pydantic parsers
├── 05_Chains/               # Simple → conditional chains
├── 06_Runnables/            # LCEL building blocks
├── 07_Document_Loaders/     # Text, CSV, web, PDF
├── 08_Text_Splitters/       # Chunking strategies
├── 09_Vector_Stores/        # Chroma notebook
├── 10_Retrievers/           # Retrieval strategies notebook
├── 11_RAG/                  # End-to-end RAG notebook
├── 12_Tools/                # Tools & toolkits notebook
├── 13_Agents/               # ReAct agent notebook
├── data/                    # Sample .txt / .csv files
├── docs/                    # Learning path, cheat sheet, troubleshooting
├── scripts/                 # Notebook checks & output stripping
├── requirements.txt
└── .env.example             # Copy to .env — never commit real keys
```

---

## 📘 Supporting Docs

- 🛣️ [Learning Path](docs/learning_path.md) — what to study, in what order
- ⚡ [Cheat Sheet](docs/cheatsheet.md) — quick code reference for every topic
- 🛠️ [Troubleshooting](docs/troubleshooting.md) — common errors and their fixes

---

## ⚠️ Important Notes

- 🔑 API keys are loaded from `.env` via `python-dotenv` — **no secret is stored in any file in this folder**.
- 📌 Dependencies are pinned to **LangChain 0.3.x**, because the Agents notebook uses `create_react_agent` and `hub`, which changed in LangChain 1.x.
- 🧪 Every Python script in this folder passes a syntax/compile check, and every notebook passes the stored-output and secret scan in [`scripts/check_notebooks.py`](scripts/check_notebooks.py).
- ⚠️ The Tools notebook demonstrates `ShellTool`, which runs real shell commands — run it only on your own machine and with care.

---

<div align="center">

**Muhammad Adnan** — Aspiring AI Engineer · BS Artificial Intelligence, Hazara University

[![GitHub](https://img.shields.io/badge/GitHub-AdnanCodex-181717?style=for-the-badge&logo=github)](https://github.com/AdnanCodex)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-adnan--ai-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/adnan-ai)

*More sections: [Python for Data Science](https://github.com/AdnanCodex/ai-engineering-notes/tree/main/01-python-for-datascience) · [Machine Learning](https://github.com/AdnanCodex/ai-engineering-notes/tree/main/02-machine-learning) · [Deep Learning](https://github.com/AdnanCodex/ai-engineering-notes/tree/main/03-deep-learning) · [FastAPI](https://github.com/AdnanCodex/ai-engineering-notes/tree/main/05-fastapi) · [Streamlit](https://github.com/AdnanCodex/ai-engineering-notes/tree/main/06-streamlit)*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1026,50:123524,100:0E7C66&height=90&section=footer" alt=""/>

</div>
