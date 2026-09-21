
from backend_starter.templates.fastapi import create_fastapi_structure



def test_fastapi_template_create_main_file(tmp_path):
    """FastAPI template should create the application entry point"""

    project_path = tmp_path / "marge"
    project_path.mkdir()

    create_fastapi_structure(
        project_path,
        "marge",
    )

    main_file = project_path / "src" / "marge" / "main.py"

    assert main_file.exists()



def test_fastapi_template_creates_requirements(tmp_path):
    """FastAPI template should include its required dependencies"""

    project_path = tmp_path / "marge"
    project_path.mkdir()

    create_fastapi_structure(
        project_path,
        "marge",
    )

    requirements_file = project_path / "requirements.txt"
    requirements = requirements_file.read_text(encoding="utf-8")

    assert "fastapi" in requirements
    assert "uvicorn[standard]" in requirements
