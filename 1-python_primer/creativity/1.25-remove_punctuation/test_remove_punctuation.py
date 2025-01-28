from remove_punctuation import remove_punctuation

def test_remove_punctuation():

    # Test case 1: Simple sentence with punctuation
    assert remove_punctuation("Let's try, Mike.") == "Lets try Mike"

    # Test case 2: Sentence with multiple types of punctuation
    assert remove_punctuation("Hello, world! How's it going?") == "Hello world Hows it going"

    # Test case 3: String with no punctuation
    assert remove_punctuation("No punctuation here") == "No punctuation here"

    # Test case 4: String with only punctuation
    assert remove_punctuation("!!!???,,,...") == ""
    
    # Test case 5: Empty string
    assert remove_punctuation("") == ""

    # Test case 6: Sentence with numbers and punctuation
    assert remove_punctuation("123! ABC# 456$ DEF&") == "123 ABC 456 DEF"

    # Test case 7: String with special characters not in punctuation
    assert remove_punctuation("Look at this @ symbol!") == "Look at this  symbol"

    print("All test cases passed!")

# Run the test cases
test_remove_punctuation()