"""
CP1404/CP5632 - Practical 2
Add functions to temperature conversation code
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    choice = get_choice()
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Thank you.")


def get_choice():
    print(MENU)
    choice = input(">>> ").upper()
    while choice == "Q" or choice == "C" or choice == "F":
        return choice
    else:
        print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()


# get_choice()
main()