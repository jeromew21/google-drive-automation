#!/usr/bin/python3
import sys
import os
from drive_automation import *

#In case the script is located elsewhere
os.chdir("/home/jerome/DriveAutomation") 

if __name__ == "__main__":
    args = sys.argv[1:]
    command = args[0]
    autom = DriveAutomator()
    if command == 'new':
        autom.create_doc("New Document")
    elif command == 'open':
        webbrowser.open("https://drive.google.com/drive/u/0/my-drive")
    elif command == 'ls':
        autom.list_files(100)