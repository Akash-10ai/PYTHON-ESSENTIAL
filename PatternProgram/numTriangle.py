# Number of rows for the triangle
rows = 5

# Outer loop to handle the rows
for i in range(1, rows + 1):
    # Inner loop to handle the numbers in each row
    for j in range(1, i + 1):
        print(j, end=" ")
    # Move to the next line after completing a row
    print()