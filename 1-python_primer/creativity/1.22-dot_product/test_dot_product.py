from dot_product import dot_product

# Test Case 1: Simple case
a = [1, 2, 3]
b = [4, 5, 6]

expected = [4, 10, 18]
assert dot_product(a, b) == expected, f"Test Case 1 Failed: {dot_product(a, b)} != {expected}"


print("All tests passed!")