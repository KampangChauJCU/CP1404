MIN_LENGTH = 4


def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    password = input("Enter password of at least {} characters: ".format(min_length))
    while len(password) < min_length:
        print("Password too short")
        password = input("Enter password of at least {} characters: ".format(min_length))
    return password


def print_asterisks(sequence):
    print('*' * len(sequence))


main()
