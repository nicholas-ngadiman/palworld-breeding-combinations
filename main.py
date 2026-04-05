"""Main Entry Point"""
from pal_input import set_cli_args, ask_user_for_input
from automate_combinations import get_breeding_combinations

RESULTS_FILE_NAME = "results.txt"

def main():
    """Main Function"""
    filename = set_cli_args()
    print("This script requires you to enter all the Pal names that will be the parents and then it will output the all the children that can be bred, along with the combinations.")
    print("The Pal names need to be spelled correctly, but do not need to be capitalised.")
    pals = ask_user_for_input(filename)
    combinations = get_breeding_combinations(pals)
    print(f"Writing results into: {RESULTS_FILE_NAME}")
    with open(RESULTS_FILE_NAME , "w", encoding="utf-8") as f:
        for k, v in combinations.items():
            f.write(f"{k}: {v}\n\n")
if __name__ == "__main__":
    main()
