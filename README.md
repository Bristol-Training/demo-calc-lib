# GitHub Practical - Calculator Library


A simple Python calculator library for practicing GitHub workflows, team collaboration, automated testing, and continuous integration.

## Project Files

- `calc_lib.py` - A library containing basic arithmetic functions
- `calc_demo.py` - A demo script that uses the calculator library
- `test_calc_lib.py` - Pytest test suite for the calculator library
- `.github/workflows/pytest.yml` - GitHub Actions CI workflow

## Getting Started

#### Prerequisites

- Python 3.8 or higher
- A package manager: pip, conda, or uv

#### `pytest` installation

Install testing dependencies using your preferred package manager:

::: {.panel-tabset}

## pip
```bash
# Using pip (built-in with Python)
pip install pytest pytest-cov
```

## conda
```bash
# Using conda (recommended for data science)
conda install pytest pytest-cov
```

## uv
```bash
# Using uv (fast, modern alternative)
uv pip install pytest pytest-cov
```
:::

#### Usage

Run the demo script:

```bash
python calc_demo.py
```

Or import the calculator library in your own code:

```python
from calc_lib import add, subtract, multiply, divide

result = add(5, 3)
print(result)  # Output: 8
```

## Calculator Functions

The calculator library provides four basic operations:

- `add(a, b)` - Returns the sum of a and b
- `subtract(a, b)` - Returns a minus b
- `multiply(a, b)` - Returns the product of a and b
- `divide(a, b)` - Returns a divided by b (raises ValueError if b is zero)

## Testing

This project includes a simple pytest test suite to demonstrate good testing practices.

To run all tests locally:

```bash
pytest -v
```

Run tests with coverage report:

```bash
pytest --cov=. --cov-report=term
```


## Continuous Integration

This repository uses **GitHub Actions** to automatically run tests on every push and pull request. The CI workflow:

- Tests against multiple Python versions (3.8, 3.9, 3.10, 3.11)
- Runs the full pytest suite with coverage reporting
- Verifies the demo script executes successfully

You can view the test results in the **Actions** tab of the GitHub repository.

## Practice Exercise

Here is an exercise for practicing Git and GitHub workflows. Add a new function power(a, b) that calculates $a^b$. Write tests for the new function and watch the tests run automatically.


#### 1. Fork and Clone

You cannot create a branch directly in someone else's repository if you're not a collaborator. Click the "Fork" button on GitHub to copy this repo to your account first. Then clone your fork:

```bash
git clone https://github.com/YOUR_USERNAME/github-calc.git
cd github-calc
```

#### 2. Create a Feature Branch

```bash
git checkout -b feature/new-power-function
```

This creates the branch and switches to it in one command.

#### 3. Make Changes and Commit

Edit the files using your text editor, then:

```bash
git status                      # See what files you changed
git add .                       # Stage all changed files
git commit -m "Add power function to calculator"
```

#### 4. Run Tests Locally

Before pushing, make sure all tests pass:

```bash
pytest -v
```

#### 5. Push and Create Pull Request

```bash
git push origin feature/new-power-function
```

- Go to GitHub and click "Compare & pull request"
- Add description and request review
- Watch the automated tests run in the PR
- Merge via the web interface once tests pass


<br>
© 2025 Pau Erola, Jean Golding Institute, University of Bristol
