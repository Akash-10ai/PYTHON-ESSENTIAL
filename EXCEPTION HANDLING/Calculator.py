def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        raise ValueError(f"Unknown operator '{op}'")

tests = [("10", "5", "+"), ("8", "0", "/"), ("abc", "2", "*"), ("4", "2", "%")]

for x, y, op in tests:
    try:
        result = calculate(float(x), float(y), op)
        print(f"{x} {op} {y} = {result}")
    except ZeroDivisionError:
        print(f"{x} {op} {y} -> Cannot divide by zero")
    except ValueError as e:
        print(f"{x} {op} {y} -> Invalid input: {e}")