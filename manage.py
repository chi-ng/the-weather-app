#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    #show instruction!
    print()
    print()
    print("####################################################")
    print("## If this is your new pull                       ##")
    print("## Do 'pip install -r requirements.txt' again     ##")
    print("## this make your develop environment up to date  ##")
    print("#############     Victor Zhang     #################")
    print()
    print()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
