def count_vowels(input_string):
    """Counts the number of vowels (a, e, i, o, u) in a string.

    Args:
        input_string: The string to check.
    Returns:
        The number of vowels in the string.
    """
    vowels = "aeiouAEIOU"

    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count