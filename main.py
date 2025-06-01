import random
import string

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")


    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation


    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with a mix of all characters
    all_chars = uppercase + lowercase + digits + symbols
    remaining_chars = [random.choice(all_chars) for _ in range(length - 4)]
    password.extend(remaining_chars)

    # Shuffle to avoid predictable order
    random.shuffle(password)

    return ''.join(password)


if __name__ == "__main__":
    user_length = int(input("Enter password length (min 8): "))
    try:
        pwd = generate_password(user_length)
        print(f"Generated Password: {pwd}")
    except ValueError as ve:
        print(f"Error: {ve}")
