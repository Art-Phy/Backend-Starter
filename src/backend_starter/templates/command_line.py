
from pathlib import Path

from backend_starter.templates.basic import create_basic_structure



def create_command_line_structure(project_path: Path, package_name: str) -> None:
    """Create a basic command-line project structure"""
    create_basic_structure(project_path, package_name)
    