PASSWORD_LENGTH = 10


def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input('Enter a password: ')
    while len(password) < PASSWORD_LENGTH:
        print(f'Password must be at least {PASSWORD_LENGTH} characters long.')
        password = input('Enter a password: ')
    return password


def print_asterisks(password):
    print("*" * len(password))


if __name__ == '__main__':
    main()
