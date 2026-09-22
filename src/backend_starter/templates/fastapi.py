
from pathlib import Path

from backend_starter.templates.basic import create_basic_structure


FASTAPI_MAIN_TEMPLATE = '''"""Main FastAPI application."""

from fastapi import FastAPI

app = FastAPI(
    title="{project_name}",
)


@app.get("/")
def root() -> dict[str, str]:
    """Return a basic welcome response."""
    return {{"message": "Welcome to {project_name}"}}
'''


FASTAPI_REQUIREMENTS_TEMPLATE = """fastapi
uvicorn[standard]
"""


FASTAPI_README_TEMPLATE = """# {project_name}

Backend API generated with Backend Starter using FastAPI.

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Run

Start the development server:

```bash
uvicorn {package_name}.main:app --app-dir src --reload
```

The API will be available at:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
"""


def create_fastapi_structure(
    project_path: Path,
    package_name: str,
) -> None:
    """Create a basic FastAPI project structure."""

    create_basic_structure(project_path, package_name)

    package_path = project_path / "src" / package_name

    (package_path / "main.py").write_text(
        FASTAPI_MAIN_TEMPLATE.format(
            project_name=project_path.name,
        ),
        encoding="utf-8",
    )

    (project_path / "requirements.txt").write_text(
        FASTAPI_REQUIREMENTS_TEMPLATE,
        encoding="utf-8",
    )

    (project_path / "README.md").write_text(
        FASTAPI_README_TEMPLATE.format(
            project_name=project_path.name,
            package_name=package_name,
        ),
        encoding="utf-8",
    )
