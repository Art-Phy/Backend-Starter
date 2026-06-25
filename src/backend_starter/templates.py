
README_TEMPLATE = """# {project_name}

Descripción pendiente.

## Instalación

## Uso

## Testing

## Licencia
"""


CHANGELOG_TEMPLATE = """# Changelog

## [Unreleased]

"""


GITIGNORE_TEMPLATE = """
### Ignore ###

# Byte-compiled / optimized / DLL files
**/.DS_Store
__pycache__/*
*.py[cod]

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*,cover

# Translations
*.mo
*.pot

# Django stuff:
*.log

# Sphinx documentation
docs/_build/

# PyBuilder
target/
*.zip
"""


AGENT_TEMPLATE = """
# AGENTS.md

# Development Guidelines

---

# Core Principles

---

# Project Structure

Unless the project requires otherwise:

Typical layout:

---

# Language Style

---

# Documentation

Documentation is considered part of the project.

README:

- Written in "add your language".

CHANGELOG:

- Written in "add your language".
- Follow Keep a Changelog.

Release Notes:

- Written in "add your language".

Code comments:

- Written in English.

Docstrings:

- Written in English.

---

# Git Workflow

Use GitFlow.

Typical branches:

```text
feature/*
bugfix/*
hotfix/*
release/*
```

Never work directly on `main`.

Commits must be written in English.

---

# Testing

Before considering a task finished:

---

# Dependencies

---

# CLI Applications

For CLI projects:

---

# APIs

---

# Database

Prefer:

---

# Docker

When Docker is used:

---

# Documentation Quality

When modifying documentation:

- Keep examples updated.
- Keep version numbers consistent.
- Update `CHANGELOG.md` when needed.
- Update `README.md` if features, commands or setup steps change.
- Prefer clear explanations over overly technical wording.

---

# Agent Behaviour

When making suggestions:

When editing code:

If multiple solutions exist:

If an improvement could be beneficial but was not requested:

Never introduce unnecessary complexity.

---

# Philosophy

"""