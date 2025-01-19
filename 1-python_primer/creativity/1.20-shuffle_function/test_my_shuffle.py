from my_shuffle import my_shuffle

# Test the shuffle function
def test_my_shuffle():

    # Test 1: Ensures the shuffled list has the same elements as the original
    original = [1, 2, 3, 4, 5]

    shuffled = original[:]
    my_shuffle(shuffled)

    assert sorted(original) == sorted(shuffled), "The shuffled list don't have the same elements as the original"