from remove_punctuation import remove_punctuation

def test_remove_punctuation():

    # Test case 1: Simple sentence with punctuation
    assert remove_punctuation("Let's try, Mike.") == "Lets try Mike"