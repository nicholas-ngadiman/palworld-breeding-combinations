"""Module for Retrieving User's Pal Names"""
import sys

def ask_user_for_input() -> list[str]:
    """ Ask user for all Pal names"""
    pals: list[str] = []
    print("Press 'Y/y' to proceed to the next step. Press 'N/n' to exit.")
    while True:
        pal = input(f"Please enter the name of Pal {len(pals) + 1}: ").strip().title()
        if pal == 'N':
            sys.exit()
        if pal =='Y':
            break
        pals.append(pal)
    return pals
