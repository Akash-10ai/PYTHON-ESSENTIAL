# Take input from the user
rows = int(input("Enter the number of rows: "))

# Loop starts from total rows and counts down to 1
for i in range(rows, 0, -1):
    # Print the changing number of leading spaces
    print(" " * (rows - i), end="")
    # Print the stars with a space in between
    print("* " * i)
