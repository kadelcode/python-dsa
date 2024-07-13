def sum_of_odd_squares(n):
    """
    This function computes the sum of squares of
    odd numbers less than n.

    Args:
        n: The number

    Return:
        sum of squares of odd numbers
    """
    odd_squares = []

    for i in range(1, n):
        if i & 1 != 0:
            odd_squares.append(i**2)

    return sum(odd_squares)

# Example usage
print(sum_of_odd_squares(7))
