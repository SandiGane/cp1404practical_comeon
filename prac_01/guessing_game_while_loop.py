"""
Guessing game while loop from Week 1 lecture videos
note nothing after WHILE, just print at prime
This is on Patterns page
"""

SECRET = 6
guess = int(input("? "))
while guess != SECRET:
    print("Guess again!")
    guess = int(input("? "))
print("You got it!")
