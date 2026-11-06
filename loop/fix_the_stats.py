# fix_the_stats.py
# Count failed logins and the average session length.

events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Bug 1: failed must be initialized before the loop to count all failed logins.
failed = 0

for event in events:
    if event == "FAILED":
        failed += 1

print(f"Failed logins: {failed}")

total = 0
count = 0

for value in minutes:
    if value > 0:
        total += value
        count += 1

# Bug 2: Use / instead of // to calculate the average as a float.
print(f"Average session: {total / count} minutes")

# Bug 3: Move the average print statement outside the loop to print it only once.

# Bug 4: Change the range ending value to 5 to include Level 4.
for level in range(1, 5):
    print(f"Level {level}")