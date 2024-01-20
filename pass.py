import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(quantity=1, length=12):
    passwords = [generate_password(length) for _ in range(quantity)]
    return passwords

def main():
    try:
        password_length = int(input("Enter the length of the password: "))
        password_quantity = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Please enter valid numeric values.")
        return

    if password_length <= 0 or password_quantity <= 0:
        print("Please enter positive values for length and quantity.")
        return

    passwords = generate_multiple_passwords(password_quantity, password_length)

    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()
