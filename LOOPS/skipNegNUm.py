numbers = [10, -5, 20, -8, 30, 0, 15, -3]
total = 0

print("Positive Number Checking Program")
print("--------------------------------")

for num in numbers:
    print("Checking number:", num)

    if num < 0:
        print("Negative number skipped")
        continue

    print("Number accepted:", num)
    total = total + num
    print("--------------------------")

print("Sum of non-negative numbers:", total)
print("Program completed successfully")