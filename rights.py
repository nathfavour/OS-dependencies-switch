#!/usr/bin/env python3

import os
import platform
import subprocess

# Get the operating system name
os_name = platform.system()

# Get the shell or terminal name
shell_name = os.environ.get("SHELL") or os.environ.get("COMSPEC")

# Define the file name
file_name = input("What file do you want to grant all rights to?")

# Define the command to run depending on the operating system and shell
if os_name == "Windows":
    if shell_name.endswith("powershell.exe"):
        command = f"icacls {file_name} /grant Everyone:F"
    elif shell_name.endswith("cmd.exe"):
        command = f"attrib +r {file_name}"
    else:
        command = None
elif os_name == "Linux" or os_name == "Darwin":
    if shell_name.endswith("bash"):
        command = f"chmod a+x {file_name}"
    else:
        command = None
else:
    command = None

# Run the command if it is not None
if command:
    subprocess.run(command, shell=True)
else:
    print(f"Sorry, I don't know how to run the command for {os_name} and {shell_name}")