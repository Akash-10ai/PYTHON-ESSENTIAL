class InsufficientBalanceError(Exception):
    pass

balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")

    if amount > balance:
        raise InsufficientBalanceError("Insufficient bank balance.")

    balance -= amount

    print("Withdrawal successful.")
    print("Remaining Balance:", balance)

except ValueError as e:
    print("Input Error:", e)

except InsufficientBalanceError as e:
    print("Transaction Failed:", e)

finally:
    print("Thank you for using our banking service.")