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
- [Learning Modules](#learning-modules)
  - [NumPy Fundamentals](#numpy-fundamentals)
  - [Pandas Fundamentals](#pandas-fundamentals)
  - [Pandas Exercises](#pandas-exercises)
  - [Data Visualization](#data-visualization)
  - [Statistics](#statistics)
- [Roadmap](#roadmap)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [License](#license)

## 📚 Overview

Notebook-first workspace for building strong ML foundations with short, focused lessons and runnable examples.

### Current Phase: Statistical Methods ✨

Current focus: **Statistics** for hypothesis testing, distributions, and inference.

## ✨ Features

- ✅ **36 notebooks** — 13 NumPy, 3 exercises, 10 Pandas, 2 Pandas exercises, 7 data viz, 1 statistics
- ✅ **Hands-on** — notebook-first, progressive difficulty
- ✅ **Reproducible** — pinned dependencies and setup steps

## 🔧 Prerequisites & Setup

### Requirements

- **Python 3.8+**, **pip**, and **Jupyter Notebook/Lab**

### Installation

1. **Clone**

   ```bash
   git clone https://github.com/gyr0byte/ML-Foundations.git "Machine Learning"
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

4. **Launch Jupyter**

   ```bash
   jupyter notebook
   ```

### Getting Started

- Start at `NumPy/1_numpy_arrays.ipynb`, finish NumPy, then move to Pandas.
- Run cells top-to-bottom and experiment with the examples.
- Move to Data Visualization with `Data Visualization/matplotlib.ipynb`.
- Continue with `Data Visualization/Distributionplot.ipynb`.
- Continue with `Data Visualization/Categoricalplot.ipynb`.
- Continue with `Data Visualization/Matrixplot.ipynb`.
- Continue with `Data Visualization/Regression.ipynb`.
- Continue with `Data Visualization/plotlyandcufflinks.ipynb`.
- Continue with `Data Visualization/IPL_capstone_project.ipynb`.

## 📖 Learning Modules

### NumPy Fundamentals

- 13 core notebooks + 3 exercises in `NumPy/`.

### Pandas Fundamentals

- 10 core notebooks in `Pandas/`, including IPL analysis, company data, and Titanic survival analysis.

### Pandas Exercises

- 2 practice notebooks in `Pandas/pandas_exercise/`.

### Data Visualization

- 7 notebooks in `Data Visualization/` covering Matplotlib basics, distribution plots, categorical plots, matrix plots, regression plots, Plotly/Cufflinks, and an IPL capstone.
- Assets: `Data Visualization/basic_plot.png`, `Data Visualization/zoro.jpg`.

### Statistics

- 1 notebook in `Statistics/` covering outlier detection and handling.

## 📁 Project Structure

```
Machine Learning/
|-- README.md                      # Project overview and guide
|-- requirements.txt               # Python dependencies
|-- LICENSE                        # License for reuse and distribution
|-- .gitignore                     # Git ignore patterns
|-- Data Visualization/            # Data visualization modules
|   |-- matplotlib.ipynb                # Matplotlib basics and plots
|   |-- Distributionplot.ipynb          # Distribution plots
|   |-- Categoricalplot.ipynb            # Categorical plots
|   |-- Matrixplot.ipynb                 # Matrix plots
|   |-- Regression.ipynb                 # Regression plots
|   |-- plotlyandcufflinks.ipynb         # Plotly and Cufflinks
|   |-- IPL_capstone_project.ipynb       # IPL capstone project
|   |-- IPL.csv                          # IPL dataset
|   |-- basic_plot.png                   # Sample plot image asset
|   `-- zoro.jpg                         # Image asset used in notebooks
|-- NumPy/                         # NumPy fundamentals modules
|   |-- 1_numpy_arrays.ipynb               # Arrays basics
|   |-- 2_arrays_types.ipynb               # Data types (dtypes)
|   |-- 3_dimension_shapes.ipynb           # Dimensions & shapes
|   |-- 4_indexing_slicing_iteration.ipynb # Advanced indexing
|   |-- 5_statistics.ipynb                 # Statistical operations
|   |-- 6_broadcasting_vectorize.ipynb     # Broadcasting & vectorization
|   |-- 7_boolean_arrays.ipynb             # Boolean indexing
|   |-- 8_linear_algebra.ipynb             # Linear algebra operations
|   |-- 9_size_of_objectsInMemory.ipynb    # Memory size exploration
|   |-- 10_useful_numpy_function.ipynb     # Useful NumPy utilities
|   |-- 11_numpy_operations.ipynb          # NumPy operations overview
|   |-- 12_Reshaping_inDepth.ipynb         # Reshaping deep dive
|   |-- 13_plotting_graphs_numpy.ipynb     # Plotting graphs with NumPy
|   `-- numpy_exercises/                   # Practice notebooks
|       |-- general_qns.ipynb              # Mixed practice questions
|       |-- nepali_cricket_score.ipynb     # Practice with real-world data
|       `-- valid_sudoku.ipynb             # NumPy practice exercise
|-- Pandas/                        # Pandas fundamentals modules
|   |-- 1_series.ipynb                     # Series basics
|   |-- 2_DataFrames.ipynb                 # DataFrames basics
|   |-- 3_Missing_Data.ipynb               # Missing data handling
|   |-- 4_Merging_Joining_Concatination.ipynb # Merging and joining
|   |-- 5_GroupByAggregation.ipynb         # GroupBy and aggregation
|   |-- 6_pivot_tables.ipynb               # Pivot tables and reshaping
|   |-- 7_Operations.ipynb                 # Pandas operations
|   |-- 8_ipl_analysis.ipynb               # IPL data analysis
|   |-- 9_company.ipynb                    # Company data analysis
|   |-- 10_titanic.ipynb                   # Titanic survival analysis
|   |-- deliveries.csv                     # IPL deliveries dataset
|   |-- ipl_matches.csv                    # IPL matches dataset
|   |-- Fortune_500_Companies.csv          # Company dataset
|   |-- titanic_data.csv                   # Titanic passenger dataset
|   `-- pandas_exercise/                   # Pandas practice notebooks
|      |-- Countries.csv                  # Sample dataset
|      |-- Countries.ipynb                # Country data practice
|      |-- feature_extraction.ipynb       # Feature extraction practice
|      `-- topanime.csv                   # Sample dataset
`-- Statistics/                    # Statistical methods modules
   `-- outliers.ipynb                    # Outlier detection and handling
```

## 🗺️ Roadmap

### Current Phase ✅

- [x] NumPy fundamentals (13 modules)
- [x] NumPy exercises (3 notebooks)
- [x] Pandas fundamentals (10 notebooks)
- [x] Pandas exercises (2 notebooks)
- [x] Data visualization (7 notebooks)

### Upcoming Phases 🚧

- [/] **Statistical Methods** — Hypothesis testing, distributions, and inference *(1 notebook started)*
- [ ] **Supervised Learning** — Regression and classification with Scikit-Learn
- [ ] **Unsupervised Learning** — Clustering and dimensionality reduction
- [ ] **Mini-Projects** — End-to-end projects combining all skills
- [ ] **Deep Learning** — Introduction to TensorFlow/PyTorch

## 🏆 Best Practices

- Follow PEP 8 and use descriptive names
- Keep cells focused with short markdown context
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

_Last Updated: June 2026_
