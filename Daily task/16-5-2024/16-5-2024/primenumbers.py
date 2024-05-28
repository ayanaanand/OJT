def calculate_prime(num):
    # Check if the number is less than 2
    if num < 2:
        return False  # Numbers less than 2 are not prime
    
    # Check for factors from 2 to the number itself
    for i in range(2, num):
        if num % i == 0:
            return False  # If the number is divisible by any other number, it's not prime
    
    return True  # If the number is not divisible by any other number, it's prime
print(calculate_prime(12))