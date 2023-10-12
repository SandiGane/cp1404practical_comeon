"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

"""

Use if elif else structure to debug code
score must be between 0-100
>=90 = excellent
>=50 = pass
<50 = bad"""

score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))
if score >= 90:
    print("Excellent")
elif score > 50:
    print("Passable")
else:
    print("Bad")
