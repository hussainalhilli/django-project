#!/usr/bin/env python
import os
import sys
# Husseins project with Mo
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "byoot.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
