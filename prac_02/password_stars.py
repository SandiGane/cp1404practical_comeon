"""
Password Stars
set minimum password length
get password
while password length is < 8 characters,
    print "Error, password must be {password length} characters long"
    get password
for number of password characters,
    print *
"""

MINIMUM_LENGTH = 6


def main():
    """Print password stars"""
    password = get_password()
    print_stars(password)


def print_stars(password):
    """print * for length of password"""
    print("*" * len(password))


def get_password():
    """get password, error and loop if less than minimum length"""
    password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        print("Error, password must be {password length} characters long")
        password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    return password


main()