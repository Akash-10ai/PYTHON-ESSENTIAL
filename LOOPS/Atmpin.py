# pythin program to perform for loop
correct_pin = "1234"
attempts = 3

for i in range(attempts):
    pin = input("Enter your ATM PIN: ")

    if pin == correct_pin:
        print("PIN verified successfully!")
        print("Access granted.")
        break
    else:
        print("Wrong PIN!")
        print("Attempts left:", attempts - i - 1)

else:
    print("Your account is temporarily locked.")

print("Thank you for using ATM.")
