# Change this number to test different values
num = 29  

# Prime numbers must be greater than 1
if num > 1:
    is_prime = True
    
    # Check factors from 2 up to the square root of the number (highly optimized)
    # If a number has a factor, it must have one less than or equal to its square root.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  # Stop looping immediately if a factor is found
            
    if is_prime:
        print(f"🎉 {num} is a PRIME number!")
    else:
        print(f"❌ {num} is a composite number (not prime).")
else:
    print(f"❌ {num} is not a prime number (primes must be greater than 1).")
