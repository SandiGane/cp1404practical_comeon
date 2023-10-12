"""Module 2 - Functions
"""
import random

"""Write a program that asks the user for a length,
then generates a random width between 1 and the length,
and prints this and the area of a rectangle of length x width
Dont forget import random

import random
get length
get rand.int width
print area of length x width is answer"""

# import random
# length = int(input("Length: "))
# width = random.randint(1, 10)
# print(f"Area of {length} x {width} is {length * width}")

# def print_line(length):
#     print('-' * length)
#
# print_line(10)

number = random.randbytes(1.45)
# def print_grid(number_of_rows, number_of_columns):
# version 3
number_of_columns = 5
number_of_rows = 6
print(f"{"number" * number_of_columns} * number_of_rows)
# version 2
for i in range(number_of_rows):
    print('*' * number_of_columns)
    # version 1
    #     for i in range(number_of_rows):
    #         for j in range(number_of_columns):
    #             print('*', end="")
    #             print()

#
# # print_grid(3, 7)
#
# """value-returning functions and SRP"""

# import random
# def main():
#     height = random.uniform(1, 2)
#     if calculate_bmi(height, 99) < 15:
#         print("Not considered overweight")
#
#
# def calculate_bmi(height, weight):
#     return weight / (height ** 2)
#
#
# main()
