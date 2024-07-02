def minmax(data):
    """
    This function finds the minimum and maximum values
    in a sequence.

    Args:
        data: A sequence of numbers.

    Returns:
        A tuple of length two containing the minimum and
        maximum values.

    """
    # check if no number is passed to the function
    if len(data) == 0:
        raise ValueError("Empty sequence")

    # Initialize minimum and maximum
    minimum, maximum = data[0], data[0]

    # Iterate through the sequence
    for num in data[1:]:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum

if __name__ == '__main__':
    # Example usage
    data = [2, 6, 3, 10, 1]
    min_value, max_value = minmax(data)
    print(f"Minimum: {min_value}, Maximum: {max_value}")
