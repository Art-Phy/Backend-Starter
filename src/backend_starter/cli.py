
import argparse

from backend_starter.generator import create_project


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a backend project structure."
    )

    parser.add_argument(
        "project_name",
        help="Name of the project to create."
    )
    
    parser.add_argument(
        "--venv",
        action="store_true",
        help="Create a virtual enviroment inside the project",
    )

    args = parser.parse_args()
    create_project(args.project_name, create_venv=args.venv)

if __name__ == "__main__":
    main()