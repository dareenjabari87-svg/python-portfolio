seconds = int(input("Session length in seconds: "))
minutes = seconds // 60
remaining_seconds = seconds % 60

print(f"Session length: {minutes} minutes and {remaining_seconds} seconds.")


# Test outputs:
# 905 -> Session length: 15 minutes and 5 seconds
# 60 -> Session length: 1 minutes and 0 seconds
# 59 -> Session length: 0 minutes and 59 seconds