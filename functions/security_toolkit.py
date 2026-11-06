# security_toolkit.py

MIN_LENGTH = 8


def border(width):
    """Print a border with the given width."""
    print("+" + "-" * (width + 2) + "+")


def show_box(text):
    """Print text inside a box."""
    border(len(text))
    print("| " + text + " |")
    border(len(text))


def show_menu():
    """Display the security toolkit menu."""
    print("SECURITY TOOLKIT")
    print()
    print("1. Check a port")
    print()
    print("2. Check a password")
    print()
    print("3. PIN guessing time")
    print()
    print("q. Quit")
    print()


def port_range(port):
    """Return the port range category or invalid."""
    if port < 0 or port > 65535:
        return "invalid"
    elif port <= 1023:
        return "system"
    elif port <= 49151:
        return "user"
    else:
        return "dynamic"


def check_port():
    """Ask for a port and display its category."""
    port = int(input("Port: "))
    show_box(f"Port {port}: {port_range(port)}")


def password_problem(password, username):
    """Return the first password problem, or an empty string."""
    if len(password) < MIN_LENGTH:
        return "too short"
    elif password == username:
        return "same as the username"
    return ""


def check_password():
    """Ask for a username and password, then check them."""
    username = input("Username: ")
    password = input("Password: ")

    problem = password_problem(password, username)

    if problem:
        show_box(f"Rejected: {problem}")
    else:
        show_box("Password accepted")


def days_to_guess(digits, per_second):
    """Calculate whole days needed to try every PIN."""
    return 10 ** digits // per_second // 86400


def check_pin():
    """Ask for PIN details and display the guessing time."""
    digits = int(input("PIN digits: "))
    per_second = int(input("Guesses per second: "))

    days = days_to_guess(digits, per_second)
    show_box(f"{digits} digits: {days} days")


# Main program
show_menu()

checks = 0

while True:
    choice = input("Choice (1, 2, 3, or q): ")

    if choice == "1":
        check_port()
        checks += 1
    elif choice == "2":
        check_password()
        checks += 1
    elif choice == "3":
        check_pin()
        checks += 1
    elif choice == "q":
        show_box(f"Checks done: {checks}")
        break
    else:
        print("Unknown choice.")
        print()
