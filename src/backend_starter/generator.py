
import subprocess
from pathlib import Path

from backend_starter.templates import TEMPLATE_BUILDERS
from backend_starter.templates.ai import (
    AGENT_TEMPLATE,
    PROJECT_TEMPLATE,
)

from backend_starter.templates.basic import (
    CHANGELOG_TEMPLATE,
    GITIGNORE_TEMPLATE,
    README_TEMPLATE,
)



def create_project(project_name: str, create_venv: bool = False, create_ai_docs: bool = False, template: str = "basic") -> None:
    project_path = Path(project_name)
    package_name = project_name.replace("-", "_")

    project_path.mkdir()

    TEMPLATE_BUILDERS[template](
        project_path,
        package_name,
    )

    if create_ai_docs:
        create_ai_documentation(project_path)

    initialize_git(project_path)

    if create_venv:
        create_virtual_environment(project_path)
    
    print(f"✅Proyecto '{project_name}' creado satisfactoriamente.\n" 
          f"📁 Ruta: {project_path.resolve()}"
    ) 



def create_ai_documentation(project_path: Path) -> None:
    """Create optional AI documentation files"""

    (project_path / "AGENT.md").write_text(
        AGENT_TEMPLATE,
        encoding="utf-8",
    )

    (project_path / "PROJECT.md").write_text(
        PROJECT_TEMPLATE,
        encoding="utf-8",
    )



def initialize_git(project_path: Path) -> None:
    subprocess.run(
        ["git", "init"],
        cwd=project_path,
        check=True,
    )

    subprocess.run(
        ["git", "checkout", "-b", "develop"],
        cwd=project_path,
        check=True,
    )



def create_virtual_environment(project_path: Path) -> None:
    subprocess.run(
        ["python3", "-m", "venv", ".venv"],
        cwd=project_path,
        check=True,
    )
