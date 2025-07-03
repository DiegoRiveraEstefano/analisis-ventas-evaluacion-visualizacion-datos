# data visualization template

## Description

This is a template for data visualization projects. It includes a virtual environment, a list of dependencies, and a main file.


### Requirements

- Python 3.12
- pip
- virtualenv

### Project structure
- `data/`: The directory for storing data files.
- `src/`: The directory for storing source code files.
- `notebooks/`: The directory for storing Jupyter Notebook files.
- `tests/`: The directory for storing test files.
- `reports/`: The directory for storing reports.
- `.vscode/`: The directory for storing Visual Studio Code settings.
- `main.py`: The main file of the project.
- `requirements.txt`: The list of dependencies for the project.
- `pyproject.toml`: The configuration file for the project.
- `README.md`: This file.
- `.gitignore`: The list of files and directories to be ignored by Git.
- `.python-version`: The version of Python to be used by the project.


### normative references
- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/)

## How to use

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

## Code Quality

### Code formatting
To format the code, use the following command:

```bash
ruff .
```

### Code linting
To lint the code, use the following command:

```bash
mypy src
```

### Code style
To check the code style, use the following command:

```bash
ruff .
```

## Testing

### Unit tests
To run the unit tests, use the following command:

```bash
pytest tests/unit
```

### Integration tests
To run the integration tests, use the following command:

```bash
pytest tests/integration
```

The integration tests will be executed and the results will be displayed.

The unit tests will be executed and the results will be displayed.

### Test coverage
To generate a test coverage report, use the following command:

```bash
pytest --cov=src --cov-report=html
```

The test coverage report will be generated in the `htmlcov` directory.


## documentation
The documentation will be generated using Sphinx.

To generate the documentation, use the following command:

```bash
sphinx-build -b html docs/source docs/build
```

The documentation will be generated in the `docs/build` directory.

## License
This project is licensed under the MIT License.

## Contact
If you have any questions or suggestions, please contact me at [my email](mailto:your-email@example.com).
