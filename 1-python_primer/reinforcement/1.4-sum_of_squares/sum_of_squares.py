def sum_of_squares(n):
    """
    This function calculates the sum of squares of
    all positive integers less than n

    Args:
        n: The positive integer.

    Returns:
        The sum of squares of all positive integers
        smaller than n.
    """
    if n <= 1:
        return n
    else:
        # Calculate sum of squares using formula
        return (n - 1) * n * (2 * n - 1) // 6

# Example usage
if __name__ == '__main__':
    number = 5
    result = sum_of_squares(number)
    print(f"The sum of squares of all positive integers smaller than {number} is {result}")
