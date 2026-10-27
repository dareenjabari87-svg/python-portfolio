# Login Decision

MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"

username = input()
failed = int(input())
password = input()

if failed >= MAX_FAILED:
    print("Account locked.")
elif username != KNOWN_USER:
    print("Unknown user.")
elif password == STORED_PASSWORD:
    print("Access granted.")
else:
    print("Access denied. Attempts left:", MAX_FAILED - failed - 1)
