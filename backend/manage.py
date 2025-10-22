#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from build_frontend import build_react

def main():
    """Run administrative tasks."""
    # 1️⃣ Build React first
    build_react()

    # 2️⃣ Then start Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
