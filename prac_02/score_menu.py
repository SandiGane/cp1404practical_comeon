"""
Display MENU
get valid score
print result
show stars (as many as score
"""


MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Get menu choice and display result"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid")
        score = int(input("Enter score: "))
    print(MENU)
    choice = input(">>> ").upper()
    if choice == "G":
        print(score)
    elif choice == "P":
        print(f"This score is {get_result(score)}")
    elif choice == "S":
         print("*" * score)
    elif choice == "Q":
        print("Farewell")
    else:
        print("Please enter valid choice")
        print(MENU)
        choice = input(">>> ".upper())


def get_result(score):
    """Gets result based on score and returns"""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


main()
