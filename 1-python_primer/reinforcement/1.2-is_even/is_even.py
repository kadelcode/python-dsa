# is_even.py

def is_even(k):
    """
    This function checks if a number is even
    
    Args:
        k: The number to check

    Returns:
        `True` if k is even, `False` otherwise
    """
    # Bitwise AND of a number with 1 returns 0 only if LSB is 0,
    # which is the case for even numbers
    return k & 1 == 0

# Example usage
print(is_even(2)) # True
print(is_even(3)) # False
