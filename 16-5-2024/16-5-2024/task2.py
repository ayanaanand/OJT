def calculate_prime(number):
    """Determine if a number is a prime number.
    
    Args:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    # Check if number is less than 2 (not prime)
    if number < 2:
        return False

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True


num = 9
if calculate_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
