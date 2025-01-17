#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

def main():
    """Run administrative tasks."""
    # Add the project root directory to Python path
    project_root = str(Path(__file__).resolve().parent)
    sys.path.append(project_root)
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line # type: ignore
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "activate your virtual environment?\n"
            f"Current Python path: {sys.path}\n"
            f"Current working directory: {os.getcwd()}"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()