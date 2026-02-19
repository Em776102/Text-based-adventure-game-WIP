import time
import builtins
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow(text):
    """Print text slowly for effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()

def wait():
    input("\nPress ENTER to continue...")
