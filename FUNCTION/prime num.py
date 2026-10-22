def is_prime(n):
    # NUm55ber less than or equal to 1 are not prime
    if n <= 1:
        return False

    # 2 is the only even prime number 
    if n == 2:
        return True

    # Exclude all other even number imidiately
    if n % 2 == 0:
        return False

    # cheak add factor up to the square root of n 
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2 # skip even number by icrementing by 2 

    return True

user_input = input("Enter a whole number to cheak : ")
number = int(user_input)

if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is NOT a prime number")