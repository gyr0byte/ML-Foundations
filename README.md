# 🚀 Machine Learning Fundamentals

> A comprehensive, hands-on learning repository documenting the journey from Python and NumPy fundamentals to practical machine learning implementation.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![NumPy](https://img.shields.io/badge/NumPy-Latest-blueviolet?logo=numpy)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites & Setup](#prerequisites--setup)
- [Getting Started](#getting-started)
- [Learning Modules](#learning-modules)
  - [NumPy Fundamentals](#numpy-fundamentals)
  - [Pandas Fundamentals](#pandas-fundamentals)
- [Roadmap](#roadmap)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [License](#license)

## 📚 Overview

This repository is a **notebook-first learning workspace** designed to build strong foundations in machine learning from the ground up. Each notebook focuses on a specific concept with clear explanations, practical code examples, and executable outputs that demonstrate learning progression.

### Current Phase: NumPy Fundamentals ✨

The current focus is mastering **NumPy** — the foundational library for numerical computing in Python and the backbone of all machine learning workflows.

## ✨ Features

- ✅ **23 Notebooks Total** — 13 NumPy, 3 exercises, 7 Pandas
- ✅ **Notebook-First Approach** — Interactive learning with live code execution
- ✅ **Progressive Difficulty** — Each module builds on previous concepts
- ✅ **Practical Examples** — Real-world use cases and applications
- ✅ **Clear Documentation** — Well-commented code and detailed explanations
- ✅ **Reproducible Environment** — Exact dependencies and setup instructions

## 📁 Project Structure

```
Machine Learning/
├── README.md                      # Project overview and guide
├── requirements.txt               # Python dependencies
├── LICENSE                        # License for reuse and distribution
├── .gitignore                     # Git ignore patterns
├── NumPy/                         # NumPy fundamentals modules
    ├── 1_numpy_arrays.ipynb               # Arrays basics
    ├── 2_arrays_types.ipynb               # Data types (dtypes)
    ├── 3_dimension_shapes.ipynb           # Dimensions & shapes
    ├── 4_indexing_slicing_iteration.ipynb # Advanced indexing
    ├── 5_statistics.ipynb                 # Statistical operations
    ├── 6_broadcasting_vectorize.ipynb     # Broadcasting & vectorization
    ├── 7_boolean_arrays.ipynb             # Boolean indexing
    ├── 8_linear_algebra.ipynb             # Linear algebra operations
    ├── 9_size_of_objectsInMemory.ipynb    # Memory size exploration
   ├── 10_useful_numpy_function.ipynb     # Useful NumPy utilities
   ├── 11_numpy_operations.ipynb          # NumPy operations overview
   ├── 12_Reshaping_inDepth.ipynb         # Reshaping deep dive
   ├── 13_plotting_graphs_numpy.ipynb     # Plotting graphs with NumPy
   └── numpy_exercises/                   # Practice notebooks
      ├── general_qns.ipynb              # Mixed practice questions
      ├── nepali_cricket_score.ipynb     # Practice with real-world data
      └── valid_sudoku.ipynb             # NumPy practice exercise
└── Pandas/                        # Pandas fundamentals modules
    ├── 1_series.ipynb                     # Series basics
    ├── 2_DataFrames.ipynb                 # DataFrames basics
    ├── 3_Missing_Data.ipynb               # Missing data handling
    ├── 4_Merging_Joining_Concatination.ipynb # Merging and joining
    ├── 5_GroupByAggregation.ipynb         # GroupBy and aggregation
   ├── 6_pivot_tables.ipynb               # Pivot tables and reshaping
   └── 7_Operations.ipynb                 # Pandas operations
```

## 🔧 Prerequisites & Setup

### Requirements

- **Python 3.8 or higher**
- **pip** (Python package manager)
- **Jupyter Notebook** or **JupyterLab**

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/machine-learning.git
   cd "Machine Learning"
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**

   ```bash
   jupyter notebook
   ```

   Then navigate to the `NumPy/` folder and open any notebook.

## 🎯 Getting Started

1. Start with `NumPy/1_numpy_arrays.ipynb`.
2. Continue sequentially through `NumPy/13_plotting_graphs_numpy.ipynb`.
3. Begin Pandas with `Pandas/1_series.ipynb`.
4. Continue with `Pandas/2_DataFrames.ipynb`.
5. Continue with `Pandas/3_Missing_Data.ipynb`.
6. Continue with `Pandas/4_Merging_Joining_Concatination.ipynb`.
7. Continue with `Pandas/5_GroupByAggregation.ipynb`.
8. Continue with `Pandas/6_pivot_tables.ipynb`.
9. Continue with `Pandas/7_Operations.ipynb`.
10. Run cells top-to-bottom and experiment with the examples.

## 📖 Learning Modules

### NumPy Fundamentals

#### Module 1: NumPy Arrays Basics

**File:** `NumPy/1_numpy_arrays.ipynb`

Create arrays, inspect shapes, and compare arrays to Python lists.

#### Module 2: Array Data Types (dtypes)

**File:** `NumPy/2_arrays_types.ipynb`

Explore dtypes, casting, and how types affect memory and precision.

#### Module 3: Dimensions and Shapes

**File:** `NumPy/3_dimension_shapes.ipynb`

Understand dimensionality, shapes, and the structure of N-D arrays.

#### Module 4: Indexing and Slicing

**File:** `NumPy/4_indexing_slicing_iteration.ipynb`

Select, slice, and iterate through arrays efficiently.

#### Module 5: Statistics and Aggregation

**File:** `NumPy/5_statistics.ipynb`

Compute common statistics and summarize arrays quickly.

#### Module 6: Broadcasting and Vectorization

**File:** `NumPy/6_broadcasting_vectorize.ipynb`

Use broadcasting rules and vectorized ops to avoid loops.

#### Module 7: Boolean Arrays and Conditional Operations

**File:** `NumPy/7_boolean_arrays.ipynb`

Filter arrays with boolean masks and combine conditions.

#### Module 8: Linear Algebra

**File:** `NumPy/8_linear_algebra.ipynb`

Work with dot products, matrices, and core linear algebra tools.

#### Module 9: Size of Objects in Memory

**File:** `NumPy/9_size_of_objectsInMemory.ipynb`

Estimate memory usage and compare array storage costs.

#### Module 10: Useful NumPy Functions

**File:** `NumPy/10_useful_numpy_function.ipynb`

Practice handy utilities for building and inspecting arrays.

#### Module 11: NumPy Operations

**File:** `NumPy/11_numpy_operations.ipynb`

Apply core element-wise, reduction, and shape operations.

#### Module 12: Reshaping In Depth

**File:** `NumPy/12_Reshaping_inDepth.ipynb`

Reshape, ravel, and reorder arrays for real workflows.

#### Module 13: Plotting Graphs with NumPy

**File:** `NumPy/13_plotting_graphs_numpy.ipynb`

Quick visualizations and plotting practice using NumPy-generated data.

### NumPy Exercises

#### Exercise 1: Valid Sudoku

**File:** `NumPy/numpy_exercises/valid_sudoku.ipynb`

Practice NumPy logic and indexing with a classic Sudoku validation task.

#### Exercise 2: General Questions

**File:** `NumPy/numpy_exercises/general_qns.ipynb`

Mixed practice questions to reinforce core NumPy concepts.

#### Exercise 3: Nepali Cricket Score

**File:** `NumPy/numpy_exercises/nepali_cricket_score.ipynb`

Practice data manipulation on a cricket score dataset.

### Pandas Fundamentals

#### Module 1: Series Basics

**File:** `Pandas/1_series.ipynb`

Create, index, and manipulate pandas Series.

#### Module 2: DataFrames Basics

**File:** `Pandas/2_DataFrames.ipynb`

Build and manipulate DataFrames with columns and indexes.

#### Module 3: Missing Data

**File:** `Pandas/3_Missing_Data.ipynb`

Detect, clean, and fill missing values in datasets.

#### Module 4: Merging, Joining, and Concatenation

**File:** `Pandas/4_Merging_Joining_Concatination.ipynb`

Combine datasets with merge, join, and concat patterns.

#### Module 5: GroupBy and Aggregation

**File:** `Pandas/5_GroupByAggregation.ipynb`

Summarize and aggregate data with GroupBy workflows.

#### Module 6: Pivot Tables

**File:** `Pandas/6_pivot_tables.ipynb`

Create and manipulate pivot tables for data reshaping.

#### Module 7: Operations

**File:** `Pandas/7_Operations.ipynb`

Apply common Pandas operations for data transformation.

#### Module 6: Pivot Tables

**File:** `Pandas/6_pivot_tables.ipynb`

Create and manipulate pivot tables for data reshaping.

## 🗺️ Roadmap

### Current Phase ✅

- [x] NumPy fundamentals (13 modules)
- [x] NumPy exercises (3 notebooks)
- [x] Pandas fundamentals (7 notebooks)

### Upcoming Phases 🚧

- [ ] **Pandas Essentials** — Data manipulation, cleaning, and analysis
- [ ] **Data Visualization** — Matplotlib and Seaborn for visual exploration
- [ ] **Statistical Methods** — Hypothesis testing, distributions, and inference
- [ ] **Supervised Learning** — Regression and classification with Scikit-Learn
- [ ] **Unsupervised Learning** — Clustering and dimensionality reduction
- [ ] **Mini-Projects** — End-to-end projects combining all skills
- [ ] **Deep Learning** — Introduction to TensorFlow/PyTorch

## 🏆 Best Practices

- Follow PEP 8 conventions
- Use descriptive variable names
- Keep cells focused and concise
- Include markdown explanations
- Pin dependencies in `requirements.txt`

## 🤝 Contributing

Suggestions and improvements are welcome.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

**Happy Learning! 🎓**

_Last Updated: May 2026_
