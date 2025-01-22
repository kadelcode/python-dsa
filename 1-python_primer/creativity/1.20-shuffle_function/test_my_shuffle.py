from my_shuffle import my_shuffle

# Test the shuffle function
def test_my_shuffle():

    # Test 1: Ensures the shuffled list has the same elements as the original
    original = [1, 2, 3, 4, 5]

    shuffled = original[:]
    my_shuffle(shuffled)

    assert sorted(original) == sorted(shuffled), "The shuffled list don't have the same elements as the original"

    
    # Test 2: Ensure the function changes the order of elements
    # Note: There's a very small chance the shuffled list could be the same
    # as the original
    no_change_count = 0

    # Run multiple trials to reduce the impact of randomness
    for _ in range(100):
        shuffled = original[:]
        my_shuffle(shuffled)

        if original == shuffled:
            no_change_count += 1
    assert no_change_count < 5, "The shuffle function rarely changes the order of elements"


    # Test 3: Handle edge cases
    empty_list = []
    my_shuffle(empty_list) # Should not raise an error
    assert empty_list == [], "The shuffle function failed on an empty list."

    single_element_list = [42]
    my_shuffle(single_element_list) # Should not raise an error
    assert single_element_list == [42], "The shuffle function failed on a single-element list"


    # Test 4: Repeated calls produce different results
    shuffled1 = original[:]
    shuffled2 = original[:]
    my_shuffle(shuffled1)
    my_shuffle(shuffled2)

    assert shuffled1 != shuffled2 or len(set(tuple(my_shuffle(original[:])) for _ in range(10))) > 1, (
        "Repeated shuffles produced the same"
        )

    print("All tests passed!")

# Run the test function
test_my_shuffle()