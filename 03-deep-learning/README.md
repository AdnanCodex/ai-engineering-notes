<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1026,50:7A1E1E,100:EE4C2C&height=180&section=header&text=Deep%20Learning%20with%20PyTorch&fontSize=40&fontColor=F5C542&animation=fadeIn&fontAlignY=38&desc=Practical%20Deep%20Learning%20%E2%80%94%20ANN%20%C2%B7%20CNN%20%C2%B7%20RNN%20%C2%B7%20LSTM%20%C2%B7%20Transfer%20Learning%20%C2%B7%20Optuna&descAlignY=58&descSize=14" alt="Deep Learning with PyTorch banner"/>

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

**Part of [AI Engineering Notes](https://github.com/AdnanCodex/ai-engineering-notes) · Section 03 — Deep Learning**

</div>

---

## 📖 About

A complete, practical **Deep Learning** series in **PyTorch** — **16 notebooks and 2 datasets**, organised into 5 topics in the exact order to learn them: PyTorch fundamentals first, then ANN, CNN, Transfer Learning, and finally RNN & LSTM projects.

> 🙏 **Credit:** These notes follow the free **CampusX** Deep Learning course (Practical Deep Learning using PyTorch). The notebooks are collected, organised, formatted and maintained here as personal learning notes by **Muhammad Adnan**.

---

## 🗺️ Learning Roadmap

```text
PyTorch Fundamentals → Dataset & DataLoader → ANN (Fashion-MNIST)
        ↓
CNN & Transfer Learning → RNN (Q&A System) → LSTM (Next Word Predictor)
```

---

## 📚 Contents

### 01 · PyTorch Fundamentals — [`01-pytorch-fundamentals/`](01-pytorch-fundamentals/)

| # | Notebook | What It Covers |
|---|------------------|----------------|
| 1 | [Tensors in PyTorch](01-pytorch-fundamentals/01_tensors_in_pytorch.ipynb) | Creating tensors, indexing, reshaping, operations |
| 2 | [PyTorch Autograd](01-pytorch-fundamentals/02_pytorch_autograd.ipynb) | Computational graphs, gradients, `backward()` |
| 3 | [PyTorch Training Pipeline](01-pytorch-fundamentals/03_pytorch_training_pipeline.ipynb) | The full loop — forward, loss, backward, optimiser step |
| 4 | [PyTorch NN Module](01-pytorch-fundamentals/04_pytorch_nn_module.ipynb) | Building models with `nn.Module` |
| 5 | [Training Pipeline with NN Module](01-pytorch-fundamentals/05_training_pipeline_with_nn_module.ipynb) | End-to-end classification pipeline using `nn.Module` |

### 02 · Dataset & DataLoader — [`02-dataset-and-dataloader/`](02-dataset-and-dataloader/)

| # | Notebook | What It Covers |
|---|------------------|----------------|
| 1 | [Dataset & DataLoader — Demo](02-dataset-and-dataloader/01_dataset_and_dataloader_demo.ipynb) | Custom `Dataset` class, batching with `DataLoader` |
| 2 | [Training Pipeline with Dataset & DataLoader](02-dataset-and-dataloader/02_training_pipeline_with_dataset_and_dataloader.ipynb) | Full pipeline using Dataset & DataLoader |

### 03 · ANN — Fashion-MNIST — [`03-ann-fashion-mnist/`](03-ann-fashion-mnist/)

| # | Notebook | What It Covers |
|---|----------|----------------|
| 1 | [Building an ANN — Fashion-MNIST](03-ann-fashion-mnist/01_ann_fashion_mnist.ipynb) | First complete neural network on Fashion-MNIST |
| 2 | [ANN Training on GPU](03-ann-fashion-mnist/02_ann_training_on_gpu.ipynb) | Moving model and data to GPU |
| 3 | [Optimizing the Neural Network](03-ann-fashion-mnist/03_ann_gpu_optimized.ipynb) | Better architecture, training tricks, higher accuracy |
| 4 | [Hyperparameter Tuning with Optuna](03-ann-fashion-mnist/04_ann_hyperparameter_tuning_optuna.ipynb) | Automated hyperparameter search with Optuna |

### 04 · CNN & Transfer Learning — [`04-cnn-and-transfer-learning/`](04-cnn-and-transfer-learning/)

| # | Notebook | What It Covers |
|---|----------|----------------|
| 1 | [Building a CNN — Fashion-MNIST](04-cnn-and-transfer-learning/01_cnn_fashion_mnist.ipynb) | Convolution, pooling and a complete CNN classifier |
| 2 | [Transfer Learning — Fashion-MNIST](04-cnn-and-transfer-learning/02_transfer_learning_fashion_mnist.ipynb) | Fine-tuning a pre-trained model |
| 3 | [CNN with Optuna](04-cnn-and-transfer-learning/03_cnn_with_optuna.ipynb) | Hyperparameter tuning for the CNN |

### 05 · RNN & LSTM — [`05-rnn-and-lstm/`](05-rnn-and-lstm/)

| # | Notebook | What It Covers |
|---|----------|----------------|
| 1 | [RNN Question Answering System](05-rnn-and-lstm/01_rnn_question_answering_system.ipynb) | A working Q&A system built with an RNN |
| 2 | [LSTM Next Word Predictor](05-rnn-and-lstm/02_lstm_next_word_predictor.ipynb) | Language modelling — predicting the next word with LSTM |

---

## 🚀 Quick Start

```bash
# 1 — Clone the full notes repository
git clone https://github.com/AdnanCodex/ai-engineering-notes.git
cd ai-engineering-notes/03-deep-learning

# 2 — Install dependencies
pip install -r requirements.txt

# 3 — Open any notebook
jupyter lab
```

> 💡 The ANN and CNN notebooks run much faster on a GPU. On a CPU-only laptop they still run — the code checks `torch.cuda.is_available()` and falls back to CPU automatically.

---

## 📂 Structure

```text
03-deep-learning/
├── 01-pytorch-fundamentals/     # Tensors, Autograd, Training Pipeline, NN Module
├── 02-dataset-and-dataloader/   # Dataset & DataLoader + training pipeline
├── 03-ann-fashion-mnist/        # ANN → GPU → Optimization → Optuna tuning
├── 04-cnn-and-transfer-learning/# CNN, Transfer Learning, CNN + Optuna
├── 05-rnn-and-lstm/             # RNN Q&A system, LSTM next-word predictor
├── data/                        # fmnist_small.csv (6,000 rows), 100_Unique_QA_Dataset.csv
├── requirements.txt
└── README.md
```

## 🗃️ Datasets

| Dataset | Used By | Notes |
|---------|---------|-------|
| [`data/fmnist_small.csv`](data/fmnist_small.csv) | ANN, CNN, Transfer Learning notebooks | 6,000-row subset of Fashion-MNIST in CSV form (`label` + 784 pixel columns) |
| [`data/100_Unique_QA_Dataset.csv`](data/100_Unique_QA_Dataset.csv) | RNN Q&A notebook | 100 question–answer pairs |

> 🔧 **Modernisation note:** The notebooks were reviewed and updated to current PyTorch practice — Colab-only dataset paths (`/content/...`) changed to repo-relative `../data/...` paths, standardised notebook headers, `torch.manual_seed(42)` reproducibility setup in every training notebook, `model.train()` / `model.eval()` added where they were missing, and `optimizer.zero_grad(set_to_none=True)` (the PyTorch 2.x recommended form). Model architectures and training logic were not changed.

---

## ⚠️ Notes

- 🎓 Full credit for the lectures and original course material goes to **CampusX**.
- 🔁 The Breast Cancer notebooks (Training Pipeline topics) load their dataset from a public URL given in the course; an internet connection is needed for those cells.
- 💻 GPU notebooks automatically fall back to CPU — they run on any laptop, just slower.

---

<div align="center">

**Muhammad Adnan** — Aspiring AI Engineer · BS Artificial Intelligence, Hazara University

[![GitHub](https://img.shields.io/badge/GitHub-AdnanCodex-181717?style=for-the-badge&logo=github)](https://github.com/AdnanCodex)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-adnan--ai-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/adnan-ai)

*More sections: [Python for Data Science](https://github.com/AdnanCodex/ai-engineering-notes/tree/main/01-python-for-datascience) · [Machine Learning](https://github.com/AdnanCodex/ai-engineering-notes/tree/main/02-machine-learning) · [Generative AI](https://github.com/AdnanCodex/ai-engineering-notes/tree/main/04-generative-ai) · [FastAPI](https://github.com/AdnanCodex/ai-engineering-notes/tree/main/05-fastapi) · [Streamlit](https://github.com/AdnanCodex/ai-engineering-notes/tree/main/06-streamlit)*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1026,50:7A1E1E,100:EE4C2C&height=90&section=footer" alt=""/>

</div>
