# password_check.py
# A Password Check

def long_enough(password, minimum=8):
    """Check if the password is long enough."""
    return len(password) >= minimum


def differs_from_username(password, username):
    """Check if the password differs from the username."""
    return password != username


def password_ok(password, username):
    """Check if both password requirements are satisfied."""
    return long_enough(password) and differs_from_username(password, username)


username = input("Username: ")
password = input("Password: ")

if password_ok(password, username):
    print("Password accepted.")
else:
    print("Password rejected.")