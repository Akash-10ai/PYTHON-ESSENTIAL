def safe_divide(numerator,denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("ERROR: cannot divide by zero")
        return None

# Test case 

numerator = int(input("enter the numerator value:"))
denominator = int(input("enter the denominator value:"))
print(safe_divide(numerator,denominator))