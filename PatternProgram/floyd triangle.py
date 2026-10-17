def print_floyd_triangle(rows):
    # Initialize the starting number
    number = 1
    
    # Outer loop handles the number of rows
    for i in range(1, rows + 1):
        # Inner loop handles the numbers printed in each row
        for j in range(1, i + 1):
            print(number, end=" ")
            number += 1  # Increment the number for the next position
        # Move to the next line after finishing a row
        print()

# Take input from the user
num_rows = int(input("Enter the number of rows: "))
print_floyd_triangle(num_rows)