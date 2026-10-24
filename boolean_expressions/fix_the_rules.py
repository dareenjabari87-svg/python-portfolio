
# fix_the_rules.py
# This program checks a connection against three rules.

role = input("Role: ")

# runtime: Convert the port input from a string to an integer for numeric comparison.
port = int(input("Port: "))

# semantic: Use == to compare the role instead of = to assign a value.
is_admin = role == "admin"

# syntax: Use <= instead of the invalid operator =<.
is_system_port = port <= 1023

# semantic: Compare both sides of or with port.
is_web_port = port == 80 or port == 443

print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")
