<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:102a43,100:33adff&height=220&section=header&text=Data%20Science%20Notebooks&fontSize=48&fontColor=ffffff&animation=fadeIn&desc=Python%20%E2%9E%9C%20NumPy%20%E2%9E%9C%20Pandas%20%E2%9E%9C%20Visualization%20%E2%9E%9C%20Cleaning%20%E2%9E%9C%20EDA&descSize=18&descAlignY=68" alt="Data Science Notebooks"/>

### 🚀 A complete hands-on learning path for Data Science & AI in Python

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-4c72b0?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

**✨ Created by [Muhammad Adnan](#-author) ✨**

`Artificial Intelligence` • `Python` • `Problem Solving`

</div>

---

## 📑 Table of Contents

- [🎯 About](#-about)
- [🗺️ Learning Path](#️-learning-path)
- [📚 Notebooks](#-notebooks)
- [🗂️ Repository Structure](#️-repository-structure)
- [⚡ Quick Start](#-quick-start)
- [📂 Datasets](#-datasets)
- [🧰 Tech Stack](#-tech-stack)
- [👤 Author](#-author)

---

## 🎯 About

This repository is a **step-by-step journey** from the first line of Python to real data analysis. Every notebook is built in the same clean style:

| ✅ Feature | Description |
|---|---|
| 🎨 **Banner & Objective** | Each notebook opens with a title banner and an *About / Objective / Topics* card |
| 🧩 **Clear sections** | Topics are split into easy, colour-marked sections |
| 💻 **Runnable code** | Short, focused code cells you can run and modify |
| 📊 **Saved outputs** | Tables and charts are visible directly on GitHub, no need to run anything |
| 🏋️ **Practice** | Exercises and real-world datasets (Titanic, IPL, IMDB, clinical trials) |

---

## 🗺️ Learning Path

```mermaid
flowchart LR
    A["🐍 Python"] --> B["🔢 NumPy"]
    B --> C["🐼 Pandas"]
    C --> D["📈 Matplotlib"]
    D --> E["🎨 Seaborn"]
    E --> F["🧹 Data Cleaning"]
    F --> G["🔍 EDA"]
    style A fill:#102a43,color:#fff,stroke:#33adff
    style B fill:#102a43,color:#fff,stroke:#33adff
    style C fill:#102a43,color:#fff,stroke:#33adff
    style D fill:#102a43,color:#fff,stroke:#33adff
    style E fill:#102a43,color:#fff,stroke:#33adff
    style F fill:#102a43,color:#fff,stroke:#33adff
    style G fill:#102a43,color:#fff,stroke:#33adff
```

> 💡 **Tip:** follow the folder numbers from `01` to `06` for the best learning experience.

---

## 📚 Notebooks

### 🐍 01 · Python
| Notebook | What you will learn |
|---|---|
| [Python Programming](01_Python/01_Python_Programming.ipynb) | Syntax, data types, control flow, functions, OOP, file handling: beginner to advanced |

### 🔢 02 · NumPy
| Notebook | What you will learn |
|---|---|
| [NumPy Handbook](02_NumPy/01_NumPy_Handbook.ipynb) | Arrays, indexing, broadcasting, math & statistics: beginner to pro |

### 🐼 03 · Pandas
| Notebook | What you will learn |
|---|---|
| [DataFrames](03_Pandas/01_Pandas_DataFrames.ipynb) | Create, select, filter and transform tables |
| [String Methods](03_Pandas/02_Pandas_Strings.ipynb) | Vectorized text processing with `.str` |
| [GroupBy](03_Pandas/03_Pandas_GroupBy.ipynb) | Split → Apply → Combine, `agg`, `apply` |
| [Merging & Joins](03_Pandas/04_Pandas_Merging_and_Joins.ipynb) | `concat`, `merge`, inner / left / right / outer / self joins |
| [MultiIndex & Pivot](03_Pandas/05_Pandas_MultiIndex_and_Pivot.ipynb) | Hierarchical index, stack / unstack, pivot tables |
| [Date & Time](03_Pandas/06_Pandas_DateTime.ipynb) | `Timestamp`, `DatetimeIndex`, `date_range`, `dt` accessor |

### 📈 04 · Data Visualization
| Notebook | What you will learn |
|---|---|
| [Matplotlib](04_Data_Visualization/01_Matplotlib.ipynb) | Scatter, bar, histogram, pie charts, styles and saving figures |
| [Seaborn](04_Data_Visualization/02_Seaborn.ipynb) | Relational, distribution, matrix, categorical, regression and multi-plots |

### 🧹 05 · Data Cleaning
| Notebook | What you will learn |
|---|---|
| [Data Accessing & Cleaning](05_Data_Cleaning/01_Data_Accessing_and_Cleaning.ipynb) | Assess and clean a clinical-trial dataset using **Define → Code → Test** |

### 🔍 06 · Exploratory Data Analysis
| Notebook | What you will learn |
|---|---|
| [Titanic EDA](06_EDA/01_Titanic_EDA.ipynb) | Univariate and bivariate analysis, feature engineering, key findings |

---

## 🗂️ Repository Structure

```text
data-science-notebooks/
├── 📁 01_Python/
├── 📁 02_NumPy/
├── 📁 03_Pandas/
├── 📁 04_Data_Visualization/
├── 📁 05_Data_Cleaning/
├── 📁 06_EDA/
├── 🖼️ assets/images/      # images used inside notebooks
├── 📂 data/               # put datasets here (see data/README.md)
├── 📄 requirements.txt
└── 📄 README.md
```

---

## ⚡ Quick Start

```bash
# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/data-science-notebooks.git
cd data-science-notebooks

# 2️⃣ (Optional) create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3️⃣ Install the dependencies
pip install -r requirements.txt

# 4️⃣ Launch Jupyter
jupyter lab
```

<details>
<summary><b>📌 Good to know</b></summary>

- Notebooks were first written in Google Colab; file paths now use `../data/...` so they work locally.
- `DataFrame.append()` was removed in pandas 2.0, so the notebooks use `pd.concat()`.
- Saved outputs are kept, so you can read everything directly on GitHub.

</details>

---

## 📂 Datasets

Datasets are **not stored** in this repository. Each notebook reads its files from the `data/` folder (for example `../data/train.csv`).
👉 The complete list of files needed per notebook is in [`data/README.md`](data/README.md).

---

## 🧰 Tech Stack

| | Library | Used for |
|---|---|---|
| 🐍 | **Python 3** | Core language |
| 🔢 | **NumPy** | Numerical computing |
| 🐼 | **Pandas** | Data analysis and wrangling |
| 📈 | **Matplotlib** | Basic plotting |
| 🎨 | **Seaborn** | Statistical visualization |
| ✨ | **Plotly** | Interactive charts |
| 📓 | **Jupyter** | Notebook environment |

---

## 👤 Author

<div align="center">

### ✨ Created by **Muhammad Adnan** ✨

*Artificial Intelligence • Python • Data Science*

⭐ If this repository helped you, give it a star!

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:33adff,100:102a43&height=100&section=footer" alt="footer"/>

</div>
