# Change this to any number you want to test
num = 4523  
running_num = num
total_sum = 0

# Loop until there are no digits left
while running_num > 0:
    # 1. Get the last digit using the modulo operator (%)
    digit = running_num % 10
    
    # 2. Add the digit to our total
    total_sum += digit
    
    # 3. Remove the last digit from the number using floor division (//)
    running_num = running_num // 10

print(f"The sum of the digits in {num} is: {total_sum}")
# Process: 3 + 2 + 5 + 4 = 14
