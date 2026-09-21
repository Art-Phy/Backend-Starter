"""
Templates for the core project structure.

These templates are generated for every new project created by Backend Starter.
"""


README_TEMPLATE = """
# {project_name}

Descripción pendiente.

## Instalación

## Uso

## Testing

## Licencia
"""

CHANGELOG_TEMPLATE = """
# Changelog

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


from pathlib import Path


def create_basic_structure(project_path: Path, package_name: str) -> None:
    """Create the basic Python project structure"""
    src_path = project_path / "src" / package_name
    tests_path = project_path / "tests"

    src_path.mkdir(parents=True)
    tests_path.mkdir()

    (project_path / "README.md").write_text(
        README_TEMPLATE.format(project_name=project_path.name),
        encoding="utf-8",
    )

    (project_path / "CHANGELOG.md").write_text(
        CHANGELOG_TEMPLATE,
        encoding="utf-8",
    )

    (project_path / "requirements.txt").write_text(
        "",
        encoding="utf-8",
    )

    (project_path / ".gitignore").write_text(
        GITIGNORE_TEMPLATE,
        encoding="utf-8,"
    )

    (src_path / "__init__.py").write_text(
        "",
        encoding="utf-8",
    )

    (tests_path / "__init__.py").write_text(
        "",
        encoding="utf-8",
    )
