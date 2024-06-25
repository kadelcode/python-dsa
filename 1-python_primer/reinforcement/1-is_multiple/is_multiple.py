def is_multiple(n, m):
    """
    This function checks if a number n is a
    multiple of another number m.

    Args:
        n: The first integer.
        m: The second integer.

    Returns:
        True if n is a multiple of  m, otherwise False.

    """
    # Check if the divisor m, is zero
    if m == 0:
        return False

    # Check if there is no remainder after division
    return n % m == 0

# Example usage
print(is_multiple(10, 2))
print(is_multiple(13, 2))
print(is_multiple(6, 0))
