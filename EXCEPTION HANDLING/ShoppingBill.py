try:
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative.")

    total = price * quantity

    print("Total Bill:", total)

except ValueError as e:
    print("Input Error:", e)

except OverflowError:
    print("Error: Number is too large.")

finally:
    print("Thank you for shopping!")