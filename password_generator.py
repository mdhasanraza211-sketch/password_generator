import random
import string
from datetime import datetime


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    else:
        return "Strong"


def save_password(password):
    with open("saved_passwords.txt", "a") as file:
        file.write(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {password}\n"
        )


def main():
    print("=" * 50)
    print("      ADVANCED PASSWORD GENERATOR")
    print("=" * 50)

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length must be at least 4.")
            return

        count = int(input("How many passwords do you want to generate? "))

        use_upper = input(
            "Include Uppercase Letters? (y/n): "
        ).lower() == "y"

        use_lower = input(
            "Include Lowercase Letters? (y/n): "
        ).lower() == "y"

        use_digits = input(
            "Include Numbers? (y/n): "
        ).lower() == "y"

        use_symbols = input(
            "Include Special Characters? (y/n): "
        ).lower() == "y"

        print("\nGenerated Passwords")
        print("-" * 50)

        for i in range(count):
            password = generate_password(
                length,
                use_upper,
                use_lower,
                use_digits,
                use_symbols
            )

            if password is None:
                print("Please select at least one character type.")
                return

            strength = check_strength(password)

            print(f"{i + 1}. {password}")
            print(f"   Strength: {strength}")

            save_password(password)

        print("\nPasswords saved in 'saved_passwords.txt'")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()