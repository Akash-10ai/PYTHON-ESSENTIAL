def calculate_factorial(n):
    """Calculates the factorial of a number using a loop."""
    if n < 0:
        return "Factorial does not exist for negative numbers."
    
    result = 1
    # Loop from 1 up to n (n + 1 is exclusive)
    for i in range(1, n + 1):
        result *= i  # Equivalent to: result = result * i
        
    return result

# Example usage:
number = 5
output = calculate_factorial(number)
print(f"The factorial of {number} is: {output}")
# Output: The factorial of 5 is: 120
