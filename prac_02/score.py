"""
CP1404 - Prac 2
Add functions to last week's broken_scores code
"""

"""
main function
    get user score
     print result
function to get score
    """


def main():
    """Get score and display result"""
    score = float(input("Enter score: "))
    print(get_result(score))


def get_result(score):
    """Determine result based on score"""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


main()
