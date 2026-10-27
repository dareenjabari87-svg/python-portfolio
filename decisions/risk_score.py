# Risk Score Calculator
score = 0

failed = int(input())
hour = int(input())
new_device = input()

if failed >= 3:
    score += 40

if hour < 6:
    score += 30

if new_device == "yes":
    score += 30

if score >= 70:
    level = "HIGH"
elif score >= 30:
    level = "MEDIUM"
else:
    level = "LOW"

print(f"Risk score: {score} ({level})")