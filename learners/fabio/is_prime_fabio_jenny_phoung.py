"""Test if number is prime."""

def is_prime(n):
    """Function to test if a number is prime."""
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))     