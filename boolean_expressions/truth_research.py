
# bool("") prints False because the string is empty.
# bool("0") prints True because the string contains a character.
# bool(0) prints False because the number is zero.
# bool(0.0) prints False because the number is zero.
# bool("False") prints True because the string is not empty.

# Source: https://docs.python.org/3/library/stdtypes.html#truth-value-testing

print(bool(""))
print(bool("0"))
print(bool(0))
print(bool(0.0))
print(bool("False"))
