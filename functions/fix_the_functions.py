# fix_the_functions.py

# Runtime bug 1: Define the function before calling it.
def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)


print_header()


def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
        total = failed * minutes

        # Logic bug 2: Return total instead of 0.
        return total

    return 0


def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"


# Runtime bug 3: Use username instead of user.
print(login_line(username="sara", failed=4))


# Logic bug 4: Print the result instead of only calling the function.
print(login_line("omar", 1))