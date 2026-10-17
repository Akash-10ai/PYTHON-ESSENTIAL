def print_hollow_diamond(rows):
    # 1. Upper half of the diamond
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(1, rows - i + 1):
            print(" ", end="")
        
        # Print stars and inner spaces
        for k in range(1, 2 * i):
            if k == 1 or k == (2 * i - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

    # 2. Lower half of the diamond
    for i in range(rows - 1, 0, -1):
        # Print leading spaces
        for j in range(1, rows - i + 1):
            print(" ", end="")
        
        # Print stars and inner spaces
        for k in range(1, 2 * i):
            if k == 1 or k == (2 * i - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Get input from the user
try:
    num_rows = int(input("Enter the number of rows for the half-diamond: "))
    print("\nHere is your hollow diamond pattern:")
    print_hollow_diamond(num_rows)
except ValueError:
    print("Please enter a valid integer.")