import math

def safe_sqrt(number1: float):
    """
    Return then real square root of a number 1: reject negative input."""
    try:
        if number1 < 0:
            raise ValueError("negative values are not allowed for real square root ")
        result = math.sqrt(number1)
        print(f"Result: {result}")
        return result
    except ValueError:
        print("Error invalid input ! please enter a positive integer or float value")
        return None

# test case 

user_input = float(input("enter a number:"))
safe_sqrt(user_input)

