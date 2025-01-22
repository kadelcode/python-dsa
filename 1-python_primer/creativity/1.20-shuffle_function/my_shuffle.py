import random

def my_shuffle(data):
    """
    Shuffle the elements of a list in place using the Fisher-Yates Shuffle algorithm
    and the randint function from the random module
    """
    for i in range(len(data) - 1, 0, -1):
        # Generate a random index from 0 to i (inclusive)
        j = random.randint(0, i)

        # Swap index of the current element with the randomly selected one
        data[i], data[j] = data[j], data[i]

    return data