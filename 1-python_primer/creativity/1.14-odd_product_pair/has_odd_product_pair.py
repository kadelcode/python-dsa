def has_odd_product_pair(sequence):
    """
    Checks if a sequence of integers contains a distinct pair whose
    product is odd.
    
    Keyword arguments:
    sequence: A sequence of integers
    Return: True if such a pair exists, False otherwise
    """

    odd_count = 0
    for num in sequence:
        if num % 2 != 0: # Check if the number is odd
            odd_count += 1
            if odd_count >= 2: # If we find too odd numbers, we can stop the loop
                return True
    return False
    