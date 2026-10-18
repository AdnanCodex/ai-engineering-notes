# 🤖 Machine Learning

Hands-on **Machine Learning** with scikit-learn, organized the way it is actually learned: data preprocessing first, then **Regression**, **Classification**, **Ensemble Learning** and **Unsupervised Learning** — each section ending with a full model-selection notebook that compares everything with cross-validation and hyperparameter tuning.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange) ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange) ![Pandas](https://img.shields.io/badge/Pandas-Data-150458)

Part of the **[ai-engineering-notes](https://github.com/AdnanCodex/ai-engineering-notes)** repository — one repo for the full AI engineering learning path.

## 🧹 1 · Data Preprocessing

Diabetes (classification) and Concrete (regression) datasets, cleaned step by step: missing values, outliers, skewness, encoding and scaling. The cleaned CSVs produced here are exactly what the Regression, Classification and Ensemble notebooks read.

| Notebook | What it covers | Open |
|---|---|---|
| Diabetes Data Preprocessing | Missing values, outliers, encoding & scaling — before/after CSVs included | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/1.%20Data_Preprocessing/For_Classification/Diabetes_Data_Preprocessing.ipynb) |
| Concrete Data Preprocessing | Full cleaning pipeline for the Concrete Strength dataset | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/1.%20Data_Preprocessing/For_Regression/Concrete_Data_Preprocessing.ipynb) |

## 📈 2 · Regression — Concrete Strength

Predicting concrete compressive strength. Every notebook reads `../1. Data_Preprocessing/For_Regression/concrete_after_preprocessing.csv`.

| Notebook | What it covers | Open |
|---|---|---|
| Linear, Polynomial, Lasso, Ridge & ElasticNet | Regularized linear models with tuning | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/2.%20Regression/1.%20Linear_Polynomial_Lesso_Ridge_ElasticNet.ipynb) |
| KNN Regression | Distance-based regression with scaling | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/2.%20Regression/2.%20KNN_Regression.ipynb) |
| Decision Tree Regression | Tree regression & pruning | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/2.%20Regression/3.%20DecisionTree_Regression.ipynb) |
| SVR Regression | Support Vector Regression with kernels | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/2.%20Regression/4.%20SVR_Regression.ipynb) |
| Best Regression Model Selection | All regressors compared: CV, tuning & leaderboard | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/2.%20Regression/Best_Regression_Model_Selection.ipynb) |

## 🎯 3 · Classification — Diabetes

Predicting diabetes outcomes. Every notebook reads `../1. Data_Preprocessing/For_Classification/diabetes_after_preprocessing.csv`.

| Notebook | What it covers | Open |
|---|---|---|
| Logistic Regression & Softmax | Binary + multinomial classification | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/3.%20Classification/1.%20Logistic_Softmax.ipynb) |
| KNN Classification | Neighbors, distance metrics & tuning | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/3.%20Classification/2.%20KNN_Classification.ipynb) |
| Naive Bayes Classification | Gaussian / Multinomial / Bernoulli NB | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/3.%20Classification/3.%20NaiveBayes_Classification.ipynb) |
| SVC Classification | SVM kernels & margin tuning | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/3.%20Classification/4.%20%20SVC_Classification.ipynb) |
| Decision Tree Classification | Splits, pruning & feature importance | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/3.%20Classification/5.%20Decision_Tree_Classification.ipynb) |
| Best Classification Model Selection | All classifiers compared: CV, tuning & leaderboard | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/3.%20Classification/Best_Classification_Model_Selection.ipynb) |

## 🧺 4 · Ensemble Learning — Concrete Strength

Bagging, Boosting, Voting and Stacking on the same preprocessed Concrete data.

| Notebook | What it covers | Open |
|---|---|---|
| Bagging | Bootstrap aggregating & Random Forest idea | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/4.%20Ensemble_Learning/1.%20Bagging.ipynb) |
| Boosting | AdaBoost / Gradient Boosting / XGBoost style workflows | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/4.%20Ensemble_Learning/2.%20Boosting.ipynb) |
| Voting | Hard & soft voting ensembles | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/4.%20Ensemble_Learning/3.%20Voting.ipynb) |
| Stacking | Meta-learner on base model predictions | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/4.%20Ensemble_Learning/4.%20Stacking.ipynb) |

## 🔍 5 · Unsupervised Learning — HR Dataset

Clustering an HR dataset. Run `01_HR_Data_Preprocessing.ipynb` first — it generates `hr_clean.csv`, `hr_preprocessed.csv` and `hr_truth.csv`, which the other notebooks in this folder read.

| Notebook | What it covers | Open |
|---|---|---|
| HR Data Preprocessing | Prepares the HR dataset; generates the cleaned CSVs used below | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/Unsupervised_Learning/01_HR_Data_Preprocessing.ipynb) |
| K-Means++ Clustering | Centroid clustering with smart seeding | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/Unsupervised_Learning/02_KMeansPlusPlus_Clustering.ipynb) |
| Hierarchical Clustering | Agglomerative clustering & dendrograms | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/Unsupervised_Learning/03_Hierarchical_Clustering.ipynb) |
| DBSCAN Clustering | Density-based clustering & noise handling | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/Unsupervised_Learning/04_DBSCAN_Clustering.ipynb) |
| OPTICS Clustering | Ordering-based density clustering | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/Unsupervised_Learning/05_OPTICS_Clustering.ipynb) |
| HDBSCAN Clustering | Hierarchical density-based clustering | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/Unsupervised_Learning/06_HDBSCAN_Clustering.ipynb) |
| Best Clustering Model Selection | Clustering methods compared with internal metrics | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdnanCodex/ai-engineering-notes/blob/main/02-machine-learning/Unsupervised_Learning/07_Best_Model_Selection.ipynb) |

## 📁 Structure

```
02-machine-learning/
├── 1. Data_Preprocessing/
│   ├── For_Classification/   # Diabetes: notebook + before/after CSVs
│   └── For_Regression/       # Concrete: notebook + before/after CSVs
├── 2. Regression/            # 5 notebooks — Concrete Strength
├── 3. Classification/        # 6 notebooks — Diabetes
├── 4. Ensemble_Learning/     # Bagging, Boosting, Voting, Stacking
└── Unsupervised_Learning/   # 7 notebooks + hr_raw_data.csv
```

## ⚡ How to run

1. Clone the repo and open any notebook — dataset paths are **repo-relative** (`../1. Data_Preprocessing/...`), so everything runs as-is, locally or in Colab via the badges above.
2. For Unsupervised Learning, run the preprocessing notebook (01) first so the intermediate HR CSVs are generated.
3. The Concrete preprocessing notebook expects the original `Concrete_Data.xls` upload (it was written for Colab); the already-cleaned CSVs are included, so the downstream notebooks work without it.

## 🧰 Tech Stack

Python · Pandas · NumPy · scikit-learn · Matplotlib · Seaborn · Jupyter / Google Colab

---

✨ Created by **Muhammad Adnan** — BS Artificial Intelligence, Hazara University
