
# 1. How to start project?

## How to clone project?

```text
git@gitlab.com:public-projects1853809/dash-mantine-template.git
```

```text
cd dash-mantine-template
```

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

### 1. Run PyTest
### 2. Sort imports
### 3. Format code
### 4. Lint code


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


