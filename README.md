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
  Master 1D, 2D, and multi-dimensional arrays.

**Topics:**

- 1D vs 2D vs N-dimensional arrays
- Understanding `.shape` and `.ndim` attributes
- Row-major (C-style) vs column-major (Fortran-style) ordering
- Reshaping and transposing arrays
- Building mental models for multi-dimensional data

---

#### Module 4: Indexing and Slicing

**File:** `NumPy/4_indexing_slicing_iteration.ipynb`

Advanced techniques for accessing and selecting array elements.

**Topics:**

- Basic indexing for 1D, 2D, and N-D arrays
- Slicing with step values and negative indices
- Fancy indexing with integer arrays
- Boolean masking and conditional selection
- Copy vs view operations

---

#### Module 5: Statistics and Aggregation

**File:** `NumPy/5_statistics.ipynb`

Perform statistical calculations on arrays.

**Topics:**

- Computing mean, median, standard deviation, variance
- Sum, product, and cumulative operations
- Min and max operations with `argmin()` and `argmax()`
- Percentiles and quantiles
- Working with NaN and infinite values

---

#### Module 6: Broadcasting and Vectorization

**File:** `NumPy/6_broadcasting_vectorize.ipynb`

Harness NumPy's power through broadcasting and vectorized operations.

**Topics:**

- Broadcasting rules and implicit array expansion
- Element-wise operations across differently-shaped arrays
- Avoiding loops with vectorized functions
- Universal functions (ufuncs) and their benefits
- Performance implications of vectorization

---

#### Module 7: Boolean Arrays and Conditional Operations

**File:** `NumPy/7_boolean_arrays.ipynb`

Use boolean indexing for powerful data filtering.

**Topics:**

- Creating boolean arrays through comparisons
- Boolean indexing and masking
- Logical operations (AND, OR, NOT)
- Combining multiple conditions
- Filtering and selecting subsets of data

---

#### Module 8: Linear Algebra

**File:** `NumPy/8_linear_algebra.ipynb`

Essential linear algebra operations for machine learning.

**Topics:**

- Matrix multiplication and dot products
- Eigenvalues and eigenvectors
- Matrix decomposition (SVD, QR)
- Solving linear systems
- Norms and distance calculations

---

#### Module 9: Size of Objects in Memory

**File:** `NumPy/9_size_of_objectsInMemory.ipynb`

Explore how array size and data types affect memory usage.

**Topics:**

- Estimating array memory footprint
- Comparing dtypes and storage size
- Understanding bytes per element
- Practical tips for memory efficiency

---

#### Module 10: Useful NumPy Functions

**File:** `NumPy/10_useful_numpy_function.ipynb`

Learn a toolbox of NumPy utilities for everyday workflows.

**Topics:**

- Common utility functions and helpers
- Array creation shortcuts
- Sorting and searching helpers
- Performance-friendly patterns

---

#### Module 11: NumPy Operations

**File:** `NumPy/11_numpy_operations.ipynb`

Practice core operations that show up across ML and data workflows.

**Topics:**

- Element-wise operations
- Reduction operations
- Shape-altering operations
- Combining arrays and outputs

---

#### Module 12: Reshaping In Depth

**File:** `NumPy/12_Reshaping_inDepth.ipynb`

Deep dive into reshaping strategies for real-world workflows.

**Topics:**

- Reshaping with `reshape()` and `ravel()`
- Resizing vs reshaping
- Order parameter (`C` vs `F`)
- Practical reshaping patterns

---

## 🗺️ Roadmap

### Current Phase ✅

- [x] NumPy fundamentals (12 modules)

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

1. Start with `1_numpy_arrays.ipynb`.
2. Continue with `2_arrays_types.ipynb`.
3. Move to `3_dimension_shapes.ipynb`.
4. Continue sequentially through `12_Reshaping_inDepth.ipynb`.
5. Run cells top-to-bottom and modify examples to test your understanding.
6. Re-run sections after edits to verify outputs and strengthen retention.

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
- [x] Reshaping and broadcasting deep dive
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
