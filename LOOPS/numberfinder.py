numbers = [12, 25, 36, 48, 50, 67, 89]
search = int(input("Enter a number to search: "))

found = False

for num in numbers:
    print("Checking number:", num)

    if num == search:
        print("Number found:", num)
        found = True
        break

if not found:
    print("Number not found in the list.")

print("Search operation completed.")