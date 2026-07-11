
from collections.abc import Callable
from pathlib import Path

from backend_starter.templates.basic import create_basic_structure
from backend_starter.templates.command_line import create_command_line_structure
from backend_starter.templates.fastapi import create_fastapi_structure


TemplateBuilder = Callable[[Path, str], None]


TEMPLATE_BUILDERS: dict[str, TemplateBuilder] = {
    "basic": create_basic_structure,
    "fastapi": create_fastapi_structure,
    "command-line": create_command_line_structure,
}
