#!/usr/bin/python3
import sys

from drive_automation import *

if __name__ == "__main__":
    args = sys.argv[1:]
    command = args[0]
    autom = DriveAutomator()
    if command == 'new':
        autom.create_doc("New Document")
    elif command == 'ls':
        autom.list_files(100)