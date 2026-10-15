# 1. Ask the user for a number and convert it to an integer
limit = int(input("Enter a limit number: "))

total_sum = 0

# 2. Loop through odd numbers up to the limit
for num in range(1, limit + 1, 2):
    total_sum += num

# 3. Print the final answer
print(f"The sum of all odd numbers up to {limit} is: {total_sum}")
