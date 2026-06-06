
import sys

from backend_starter.generator import create_project


def main() -> None:
    if len(sys.argv) != 2:
        print("Uso: backend-starter <nombre_proyecto>")
        sys.exit(1)

    project_name = sys.argv[1]

    create_project(project_name)


if __name__ == "__main__":
    main()