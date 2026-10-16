products = ["Laptop", "Mouse", "Keyboard", "Monitor", "USB"]
prices = [50000, 500, 1200, 8000, 300]
total = 0

print("Welcome to Online Shopping")
print("--------------------------")

for i in range(len(products)):
    print("Product:", products[i])
    print("Price:", prices[i])

    if prices[i] < 1000:
        print("Low-cost item skipped")
        print("--------------------------")
        continue

    print("Product added to bill")
    total = total + prices[i]
    print("--------------------------")

print("Final Shopping Bill:", total)
print("Thank you for shopping!")