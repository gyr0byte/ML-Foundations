# Machine Learning Journey

This repository is a lightweight notebook-based workspace for learning core Python data science and machine learning concepts. At the moment, it focuses on NumPy fundamentals through a single hands-on notebook.

## What is in this repo

- `NumPy/numpy_arrays.ipynb` - a beginner-friendly notebook covering basic array creation and indexing with NumPy.

## Notebook overview

The current notebook demonstrates:

- importing NumPy with `import numpy as np`
- creating one-dimensional arrays with `np.array(...)`
- mixing integer and floating-point values in arrays
- accessing array elements by index

## Requirements

- Python 3.9 or newer
- Jupyter Notebook or VS Code with the Jupyter extension
- `numpy`

## Getting started

1. Open the workspace in VS Code.
2. Open `NumPy/numpy_arrays.ipynb`.
3. Select a Python kernel.
4. Run the notebook cells from top to bottom.

If you want to use a terminal instead, install the dependency first:

```bash
pip install numpy
```

Then start Jupyter:

```bash
jupyter notebook
```

## Example code

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([0, 0.5, 1, 1.5, 2])

print(a[0], a[1])
```

## Suggested next steps

- add notebook examples for array shape, dtype, slicing, and reshaping
- explore vectorized arithmetic and broadcasting
- expand the repo with additional notebooks for pandas, visualization, or model training

## Repository layout

```text
.
├── README.md
└── NumPy/
	└── numpy_arrays.ipynb
```

## Notes

This repository is still small, so the README is intentionally broad and easy to extend as you add more notebooks and examples.
