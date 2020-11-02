"""
A simple script that blacks and pylints *.py files

http://pylint.pycqa.org/en/latest/
"""

# STANDARD PYTHON MODULES
import os
from time import time

# these can be safely ignored in most circumstances
DISABLE = (
    # too many?
    "too-many-statements",
    "too-many-locals",
    "too-many-branches",
    "too-many-function-args",
    "too-many-arguments",
    "too-many-nested-blocks",
    "too-many-lines",
    # improper exception handling
    "bare-except",
    "broad-except",
    # snake_case, etc.
    "invalid-name",
    # sometimes it just can't find the modules referenced - on this machine
    "import-error",
    # whitespace authoritarianism
    "bad-continuation",
    "bad-whitespace",
    # class minimums
    "too-few-public-methods",
    "no-self-use",
    # suppression
    "suppressed-message",
    "locally-disabled",
    "useless-suppression",
)


def user_input():
    """
    prompt user to choose to use: black, pylint, and isort
    """
    # Black
    dispatch = {
        1: "Black All!",
        2: "Skip",
    }
    print("\n          Black Menu\n")
    for key, val in dispatch.items():
        print("         ", key, "  :  ", val)
    black_choice = input("\n\nInput Number or Press Enter for Choice 1\n\n  ")
    if black_choice == "":
        black_choice = 1
    black_choice = int(black_choice)
    # Pylint
    dispatch = {
        1: "Pylint-Lite All!",
        2: "Pylint All!",
        3: "Skip",
    }
    print("\n          Pylint Menu\n")
    for key, val in dispatch.items():
        print("         ", key, "  :  ", val)
    pylint_choice = input("\n\nInput Number or Press Enter for Choice 1\n\n  ")
    if pylint_choice == "":
        pylint_choice = 1
    pylint_choice = int(pylint_choice)
    disabled = ""
    if pylint_choice == 1:
        disabled = "--enable=all --disable="
        for item in DISABLE:
            disabled += item + ","
        disabled.rstrip(",")
    # Isort
    dispatch = {
        1: "Isort All!",
        2: "Skip",
    }
    print("\n          Isort Menu\n")
    for key, val in dispatch.items():
        print("         ", key, "  :  ", val)
    isort_choice = input("\n\nInput Number or Press Enter for Choice 1\n\n  ")
    if isort_choice == "":
        isort_choice = 1
    isort_choice = int(isort_choice)

    return black_choice, pylint_choice, isort_choice, disabled


def main():
    """
    \033c\nWelcome to lite Black Pylint Lite All! \n
    """
    print(main.__doc__)
    black_choice, pylint_choice, isort_choice, disabled = user_input()
    start = time()
    print("\033c")
    # Get all of the python files in the current folder
    pythons = [filer for filer in os.listdir() if filer.endswith(".py")]
    # Sort Imports
    if isort_choice == 1:
        for name in pythons:
            print("Isorting script:", name)
            os.system(f"isort {name}")
            print("-" * 100)
    # Black Format
    if black_choice == 1:
        for name in pythons:
            print("Blacking script:", name)
            os.system(f"black {name}")
            print("-" * 100)
    # Pylint
    if pylint_choice in [1, 2]:
        for name in pythons:
            print("Pylinting script:", name)
            os.system(f"pylint {name} {disabled}")
            print("-" * 100)
    elapsed = time() - start
    print("Done.\n\n", len(pythons), "scripts took %.1f" % elapsed, "seconds.")


if __name__ == "__main__":
    main()
