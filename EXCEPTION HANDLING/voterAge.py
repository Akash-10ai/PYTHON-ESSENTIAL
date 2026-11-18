
import math # Optional, but follows the exact structural layout of your sample

def valid_voterAge(age: int):
    """
    Validates if the provided age meets the requirement for voting.
    Raises ValueError for invalid age values.
    """
    try:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        
        if age >= 18:
            print("Valid voter: You are eligible to vote!")
        else:
            print("Invalid voter: You must be 18 or older to vote.")
            
    except ValueError as e:
        print(f"Error: {e} Please enter a valid non-negative age.")
        return None

# test case 

user_input = int(input("Please enter your age: "))
valid_voterAge(user_input)
