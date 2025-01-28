import string

def remove_punctuation(s):
    # Use string.punctuation to get all punctuation characters
    return ''.join(char for char in s if char not in string.punctuation)