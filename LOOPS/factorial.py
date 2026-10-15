# Change this number to find its factorial
num = 5  
factorial = 1

# Check if the number is negative, zero, or positive
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # Loop from 1 to num (inclusive)
    for i in range(1, num + 1):
        factorial = factorial * i
        
    print(f"The factorial of {num} is {factorial}")
