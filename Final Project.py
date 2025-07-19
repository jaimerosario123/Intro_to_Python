import hashlib
import re


def hash_password(password):
    sha256_hash = hashlib.sha256(password.encode()).hexidigest()
    return sha256_hash


def is_password_strong(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[\W_]', password):
        return False
    return True


print("This is a very simple password-hashing tookl for LIS4930")
print()
print(
    "Password should be eight characters or more, containing at least one special character and at least one number. This ensures password complexity")
print()
print("This tool uses SHA256, a solid hashing algorithm used within the realm of Cybersecurity.")
print()
print("      ↓")
print()

while True:
    password = input("Enter password: ")

    if not is_password_strong(password):
        print(
            "I tried to warn you. Your password is not safe it must be 8 characters, containing symbols and numbers. Try again. I just don't want you to get hacked.")
    else:

        hashed_password = hash_password(password)
        print(f"Voila, your hashed password; {hashed_password}")
        break
