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
  - [Foundation_For_ML](#foundation_for_ml)
  - [Ensemble Learning](#ensemble-learning)
  - [Model Tuning](#model-tuning)
  - [Deep Learning](#deep-learning)
  - [Dimensionality Reduction](#dimensionality-reduction)
  - [NLP ( ML approach )](#nlp-ml-approach)
  - [Supervised Learning](#supervised-learning)
  - [Unsupervised Learning](#unsupervised-learning)
- [Roadmap](#roadmap)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [License](#license)

## 📚 Overview

Notebook-first workspace for building strong ML foundations with short, focused lessons and runnable examples.

### Current Phase: Specialized ML Topics ✨

Current focus: **Deep learning, ensemble learning, model tuning, and supervised/unsupervised learning**.

## ✨ Features

- ✅ **57 notebooks** — 13 NumPy, 3 NumPy exercises, 10 Pandas, 2 Pandas exercises, 7 Data Viz, 6 Statistics, 3 Foundation projects, 3 Ensemble notebooks, 2 Model Tuning notebooks, 1 Deep Learning notebook, 2 Supervised notebooks, 2 Unsupervised notebooks, 1 Dimensionality Reduction, 2 NLP notebooks
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
- Move to Statistics with `Statistics/1_outliers.ipynb`.
- Continue with `Statistics/2_Ztest.ipynb`, `Statistics/3_Ttest.ipynb`, `Statistics/4_Two_sample_T_test.ipynb`, `Statistics/5_chi_square_test.ipynb`, and `Statistics/6_ANNOVA_test.ipynb`.
- Move to Foundation_For_ML with `Foundation_For_ML/1_foundation_project.ipynb`, `Foundation_For_ML/2_foundation_project.ipynb`, and `Foundation_For_ML/3_FORD_car_price_prediction.ipynb`.
- Continue with `Ensemble_Learning/bagging.ipynb`, `Ensemble_Learning/boosting.ipynb`, and `Ensemble_Learning/stacking.ipynb`.
- Continue with `Model_Tuning/cross_validation.ipynb` and `Model_Tuning/grid_search_cv.ipynb`.
- Move to `Supervised_Learning/1_Logistic_Regression.ipynb` and `Supervised_Learning/2_heart_disease_pred.ipynb`.
- Finish with `Unsupervised_Learning/k_means_clustering.ipynb` and `Unsupervised_Learning/DBSCAN.ipynb`.
- Explore Dimensionality Reduction with `Dimensionality_Reduction/pca_dimension.ipynb`.
- Try NLP notebooks in `NLP( ML approach )/bag_of_words.ipynb` and `NLP( ML approach )/emotion_prediction.ipynb`.
- Continue with `Deep_Learning/ANN/basic_neural_network.ipynb`.

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

- 6 notebooks in `Statistics/` covering outlier detection and handling, Z-test, T-test, Two-sample T-test, Chi-square test, and ANOVA test hypothesis testing.

### Foundation_For_ML

- 3 project notebooks in `Foundation_For_ML/` applying statistical and exploratory analysis to real-world datasets.

### Ensemble Learning

- 3 notebooks in `Ensemble_Learning/` covering bagging, boosting, and stacking.

### Model Tuning

- 2 notebooks in `Model_Tuning/` covering cross-validation and grid search.

### Deep Learning

- 1 notebook in `Deep_Learning/ANN/` covering a basic neural network for binary classification.

### Supervised Learning

- 2 notebooks in `Supervised_Learning/` covering logistic regression and heart-disease prediction.

### Dimensionality Reduction

- 1 notebook in `Dimensionality_Reduction/` covering PCA for dimensionality reduction.

### NLP ( ML approach )

- 2 notebooks in `NLP( ML approach )/` covering bag-of-words and an emotion-prediction example.

### Unsupervised Learning

- 2 notebooks in `Unsupervised_Learning/` covering k-means clustering and DBSCAN.

## 📁 Project Structure

```
Machine Learning/
|-- README.md                               # Project overview and guide
|-- requirements.txt                        # Python dependencies
|-- LICENSE                                 # License for reuse and distribution
|-- .gitignore                              # Git ignore patterns
|-- Data Visualization/                     # Data visualization modules
|   |-- matplotlib.ipynb                    # Matplotlib basics and plots
|   |-- Distributionplot.ipynb              # Distribution plots
|   |-- Categoricalplot.ipynb               # Categorical plots
|   |-- Matrixplot.ipynb                    # Matrix plots
|   |-- Regression.ipynb                    # Regression plots
|   |-- plotlyandcufflinks.ipynb            # Plotly and Cufflinks
|   |-- IPL_capstone_project.ipynb          # IPL capstone project
|   |-- IPL.csv                             # IPL dataset
|   |-- basic_plot.png                      # Sample plot image asset
|   `-- zoro.jpg                            # Image asset used in notebooks
|-- NumPy/                                  # NumPy fundamentals modules
|   |-- 1_numpy_arrays.ipynb                # Arrays basics
|   |-- 2_arrays_types.ipynb                # Data types (dtypes)
|   |-- 3_dimension_shapes.ipynb            # Dimensions & shapes
|   |-- 4_indexing_slicing_iteration.ipynb  # Advanced indexing
|   |-- 5_statistics.ipynb                  # Statistical operations
|   |-- 6_broadcasting_vectorize.ipynb      # Broadcasting & vectorization
|   |-- 7_boolean_arrays.ipynb              # Boolean indexing
|   |-- 8_linear_algebra.ipynb              # Linear algebra operations
|   |-- 9_size_of_objectsInMemory.ipynb     # Memory size exploration
|   |-- 10_useful_numpy_function.ipynb      # Useful NumPy utilities
|   |-- 11_numpy_operations.ipynb           # NumPy operations overview
|   |-- 12_Reshaping_inDepth.ipynb          # Reshaping deep dive
|   |-- 13_plotting_graphs_numpy.ipynb      # Plotting graphs with NumPy
|   `-- numpy_exercises/                    # Practice notebooks
|       |-- general_qns.ipynb               # Mixed practice questions
|       |-- nepali_cricket_score.ipynb      # Practice with real-world data
|       `-- valid_sudoku.ipynb              # NumPy practice exercise
|-- Pandas/                                 # Pandas fundamentals modules
|   |-- 1_series.ipynb                      # Series basics
|   |-- 2_DataFrames.ipynb                  # DataFrames basics
|   |-- 3_Missing_Data.ipynb                # Missing data handling
|   |-- 4_Merging_Joining_Concatination.ipynb # Merging and joining
|   |-- 5_GroupByAggregation.ipynb          # GroupBy and aggregation
|   |-- 6_pivot_tables.ipynb                # Pivot tables and reshaping
|   |-- 7_Operations.ipynb                  # Pandas operations
|   |-- 8_ipl_analysis.ipynb                # IPL data analysis
|   |-- 9_company.ipynb                     # Company data analysis
|   |-- 10_titanic.ipynb                    # Titanic survival analysis
|   |-- deliveries.csv                      # IPL deliveries dataset
|   |-- ipl_matches.csv                     # IPL matches dataset
|   |-- Fortune_500_Companies.csv           # Company dataset
|   |-- titanic_data.csv                    # Titanic passenger dataset
|   `-- pandas_exercise/                    # Pandas practice notebooks
|       |-- Countries.csv                   # Sample dataset
|       |-- Countries.ipynb                 # Country data practice
|       |-- feature_extraction.ipynb        # Feature extraction practice
|       `-- topanime.csv                    # Sample dataset
|-- Statistics/                             # Statistical methods modules
|   |-- 1_outliers.ipynb                    # Outlier detection and handling
|   |-- 2_Ztest.ipynb                       # Hypothesis testing: Z-test
|   |-- 3_Ttest.ipynb                       # Hypothesis testing: T-test
|   |-- 4_Two_sample_T_test.ipynb           # Hypothesis testing: Two-sample T-test
|   |-- 5_chi_square_test.ipynb             # Hypothesis testing: Chi-square test
|   `-- 6_ANNOVA_test.ipynb                 # Hypothesis testing: ANOVA test
|-- Foundation_For_ML/                      # Foundation ML projects
|   |-- 1_foundation_project.ipynb          # Foundation ML project 1
|   |-- 2_foundation_project.ipynb          # Foundation ML project 2
|   |-- 3_FORD_car_price_prediction.ipynb    # Ford car price prediction project
|   |-- ford.csv                             # Ford car dataset
|   |-- heart.csv                            # Heart disease dataset
|   `-- insurance.csv                        # Insurance dataset
|-- Ensemble_Learning/                      # Ensemble learning notebooks
|   |-- bagging.ipynb                       # Bagging ensemble notebook
|   |-- boosting.ipynb                      # Boosting ensemble notebook
|   `-- stacking.ipynb                      # Stacking ensemble notebook
|-- Model_Tuning/                           # Hyperparameter tuning notebooks
|   |-- cross_validation.ipynb              # Cross-validation notebook
|   `-- grid_search_cv.ipynb                # Grid-search CV notebook
|-- Deep_Learning/                          # Deep learning notebooks
|   |-- ANN/                                # Artificial neural networks
|   |   `-- basic_neural_network.ipynb      # Basic neural network example
|   `-- CNN/                                # Convolutional neural network section
|-- Supervised_Learning/                    # Supervised learning notebooks
|   |-- 1_Logistic_Regression.ipynb         # Logistic regression notebook
|   |-- 2_heart_disease_pred.ipynb          # Heart-disease prediction notebook
|   |-- app.py                              # Streamlit app for the prediction workflow
|   |-- columns.pkl                         # Model feature columns
|   |-- heart.csv                           # Heart disease dataset
|   |-- scaler.pkl                          # Saved scaler object
|   `-- SVM_heart_model.pkl                 # Saved SVM model
|-- Dimensionality_Reduction/               # Dimensionality reduction modules
|   `-- pca_dimension.ipynb                 # PCA dimensionality reduction
|-- NLP( ML approach )/                     # Natural Language Processing notebooks
|   |-- bag_of_words.ipynb                  # Bag-of-words example
|   `-- emotion_prediction.ipynb            # Emotion prediction example
`-- Unsupervised_Learning/                  # Unsupervised learning notebooks
    |-- k_means_clustering.ipynb            # K-means clustering notebook
    `-- DBSCAN.ipynb                        # DBSCAN clustering notebook
```

## 🗺️ Roadmap

### Current Phase ✅

- [x] NumPy fundamentals (13 modules)
- [x] NumPy exercises (3 notebooks)
- [x] Pandas fundamentals (10 notebooks)
- [x] Pandas exercises (2 notebooks)
- [x] Data visualization (7 notebooks)
- [x] Statistical methods (6 notebooks)
- [x] Foundation For ML (3 notebooks)
- [x] Ensemble Learning (3 notebooks)
- [x] Model Tuning (2 notebooks)

### Upcoming Phases 🚧

- [/] **Supervised Learning** — Logistic regression and classification workflows _(2 notebooks)_
- [/] **Unsupervised Learning** — K-means clustering and DBSCAN _(2 notebooks)_
- [/] **Deep Learning** — Neural network basics with TensorFlow/Keras _(1 notebook)_
- [ ] **Mini-Projects** — End-to-end projects combining all skills
- [ ] **Advanced Deep Learning** — Introduction to TensorFlow/PyTorch

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

_Last Updated: August 2026_
