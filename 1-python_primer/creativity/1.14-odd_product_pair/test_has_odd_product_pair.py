test_cases = [
    ([2, 4, 6, 8], False),  # No odd numbers, so no odd product
    ([2, 4, 7, 9], True),   # Two odd numbers (7, 9), their product is odd
    ([1, 3, 5, 7], True),   # multiple odd numbers, at least one pair exists
    ([1, 2, 4, 6], False),  # Only one odd number, no pair exists
    ([1, 1], True),         # Two odd numbers (1, 1), their product is odd
    ([], False),            # Empty sequence, no pairs
    ([2], False),           # Single even number, no pairs
    ([3], False),           # Single odd number, no pairs
    ([1, 3, 2, 4, 5], True) # Three odd numbers (1, 3, 5), pairs exist
]

# Testing the function
for i, (sequence, expected) in enumerate(test_cases, 1):
    result = has_odd_product_pair(sequence)
    print(f"Test case {i}: Input: {sequence} | Expected: {expected} | Got: {result}")