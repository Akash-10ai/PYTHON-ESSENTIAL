def sum_to_n_formula(n):
    if n < 1:

        return (n * (n + 1)) // 2

user_input = input("Enter a positive whole number:" )
number = int(user_input)

result = sum_to_n_formula(number)
print(f"the sum of number 1 to {number} is: {result}")