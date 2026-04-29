# Machine Learning Journey

A personal, hands-on repository documenting my machine learning learning path from fundamentals to practical implementation.

This project is built as a notebook-first learning workspace. Each notebook focuses on one concept, with code examples and outputs that make the progression visible.

## Project Goals

- Build strong foundations in Python, NumPy, and data handling
- Practice writing clean, readable, reproducible notebook code
- Create a public record of progress and milestones
- Transition from fundamentals to applied machine learning projects

## Current Focus

The current phase is **NumPy fundamentals**, with a focus on understanding arrays as the core data structure for machine learning workflows.

## Repository Structure

```text
.
├── README.md
└── NumPy/
    ├── 1numpy_arrays.ipynb
    ├── 2arrays_types.ipynb
    └── 3dimension_shapes.ipynb
```

## Learning Modules

### 1) NumPy Arrays

Notebook: `NumPy/1numpy_arrays.ipynb`

Topics covered:

- NumPy import and setup
- Creating arrays with `np.array(...)`
- Basic indexing
- Slicing and selecting ranges
- Accessing multiple positions

### 2) Array Types (dtypes)

Notebook: `NumPy/2arrays_types.ipynb`

Topics covered:

- Integer and floating-point arrays
- Mixed-type arrays and automatic type promotion
- Inspecting and understanding `dtype`
- Why data types matter for memory and computation

### 3) Dimensions and Shapes

Notebook: `NumPy/3dimension_shapes.ipynb`

Topics covered:

- 1D vs 2D array structures
- Reading and interpreting `.shape`
- Reading dimensions using `.ndim`
- Row/column layout intuition
- Building arrays with explicit shape awareness

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
