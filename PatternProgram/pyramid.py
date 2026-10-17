# Number of rows for the pyramid
rows = 5

for i in range(1, rows + 1):
    # Print spaces to center align the numbers
    print(" " * (rows - i), end="")
    
    # Print increasing numbers
    for j in range(1, 2 * i):
        print(j, end="")
        
    # Move to the next line
    print()