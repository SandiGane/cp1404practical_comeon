"""
get low and high number
check high is higher than low
n = random number between low and high
print n smiley faces
"""

"""import random

def main():
    low, high = get_limits()
    number_of_smileys = random_number()
    print( ":)" * number_of_smileys)


def get_limits():
    low = int(input("Set low number: "))
    high = int(input("Set high number: "))
    while high <= low:
        print(f"High number must be higher than low - {low}")
        high = input("Set high number: ")
    return low, high


def random_number(low, high):
        get_limits()
        number_of_smileys = random.randint(low, high + 1)
        return number_of_smileys


main()
"""

# def is_even (number):
#     if number % 2 == 0:
#         """
#         def is_even(number):
#         return number % 2 == 0
#
# Name functions "this function will..."
# determine_grade
# convert_USD_to_AUD
# print_report
# calculate_average
# is_even
# get_valid_age

# Osmond's way


import random

def main():
    low = get_number("Low: ")
    high = get_number("High: ")
    while high <= low:
        print("Error")
        high = get_number("High: ")
    random_number = random.randint(low, high)
    print_smiley_faces(random_number)

def get_number(prompt):
    number = int(input(prompt))
    return number


def print_smiley_faces(number_of_smileys):
    print(":)" * number_of_smileys)

main()