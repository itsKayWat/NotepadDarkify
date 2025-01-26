import subprocess
import sys

def install_requirements():
    try:
        # No external packages required for this project
        # winreg is part of Python's standard library
        print("No additional packages required!")
        print("The script uses only built-in Python libraries.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    install_requirements()