"""Main Entry Point"""
from pal_input import ask_user_for_input
from run_playwright import get_combinations

def main():
    """Main Function"""
    print("This script requires you to enter all the Pal names that will be the parents and then it will output the all the children that can be bred, along with the combinations.")
    print("The Pal names need to be spelled correctly, but do not need to be capitalised.")
    pals = ask_user_for_input()
    combinations = get_combinations(pals)
    print(combinations)
if __name__ == "__main__":
    main()
