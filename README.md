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
- [Roadmap](#roadmap)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [Resources](#resources)
- [License](#license)

## 📚 Overview

This repository is a **notebook-first learning workspace** designed to build strong foundations in machine learning from the ground up. Each notebook focuses on a specific concept with clear explanations, practical code examples, and executable outputs that demonstrate learning progression.

### Current Phase: NumPy Fundamentals ✨

The current focus is mastering **NumPy** — the foundational library for numerical computing in Python and the backbone of all machine learning workflows.

## ✨ Features

- ✅ **8 Comprehensive NumPy Notebooks** — Progressive learning from basics to advanced topics
- ✅ **Notebook-First Approach** — Interactive learning with live code execution
- ✅ **Progressive Difficulty** — Each module builds on previous concepts
- ✅ **Practical Examples** — Real-world use cases and applications
- ✅ **Clear Documentation** — Well-commented code and detailed explanations
- ✅ **Reproducible Environment** — Exact dependencies and setup instructions

## 📁 Project Structure

```
Machine Learning/
├── README.md                      # Project overview and guide
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore patterns
└── NumPy/                        # NumPy fundamentals modules
    ├── 1numpy_arrays.ipynb              # Arrays basics
    ├── 2arrays_types.ipynb              # Data types (dtypes)
    ├── 3dimension_shapes.ipynb          # Dimensions & shapes
    ├── 4indexing_and_slicing.ipynb      # Advanced indexing
    ├── 5statistics.ipynb                # Statistical operations
    ├── 6broadcasting_vectorize.ipynb    # Broadcasting & vectorization
    ├── 7boolean_arrays.ipynb            # Boolean indexing
    └── 8linear_algebra.ipynb            # Linear algebra operations
```

## 🔧 Prerequisites & Setup

### Requirements

- **Python 3.8 or higher**
- **pip** (Python package manager)
- **Jupyter Notebook** or **JupyterLab**
- **NumPy** (primary library)

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

### Dependencies

Core libraries used in this project:

- **NumPy** — Numerical computing
- **Jupyter** — Interactive notebooks
- **Matplotlib** — Data visualization (upcoming)
- **Pandas** — Data manipulation (upcoming)
- **Seaborn** — Advance Visualization (upcoming)

See `requirements.txt` for the complete list of pinned versions.

## 🎯 Getting Started

### Step 1: Set Up Your Environment

Follow the installation steps above. Ensure your Python environment is activated.

### Step 2: Start with the Basics

Begin with **`NumPy/1numpy_arrays.ipynb`** for an introduction to NumPy arrays and foundational concepts.

### Step 3: Progress Sequentially

Work through the notebooks in order (1 → 8). Each module builds on previous concepts:

```
Arrays → Types → Dimensions → Indexing → Statistics → Broadcasting → Boolean → Linear Algebra
```

### Step 4: Hands-On Learning

Modify and experiment with the code examples. Understanding comes from doing!

## 📖 Learning Modules

### NumPy Fundamentals

Master the NumPy library — the cornerstone of Python's scientific computing ecosystem.

#### Module 1: NumPy Arrays Basics

**File:** `NumPy/1numpy_arrays.ipynb`

Learn how to create and work with NumPy arrays, the fundamental data structure.

**Topics:**

- NumPy import and setup
- Creating arrays with `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`
- Basic array properties (shape, size, dtype)
- Simple indexing and element access
- Understanding array vs list differences

---

#### Module 2: Array Data Types (dtypes)

**File:** `NumPy/2arrays_types.ipynb`

Understand data types and how they affect memory usage and computation.

**Topics:**

- Integer and floating-point data types
- Mixed-type arrays and automatic type promotion
- Inspecting and specifying `dtype` explicitly
- Type casting and conversions
- Why data types matter for performance and memory efficiency

---

#### Module 3: Dimensions and Shapes

**File:** `NumPy/3dimension_shapes.ipynb`

Master 1D, 2D, and multi-dimensional arrays.

**Topics:**

- 1D vs 2D vs N-dimensional arrays
- Understanding `.shape` and `.ndim` attributes
- Row-major (C-style) vs column-major (Fortran-style) ordering
- Reshaping and transposing arrays
- Building mental models for multi-dimensional data

---

#### Module 4: Indexing and Slicing

**File:** `NumPy/4indexing_and_slicing.ipynb`

Advanced techniques for accessing and selecting array elements.

**Topics:**

- Basic indexing for 1D, 2D, and N-D arrays
- Slicing with step values and negative indices
- Fancy indexing with integer arrays
- Boolean masking and conditional selection
- Copy vs view operations

---

#### Module 5: Statistics and Aggregation

**File:** `NumPy/5statistics.ipynb`

Perform statistical calculations on arrays.

**Topics:**

- Computing mean, median, standard deviation, variance
- Sum, product, and cumulative operations
- Min and max operations with `argmin()` and `argmax()`
- Percentiles and quantiles
- Working with NaN and infinite values

---

#### Module 6: Broadcasting and Vectorization

**File:** `NumPy/6broadcasting_vectorize.ipynb`

Harness NumPy's power through broadcasting and vectorized operations.

**Topics:**

- Broadcasting rules and implicit array expansion
- Element-wise operations across differently-shaped arrays
- Avoiding loops with vectorized functions
- Universal functions (ufuncs) and their benefits
- Performance implications of vectorization

---

#### Module 7: Boolean Arrays and Conditional Operations

**File:** `NumPy/7boolean_arrays.ipynb`

Use boolean indexing for powerful data filtering.

**Topics:**

- Creating boolean arrays through comparisons
- Boolean indexing and masking
- Logical operations (AND, OR, NOT)
- Combining multiple conditions
- Filtering and selecting subsets of data

---

#### Module 8: Linear Algebra

**File:** `NumPy/8linear_algebra.ipynb`

Essential linear algebra operations for machine learning.

**Topics:**

- Matrix multiplication and dot products
- Eigenvalues and eigenvectors
- Matrix decomposition (SVD, QR)
- Solving linear systems
- Norms and distance calculations

---

## 🗺️ Roadmap

### Current Phase ✅

- [x] NumPy fundamentals (8 modules)

### Upcoming Phases 🚧

- [ ] **Pandas Essentials** — Data manipulation, cleaning, and analysis
- [ ] **Data Visualization** — Matplotlib and Seaborn for visual exploration
- [ ] **Statistical Methods** — Hypothesis testing, distributions, and inference
- [ ] **Supervised Learning** — Regression and classification with Scikit-Learn
- [ ] **Unsupervised Learning** — Clustering and dimensionality reduction
- [ ] **Mini-Projects** — End-to-end projects combining all skills
- [ ] **Deep Learning** — Introduction to TensorFlow/PyTorch

## 🏆 Best Practices

### Code Style

- Follow PEP 8 conventions
- Use descriptive variable names
- Add comments for clarity and learning

### Notebook Practices

- Keep cells focused and concise
- Include markdown cells with explanations
- Use meaningful output displays
- Document assumptions and edge cases

### Reproducibility

- Pin dependency versions in `requirements.txt`
- Include random seed settings where applicable
- Provide clear setup instructions
- Test notebooks regularly

## 🤝 Contributing

This is a personal learning repository, but suggestions and improvements are welcome!

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

### Types of Contributions

- 🐛 Bug fixes and error corrections
- 📝 Enhanced documentation and explanations
- 💡 Additional examples and use cases
- 🎨 Visual improvements and visualizations
- 📊 New topics or modules

## 📚 Resources

### Official Documentation

- [NumPy Documentation](https://numpy.org/doc/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/index.html)
- [Jupyter Documentation](https://jupyter.org/documentation)

### Learning Resources

- [NumPy Tutorial by W3Schools](https://www.w3schools.com/python/numpy/default.asp)
- [DataCamp NumPy Courses](https://www.datacamp.com/)
- [Real Python NumPy Guides](https://realpython.com/numpy-tutorial/)
- [3Blue1Brown Linear Algebra](https://www.3blue1brown.com/series/essence-of-linear-algebra)

### Recommended Books

- "Python for Data Analysis" by Wes McKinney
- "Hands-On Machine Learning" by Aurélien Géron
- "Introduction to Statistical Learning" by James, Witten, et al.

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

## 🙋 Questions & Support

Have questions or found an issue? Feel free to:

- Open an issue on GitHub
- Check existing documentation
- Review notebook comments for detailed explanations

---

**Happy Learning! 🎓**

_Last Updated: April 2026_

## Tech Stack

- Python 3.9+
- NumPy
- Jupyter Notebook
- VS Code + Jupyter extension (recommended)

## Setup

### Option A: VS Code (recommended)

1. Open this repository in VS Code.
2. Install the Python and Jupyter extensions.
3. Create and activate a virtual environment.
4. Install dependencies.
5. Open any notebook inside the `NumPy/` folder and select a Python kernel.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependency:

```bash
pip install numpy jupyter
```

### Option B: Jupyter directly

```bash
jupyter notebook
```

Then open notebooks from the `NumPy/` directory.

## How to Use This Repository

1. Start with `1numpy_arrays.ipynb`.
2. Continue with `2arrays_types.ipynb`.
3. Finish the current module with `3dimension_shapes.ipynb`.
4. Run cells top-to-bottom and modify examples to test your understanding.
5. Re-run sections after edits to verify outputs and strengthen retention.

## Recommended Learning Workflow

- Read markdown explanation first
- Predict output before running each code cell
- Run the cell and compare with your prediction
- Change values/shapes/types and observe behavior
- Write short notes about what surprised you

## Progress Snapshot

- [x] NumPy basics: arrays and indexing
- [x] NumPy dtypes and type behavior
- [x] Dimensions and shapes
- [ ] Reshaping and broadcasting deep dive
- [ ] Vectorized operations mini-projects
- [ ] Pandas fundamentals
- [ ] Data visualization fundamentals
- [ ] First end-to-end ML project

## Why This Journey Matters

Machine learning models are only as strong as your understanding of data structures and transformations. Mastering NumPy early creates a strong base for:

- data preprocessing
- feature engineering
- model input pipelines
- efficient numerical computing

## Next Planned Additions

- `NumPy/4reshaping_broadcasting.ipynb`
- `NumPy/5vectorized_operations.ipynb`
- A dedicated `Pandas/` learning track
- Starter project folders for regression/classification workflows

## Contributing

This is primarily a personal learning repository, but feedback and suggestions are welcome.

Ways to contribute:

- open an issue with improvement ideas
- suggest better explanations for notebook sections
- propose additional practice tasks

## License

No license file is currently defined.
If this repo is meant to be open for reuse, add a `LICENSE` file (for example, MIT).

## Contact

If you are also learning machine learning, feel free to fork this repository and build your own progression path.
