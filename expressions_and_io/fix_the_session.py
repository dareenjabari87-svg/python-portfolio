
# fix_the_session.py
# This program reports a user's session time.

username = input("Username: ")

# runtime: convert the input string to an integer before calculating
total_seconds = int(input("Session length in seconds: "))

minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 30)

# semantic: use an f-string to display the username value
print(f"User: {username}")

# runtime: use an f-string to combine text and numeric values
print(f"Session: {minutes} min {seconds} s")
print("=" * 30)
