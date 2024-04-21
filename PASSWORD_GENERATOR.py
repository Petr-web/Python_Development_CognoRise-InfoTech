import random
import string

def generate_password(length, complexity):
    characters = ""

    if complexity == "1":
        characters = string.ascii_letters
    elif complexity == "2":
        characters = string.ascii_letters + string.digits
    elif complexity == "3":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Please try again.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the desired complexity level:\n1: Letters\n2: Letters + Digits\n3: Letters + Digits + Special Characters\n")
    password = generate_password(length, complexity)

    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()