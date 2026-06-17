
import subprocess
from pathlib import Path

from backend_starter.templates import(
    CHANGELOG_TEMPLATE,
    GITIGNORE_TEMPLATE,
    README_TEMPLATE,
)



def create_project(project_name: str, create_venv: bool = False) -> None:
    project_path = Path(project_name)

    package_name = project_name.replace("-", "_")

    project_path.mkdir()

    src_path = project_path / "src" / package_name
    tests_path = project_path / "tests"

    src_path.mkdir(parents=True)
    tests_path.mkdir()


    (project_path / "README.md").write_text(
        README_TEMPLATE.format(project_name=project_name),
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
        encoding="utf-8",
    )

    (src_path / "__init__.py").write_text(
        "",
        encoding="utf-8",
    )

    (tests_path / "__init__.py").write_text(
        "",
        encoding="utf-8",
    )

    initialize_git(project_path)

    if create_venv:
        create_virtual_environment(project_path
                                  )
    print(f"✅Proyecto '{project_name}' creado satisfactoriamente.\n" 
          f"📁 Ruta: {project_path.resolve()}"
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
