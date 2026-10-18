![Machine Learning](https://capsule-render.vercel.app/api?type=waving&color=0:102a43,100:33adff&height=220&section=header&text=Machine%20Learning&fontSize=48&fontColor=ffffff&animation=fadeIn&desc=Preprocessing%20%E2%80%A2%20Regression%20%E2%80%A2%20Classification%20%E2%80%A2%20Ensembles%20%E2%80%A2%20Clustering&descSize=17&descAlignY=68)

### 🤖 A complete hands-on Machine Learning path with scikit-learn

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge) ![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

**✨ Created by Muhammad Adnan ✨**

`Machine Learning` • `Supervised Learning` • `Unsupervised Learning` • `Model Selection`

---

## 📑 Table of Contents

- 🎯 About
- 🗺️ Learning Path
- 📚 Notebooks
- 🗂️ Repository Structure
- ⚡ Quick Start
- 📂 Datasets
- 🧰 Tech Stack
- 👤 Author

---

## 🎯 About

This section is a **step-by-step journey** through classical Machine Learning — built the way it is actually learned: data preprocessing first, then **Regression**, **Classification**, **Ensemble Learning** and **Unsupervised Learning**. Every topic section ends with a full **model-selection notebook** that compares all models with cross-validation and hyperparameter tuning.

| ✅ Feature | Description |
| --- | --- |
| 🎨 **Banner & Objective** | Each notebook opens with a title banner and an *About / Objective / Topics* card |
| 🧩 **Clear sections** | Topics are split into easy, colour-marked sections |
| 💻 **Runnable code** | Short, focused code cells you can run and modify |
| 📊 **Saved outputs** | Tables and charts are visible directly on GitHub, no need to run anything |
| 🏆 **Model selection** | Every section closes with a best-model comparison notebook |

---

## 🗺️ Learning Path

```
flowchart LR
    A["🧹 Preprocessing"] --> B["📈 Regression"]
    B --> C["🎯 Classification"]
    C --> D["🧺 Ensemble Learning"]
    D --> E["🔍 Unsupervised Learning"]
    style A fill:#102a43,color:#fff,stroke:#33adff
    style B fill:#102a43,color:#fff,stroke:#33adff
    style C fill:#102a43,color:#fff,stroke:#33adff
    style D fill:#102a43,color:#fff,stroke:#33adff
    style E fill:#102a43,color:#fff,stroke:#33adff
```

> 💡 **Tip:** follow the sections in order — the datasets cleaned in Section 1 are exactly what Sections 2, 3 and 4 train on.

---

## 📚 Notebooks

### 🧹 Data Preprocessing

| Notebook | What you will learn |
| --- | --- |
| [Diabetes Data Preprocessing](1.%20Data_Preprocessing/For_Classification/Diabetes_Data_Preprocessing.ipynb) | Missing values, outliers, encoding & scaling — before/after CSVs included |
| [Concrete Data Preprocessing](1.%20Data_Preprocessing/For_Regression/Concrete_Data_Preprocessing.ipynb) | Full cleaning pipeline for the Concrete Strength dataset |

### 📈 Regression — Concrete Strength

| Notebook | What you will learn |
| --- | --- |
| [Linear, Polynomial, Lasso, Ridge & ElasticNet](2.%20Regression/1.%20Linear_Polynomial_Lesso_Ridge_ElasticNet.ipynb) | Regularized linear models with hyperparameter tuning |
| [KNN Regression](2.%20Regression/2.%20KNN_Regression.ipynb) | Distance-based regression with feature scaling |
| [Decision Tree Regression](2.%20Regression/3.%20DecisionTree_Regression.ipynb) | Tree regression, depth control & pruning |
| [SVR Regression](2.%20Regression/4.%20SVR_Regression.ipynb) | Support Vector Regression with different kernels |
| [Best Regression Model Selection](2.%20Regression/Best_Regression_Model_Selection.ipynb) | All regressors compared: cross-validation, tuning & leaderboard |

### 🎯 Classification — Diabetes

| Notebook | What you will learn |
| --- | --- |
| [Logistic Regression & Softmax](3.%20Classification/1.%20Logistic_Softmax.ipynb) | Binary + multinomial classification |
| [KNN Classification](3.%20Classification/2.%20KNN_Classification.ipynb) | Neighbors, distance metrics & tuning |
| [Naive Bayes Classification](3.%20Classification/3.%20NaiveBayes_Classification.ipynb) | Gaussian / Multinomial / Bernoulli Naive Bayes |
| [SVC Classification](3.%20Classification/4.%20%20SVC_Classification.ipynb) | SVM kernels & margin tuning |
| [Decision Tree Classification](3.%20Classification/5.%20Decision_Tree_Classification.ipynb) | Splits, pruning & feature importance |
| [Best Classification Model Selection](3.%20Classification/Best_Classification_Model_Selection.ipynb) | All classifiers compared: cross-validation, tuning & leaderboard |

### 🧺 Ensemble Learning — Concrete Strength

| Notebook | What you will learn |
| --- | --- |
| [Bagging](4.%20Ensemble_Learning/1.%20Bagging.ipynb) | Bootstrap aggregating & the Random Forest idea |
| [Boosting](4.%20Ensemble_Learning/2.%20Boosting.ipynb) | AdaBoost & gradient boosting workflows |
| [Voting](4.%20Ensemble_Learning/3.%20Voting.ipynb) | Hard & soft voting ensembles |
| [Stacking](4.%20Ensemble_Learning/4.%20Stacking.ipynb) | Meta-learner trained on base model predictions |

### 🔍 Unsupervised Learning — HR Dataset

| Notebook | What you will learn |
| --- | --- |
| [HR Data Preprocessing](Unsupervised_Learning/01_HR_Data_Preprocessing.ipynb) | Prepares the HR dataset; generates the cleaned CSVs used by the notebooks below |
| [K-Means++ Clustering](Unsupervised_Learning/02_KMeansPlusPlus_Clustering.ipynb) | Centroid clustering with smart seeding |
| [Hierarchical Clustering](Unsupervised_Learning/03_Hierarchical_Clustering.ipynb) | Agglomerative clustering & dendrograms |
| [DBSCAN Clustering](Unsupervised_Learning/04_DBSCAN_Clustering.ipynb) | Density-based clustering & noise handling |
| [OPTICS Clustering](Unsupervised_Learning/05_OPTICS_Clustering.ipynb) | Ordering-based density clustering |
| [HDBSCAN Clustering](Unsupervised_Learning/06_HDBSCAN_Clustering.ipynb) | Hierarchical density-based clustering |
| [Best Clustering Model Selection](Unsupervised_Learning/07_Best_Model_Selection.ipynb) | Clustering methods compared with internal validation metrics |

---

## 🗂️ Repository Structure

```
02-machine-learning/
├── 📁 1. Data_Preprocessing/
│   ├── 📁 For_Classification/   # Diabetes: notebook + before/after CSVs
│   └── 📁 For_Regression/       # Concrete: notebook + before/after CSVs
├── 📁 2. Regression/            # 5 notebooks — Concrete Strength
├── 📁 3. Classification/        # 6 notebooks — Diabetes
├── 📁 4. Ensemble_Learning/     # Bagging, Boosting, Voting, Stacking
├── 📁 Unsupervised_Learning/   # 7 notebooks + hr_raw_data.csv
└── 📄 README.md
```

---

## ⚡ Quick Start

```bash
# 1️⃣ Clone the repository
git clone https://github.com/AdnanCodex/ai-engineering-notes.git
cd ai-engineering-notes/02-machine-learning

# 2️⃣ Install the dependencies
pip install pandas numpy scikit-learn matplotlib seaborn jupyter

# 3️⃣ Launch Jupyter
jupyter lab
```

**📌 Good to know**

- Dataset paths inside the notebooks are **repo-relative** (`../1. Data_Preprocessing/...`), so everything runs as-is after cloning — no path editing needed.
- Saved outputs are kept, so you can read everything directly on GitHub.
- For Unsupervised Learning, run `01_HR_Data_Preprocessing.ipynb` first — it generates the intermediate CSVs the other notebooks read.

---

## 📂 Datasets

| Dataset | Used in | Files |
| --- | --- | --- |
| **Diabetes** | Data Preprocessing, Classification | `diabetes_before_preprocessing.csv`, `diabetes_after_preprocessing.csv` |
| **Concrete Strength** | Data Preprocessing, Regression, Ensemble Learning | `concrete_before_preprocessing.csv`, `concrete_after_preprocessing.csv` |
| **HR (synthetic)** | Unsupervised Learning | `hr_raw_data.csv` (included); cleaned versions are generated by the preprocessing notebook |

> The Concrete preprocessing notebook expects the original `Concrete_Data.xls` upload — the already-cleaned CSVs are included here, so all downstream notebooks work without it.

---

## 🧰 Tech Stack

|  | Library | Used for |
| --- | --- | --- |
| 🐍 | **Python 3** | Core language |
| 🔢 | **NumPy** | Numerical computing |
| 🐼 | **Pandas** | Data analysis and wrangling |
| 🤖 | **scikit-learn** | ML models, tuning & evaluation |
| 📈 | **Matplotlib** | Basic plotting |
| 🎨 | **Seaborn** | Statistical visualization |
| 📓 | **Jupyter** | Notebook environment |

---

## 👤 Author

### ✨ Created by **Muhammad Adnan** ✨

*Artificial Intelligence • Machine Learning • Data Science*

⭐ If this section helped you, give the repository a star!

![footer](https://capsule-render.vercel.app/api?type=waving&color=0:33adff,100:102a43&height=100&section=footer)
