from remove_punctuation import remove_punctuation

def test_remove_punctuation():

    # Test case 1: Simple sentence with punctuation
    assert remove_punctuation("Let's try, Mike.") == "Lets try Mike"

    # Test case 2: Sentence with multiple types of punctuation
    assert remove_punctuation("Hello, world! How's it going?") == "Hello world Hows it going"