# conditional_tests.py

user = "analyst"
role = "viewer"
failed = 3
port = 22

print("Is user == 'analyst'? I predict True.")
print(user == "analyst")

print("\nIs role != 'viewer'? I predict False.")
print(role != "viewer")

print("\nIs failed > 3? I predict False.")
print(failed > 3)

print("\nIs port < 22? I predict False.")
print(port < 22)

print("\nIs failed >= 3? I predict True.")
print(failed >= 3)

print("\nIs port <= 22? I predict True.")
print(port <= 22)

print("\nIs user == 'analyst' and role == 'viewer'? I predict True.")
print(user == "analyst" and role == "viewer")

print("\nIs failed == 0 or port == 22? I predict True.")
print(failed == 0 or port == 22)

print("\nIs not (role == 'viewer')? I predict False.")
print(not (role == "viewer"))

print("\nIs user == 'admin' or failed < 3? I predict False.")
print(user == "admin" or failed < 3)
