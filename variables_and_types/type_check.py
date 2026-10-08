# type_check.py - checks the types of different values

# Predictions:
# 8080 -> int
# "8080" -> str
# 99.5 -> float
# "198.51.100.7" -> str
# 1_000 -> int

print(8080, type(8080))
print("8080", type("8080"))
print(99.5, type(99.5))
print("198.51.100.7", type("198.51.100.7"))
print(1_000, type(1_000))

# Conversions:
# "443" -> int
# 8080 -> str
# "2.5" -> float

print(int("443"), type(int("443")))
print(str(8080), type(str(8080)))
print(float("2.5"), type(float("2.5")))