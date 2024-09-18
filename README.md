# Dash Mantine Project Template



# First steps after cloning

1. Rename project folder
    - In pyproject.toml file, replace every occurrence of following name with name of your project:
        - dash-mantine-template


2. Add dependencies in pyproject.toml file
    - Production dependencies
    - Optional dependencies


3. PyCharm setup

    - Make src folder as source folder (settings --> project --> project structure)
    - Choose python interpreter from venv (created in next section)
    - In run/debug configuration uncheck following two items:
        - Add content roots to PYTHONPATH
        - Add source roots to PYTHONPATH


# Run project

1. Go into dash-mantine-directory

    ```shell script
    cd dash-mantine-template
    ```

2. Upgrade pip

    ```python
    python -m pip install --upgrade pip
    ```

3. Install virtual environment

    ```python
    python -m venv venv
    ```

4. Install project in editable mode

    ```python
    pip install -e .[dev]
    ```

5. Install project for production

    ```python
    pip install .
    ```


# Run tests

1. Go to root directory
    ```shell script
    cd dash-mantine-template
    ```

2. Start tests

    ```shell script
    pytest .
    ```


# Make sure that pre-commit hook works

    - Make sure that you have pre-commit installed

    ```shell script
    pre-commit install

    ```
