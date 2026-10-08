# int_research.py - tests which strings can be converted to integers

# Predictions:
# int(" 22 ") will work because surrounding whitespace is allowed.
# int("+22") will work because a plus sign is allowed before the number.
# int("0022") will work because leading zeros are allowed.
# int("2_2") will work because a single underscore between digits is allowed.

print(int(" 22 "))
print(int("+22"))
print(int("0022"))
print(int("2_2"))

# Documentation:
# https://docs.python.org/3/library/functions.html#int
