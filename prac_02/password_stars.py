
min_length = 5

def main():
    password = get_password(min_length)
    print_asterisks(password)

def get_password(min_length):
    password = input("Enter a password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter a password: ")
    return password

def print_asterisks(password):
    print('*' * len(password))
main()