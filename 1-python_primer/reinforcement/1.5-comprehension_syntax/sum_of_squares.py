def sum_of_squares(n):
    """
    This function computes the sum of squares
    of all positive integers smaller than n
    
    Args:
        n: The integer

    Return:
        The sum of squares
    """
    return sum([i * i for i in range(1, n)])

# Example usage
if __name__ == '__main__':
    print(sum_of_squares(4))
