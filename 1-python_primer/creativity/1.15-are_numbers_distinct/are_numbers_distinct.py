def are_numbers_distinct(seqeunce):
    """
    Determines if all numbers in a sequence are distinct.
    
    :param sequence: A sequence of numbers
    :return: True if all numbers are distinct, False otherwise
    """

    return len(seqeunce) == len(set(seqeunce))
    