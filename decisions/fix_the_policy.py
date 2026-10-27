
# fix_the_policy.py
# Check a new password against an example policy and classify its length.

MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# Bug 1 - Syntax: Missing colon
if len(password) < MIN_LENGTH:
    # Bug 2 - Syntax: Missing indentation
    print("- Too short.")
elif password == username:
    print("- Same as the username.")

# Bug 3 - Semantic: Check the longer length first
if len(password) >= 16:
    strength = "long"
# Bug 4 - Semantic: Check acceptable length after long
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

print(f"Length: {len(password)} ({strength})")
