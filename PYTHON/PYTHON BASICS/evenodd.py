# check if a number is even or odd

# taking number from user

number = int(input("enter a number: "))

# if number is divisible by 2 then it is even otherwise odd
if(number % 2 == 0):
    print("even")
else:
    print("odd")