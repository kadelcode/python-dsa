from dot_product import dot_product

# Test Case 1: Simple case
a = [1, 2, 3]
b = [4, 5, 6]

expected = [4, 10, 18]
assert dot_product(a, b) == expected, f"Test Case 1 Failed: {dot_product(a, b)} != {expected}"


# Test Case 2: Arrays with negative values
a = [-1, -2, -3]
b = [4, -5, 6]
expected = [-4, 10, -18]
assert dot_product(a, b) == expected, f"Test Case 2 Failed: {dot_product(a, b)} != {expected}"

# Test Case 3: Arrays with zeros
a = [0, 0, 0]
b = [4, -5, 6]
expected = [0, 0, 0]
assert dot_product(a, b) == expected, f"Test Case 3 Failed: {dot_product(a, b)} != {expected}"

# Test Case 4: Empty arrays
a = []
b = []
expected = []
assert dot_product(a, b) == expected, f"Test Case 4 Failed: {dot_product(a, b)} != {expected}"

print("All tests passed!")