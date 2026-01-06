# 🚀 Project Setup & Development Guide

## 📋 Table of Contents
- [Getting Started](#getting-started)
- [Project Management](#project-management)
- [Code Quality](#code-quality)
- [Development Workflow](#development-workflow)

---

## Getting Started

### 🔄 Clone Project (Quick Start)

<details>
<summary><strong>View Steps</strong></summary>

**1. Clone the repository**
```bash
git clone git@gitlab.com:public-projects1853809/dash-mantine-template.git
```

**2. Navigate to project directory**
```bash
cd dash-mantine-template
```

**3. Create PostgreSQL database**

Use this `docker-compose.yml` configuration:

```yaml
services:
  db:
    image: postgres:15  
    container_name: postgres_db
    restart: always
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydatabase
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
```

**4. Run the application**
```bash
uv run my-new-app
```

</details>

---

### 🎯 Clone Project with Custom Name

<details>
<summary><strong>View Steps</strong></summary>

**1. Create new package**
```bash
uv init --package my-new-app
```

**2. Clone dash-mantine-project**
```bash
git clone git@gitlab.com:public-projects1853809/dash-mantine-template.git
```

**3. Clean the new project folder**
```bash
cd my-new-app
rm -rf *
rm .gitignore
rm .python-version
```

**4. Copy template files**

Copy everything from `dash-mantine-project` to `my-new-app` folder

**5. Update `pyproject.toml`**

*Before:*
```toml
name = "dash-mantine-template"
authors = [
    { name = "Milan Mitrovic", email = "milanmitrovic1991@gmail.com" }
]
[project.scripts]
dash-mantine-template = "dash_mantine_template:main"
```

*After:*
```toml
name = "my-new-app"
authors = [
    { name = "Name Surname", email = "user@email.com" }
]
[project.scripts]
my-new-app = "my_new_app:main"
```

**6. Rename source folder**
```bash
mv src/dash_mantine_template/ src/my_new_app/
```

**7. Update imports in `pages/` folder**

*Before:*
```python
from dash_mantine_template.components.filters.XYZ import (
    ZXY,
)
```

*After:*
```python
from my_new_app.components.filters.radio_button import (
    radio_button__component,
)
```

**8. Update HTML template filepath**

*Before:*
```python
with open(
    "src/dash_mantine_template/components/miscellaneous/InitialTheme.html",
    "r",
    encoding="utf-8",
) as file:
    html_string = file.read()
```

*After:*
```python
with open(
    "src/my_new_app/components/miscellaneous/InitialTheme.html",
    "r",
    encoding="utf-8",
) as file:
    html_string = file.read()
```

**9. Create PostgreSQL database**

Use the same `docker-compose.yml` from Quick Start section

**10. Run the application**
```bash
uv run my-new-app
```

**11. Update test imports**
```bash
find tests/ -type f -name "*.py" -exec sed -i '' 's/from my_new_app\./from dash_mantine_template./g' {} +
```

</details>

---

## Project Management

### 📦 Dependencies

**Sync project dependencies**
```bash
uv sync --dev
```

**Add project dependency**
```bash
uv add python_package_name
```

**Add development dependency**
```bash
uv add --dev package_name
```

**Install with dev dependencies**
```bash
uv sync --dev
```

---

### 🔧 Pre-commit Hooks

**1. Auto-update hook versions**
```bash
uv run pre-commit autoupdate
```

**2. Reinstall hooks**
```bash
uv run pre-commit install --install-hooks
```

**3. Run hooks**
```bash
# Run on staged files
uv run pre-commit run

# Run on all files
uv run pre-commit run --all-files
```

---

### ▶️ Running the Project

**Start application**
```bash
uv run dash-mantine-template
```

---

## Code Quality

### 🧪 Testing

**Run tests**
```bash
uv run pytest .
```

**Generate coverage report**
```bash
COVERAGE_FILE=temp/coverage_data/.coverage uv run python -m pytest --cov .
```

**Save coverage report as HTML**
```bash
COVERAGE_FILE=temp/coverage_data/.coverage pytest --cov=. --cov-report=html:temp/coverage_report/html --cov-report=xml:temp/coverage_report/xml/coverage.xml
```

---

### ✨ Code Formatting & Linting

**Run ruff linter**
```bash
uv run ruff check
```

**Auto-fix linter issues**
```bash
uv run ruff check --fix
```

**Format code**
```bash
uv run ruff format
```

**Sort imports**
```bash
uv run ruff check --select I --fix
```

---

### ✅ Pre-commit Checklist

Before each commit, ensure you:
- ✓ Run PyTest
- ✓ Sort imports
- ✓ Format code
- ✓ Lint code

---

### 🗄️ Database Migrations (Pyway)

```bash
# View migration info
uv run pyway info

# Validate migrations
uv run pyway validate

# Run migrations
uv run pyway migrate

# Import (TBD)
# Checksum (TBD)
```

---

## Development Workflow

### 🌿 Branch Strategy

**Branch Types:**
- `main` - Production-ready code
- `develop` - Integration branch for features
- `feature/branch_name` - Feature development
- `release/branch_name` - Release preparation

---

### 🏷️ Tagging Convention

- `test-version_number` - Test environment
- `uat-version_number` - UAT environment
- `prod-version_number` - Production environment

---

### 🚢 Deployment Strategy

**Three-tier deployment process:**

| Environment | Tag Pattern | Permission Level |
|-------------|-------------|------------------|
| TEST | `test-version_number` | Developer |
| UAT | `uat-version_number` | Higher Authority I |
| PROD | `prod-version_number` | Higher Authority II |

**How it works:**
- Deployment is triggered when a TAG with specific name pattern is created
- Different CICD pipelines run based on TAG name
- User permissions determine which TAGs can be created

---

### 🔄 Workflow Process

1. Create feature branch from `develop`
2. Merge feature into `develop`
3. Create release branch from `develop`
4. Deploy release branch to UAT
5. Iterate on feedback (on release or develop branch?)
6. Handle concurrent feature development after release candidate creation

**Open Questions:**
- Where to iterate user feedback? Release or develop branch?
- How to handle features being developed after RC branch creation?
  - Merge changes into develop or wait?

---

### 📝 Git Workflow

1. Create issue
2. Create Pull/Merge Request
3. (To be continued...)

---

*Last updated: January 2026*