"""Module for Retrieving User's Pal Names"""
import sys

def ask_user_for_input(filename: str | None = None) -> list[str]:
    """ Ask user for all Pal names"""
    pals: list[str] = []
    if filename is None:
        print("Press 'Y/y' to proceed to the next step. Press 'N/n' to exit.")
        while True:
            pal = input(f"Please enter the name of Pal {len(pals) + 1}: ").strip().title()
            if pal == 'N':
                sys.exit()
            if pal =='Y':
                break
            pals.append(pal)
    else:
        print(f"Opening file: {filename}")
        with open(filename, "r", encoding="utf-8") as f:
            pals = f.readlines()
    return pals
