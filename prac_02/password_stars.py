"""
CP1404 - Practical
Get a password with minimum length and display it as asterisks
"""
PASSWORD_LENGTH = 10


def main():
    """Get user password and print password as asterisks"""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get password with a minimum length requirement"""
    password = input('Enter a password: ')
    while len(password) < PASSWORD_LENGTH:
        print(f'Password must be at least {PASSWORD_LENGTH} characters long.')
        password = input('Enter a password: ')
    return password


def print_asterisks(password):
    """Print as many asterisks as there are in a password"""
    print("*" * len(password))


if __name__ == '__main__':
    main()
