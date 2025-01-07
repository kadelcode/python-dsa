def reverse_list(input_list):
    """This function reverse a list
    
    Keyword arguments:
    input_list -- The sequence to reverse
    Return: The reversed list
    """
    
    # Creeate an empty list to store reversed elements
    reversed_list = []

    # Loop from the end of the list to the start
    for i in range(len(input_list) - 1, -1, -1):
        # Add the current element to the new list
        reversed_list.append(input_list[i])

    # Return the reversed list
    return reversed_list