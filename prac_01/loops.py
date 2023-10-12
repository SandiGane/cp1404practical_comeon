"""
3. Loops
"""

# Display odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Count in 10s from 0 t0 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Descending from 20 to 1
for i in range(21, 0, -1):
    print(i, end=' ')
print()

# Stars loop
number_of_stars = int(input("Number: "))
for i in range(number_of_stars):
    print("*", end="")
print()

# Increasing stars
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars + 1):
    print("*" * i)
print()
