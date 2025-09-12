
# 1. How to start project?

## How to clone project?

<details>

<summary>Steps</summary>


1. Clone project

```bash
git clone git@gitlab.com:public-projects1853809/dash-mantine-template.git
```

2. Change directory

```bash
cd dash-mantine-template
```

3. Create necessary sub-directories

```bash
mkdir temp; 
mkdir temp/logs;
```

3a. Create Postgress database

- Here is instruction how ro create pg database: https://gitlab.com/public-projects1853809/dash-mantine-template/-/boards?show=eyJpaWQiOiIyOSIsImZ1bGxfcGF0aCI6InB1YmxpYy1wcm9qZWN0czE4NTM4MDkvZGFzaC1tYW50aW5lLXRlbXBsYXRlIiwiaWQiOjE3MzQxODQ3Nn0%3D

4. Run app

```bash
uv run my-new-app
```

</details>

## How to clone project under your project name?

<details>

<summary>Steps</summary>


1. Create new package

```bash
uv init --package my-new-app
```

2. Clone dash-mantine-project

```bash
git clone git@gitlab.com:public-projects1853809/dash-mantine-template.git
```

3. Delete everything from folder my-new-app

```bash
cd my-new-app
rm -rf *
rm .gitignore
rm .python-version
```

4. Copy everything from dash-mantine-project onto my-new-app folder

5. Rename names in pyproject.toml file.

```txt
# Old

name = "dash-mantine-template"
authors = [
    { name = "Milan Mitrovic", email = "milanmitrovic1991@gmail.com" }
]
[project.scripts]
dash-mantine-template = "dash_mantine_template:main"
```


```txt
# New

name = "my-new-app"
authors = [
    { name = "Name Surname", email = "user@email.com" }
]
[project.scripts]
my-new-app = "my_new_app:main"
```

```bash
# rename source folder

- mv src/dash_mantine_template/ src/my_new_app/

```

6. Rename imports in pages/ folder:

```python
# Old

from dash_mantine_template.components.filters.radio_button
import (
    radio_button__component,
)
```

```python
# New

from my_new_app.components.filters.radio_button import (
    radio_button__component,
)
```

7. Rename filepath to html template:

```python
# Old

with open(
        "src/dash_mantine_template/components/miscellaneous/InitialTheme.html",
        "r",
        encoding="utf-8",
    ) as file:
        html_string = file.read()
```

```python
# New

with open(
    "src/my_new_app/components/miscellaneous/InitialTheme.html",
        "r",
        encoding="utf-8",
    ) as file:
        html_string = file.read()

```

8. Create necessary folders inside temp/ directory:

```bash
mkdir temp; 
mkdir temp/logs;
```

8a. Create pg database

- Here is instruction how ro create pg database: https://gitlab.com/public-projects1853809/dash-mantine-template/-/boards?show=eyJpaWQiOiIyOSIsImZ1bGxfcGF0aCI6InB1YmxpYy1wcm9qZWN0czE4NTM4MDkvZGFzaC1tYW50aW5lLXRlbXBsYXRlIiwiaWQiOjE3MzQxODQ3Nn0%3D

9. Run app.

```bash
uv run my-new-app
```


10. Rename imports in tests/ folder:

```bash

find tests/ -type f -name "*.py" -exec sed -i '' 's/from my_new_app\./from dash_mantine_template./g' {} +


```


</details>


## How to sync project?

```text
uv sync --dev
```

## How to start project?

```text
uv run dash-mantine-template
```

## How to run tests?

```text
 uv run pytest .
```

## How to get coverage report?

```text
COVERAGE_FILE=temp/coverage_data/.coverage uv run python -m pytest --cov .
```

## How to save coverage report in .html file?

```text
COVERAGE_FILE=temp/coverage_data/.coverage pytest --cov=. --cov-report=html:temp/coverage_report/html --cov-report=xml:temp/coverage_report/xml/coverage.xml
```

## How to add project dependency?

```text
uv add python_package_name
```

## How to add development dependency?

```text
uv add --dev package_name
```

## How to install project with 'dev' dependencies?

```text
uv sync --dev
```


## How to run ruff linter?

```text
uv run ruff check
```

# Linter fix
```text
uv run ruff check --fix
```

## How to run ruff formatter? 

```text
uv run ruff format
```

## How to sort imports?

```text
uv run ruff check --select I --fix
```

## What code quality steps should be done before each commit?

- Run PyTest
- Sort imports
- Format code
- Lint code

## Pyway migrations
- INFO: uv run pyway info
- VALIDATE: uv run pyway validate
- MIGRATE: uv run pyway migrate
- IMPORT: ...
- CHECKSUM: ...


# 2. How to develop product using project template?

## Workflow
- Create feature branch
- Merge it into develop
- Create release branch from develop
- Deploy release branch to UAT
- Where to iterate (implement user feedback)? On release or on develop branch?
- What to do with development of features that being developed after rc (release candidate) branch was created?
    - Shall we merge changes into develop or wait?

    
## Branches:
- main
- develop
- feature/branch_name
- release/branch_name

## Tags:
- test-version_number
- uat-version_number
- prod-version_number

## Deployment strategy:
- There are 3 levels of permissions.
- Deployment to TEST, UAT, PROD.
- How is deployment triggered?
  - Deployment is triggered after TAG with specific name pattern is created.
  - Depending on TAG name, different CICD pipeline is triggered.
  - Different users have different right to create different TAGs.
    - Developer can create TAG that starts with TEST-version_number
    - Higher authority I can create TAG with UAT-version_number
    - Higher authority II can create tag with PROD-version_number

## Git strategy:
1. Create issue
2. Create PR/MR
3. 


