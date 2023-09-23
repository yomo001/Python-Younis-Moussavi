# start with the main, and enter the other functions in the same order they are to be read 
# Clean code - clear variable names, order of functions according to above
# Refractioning or something: Something in the code is changed to make it clearer - without changing its functionality. Even changing variable name is such thing.


# START WITH MAIN; AND THEN START TYPING BENEATH IT EVERYTHING; EVEN FUNCTION TO BE CALLED AND AFTER THAT DEFINE AND WRITE THE FUNCTION BELOW, 
SIGNS = ["rock", "paper", "scissors"]     # in python, capitalization is done to mark that this global variable is CONSTANT and NOT to be changed anywhere.

def main():
    print(f"Welcome to the {', '.join(SIGNS)} game.")
    print_rules()


def print_rules():
    print("\nRules: Each player picks a sign.")
    for winner, loser in zip([0, 1, 2], [2, 0, 1]):
        print(f"{SIGNS[winner]} wins over {SIGNS[loser]}")


main()
