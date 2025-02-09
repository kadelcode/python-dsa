def norm(v, p=2):
    """
    Computes the p-norm of a vector v. If p is not provided, it defaults to
    the Euclidean norm

    Parameters:
        v (list): A list of numbers representing the vector.
        p (int or float, optional): The order of the norm. Defaults to 2
        (Euclidean norm)

    Returns:
        float: The computed p-norm of the vector.
    """
    return sum(abs(x) ** p for x in v) ** (1 / p)

# Example usage:
v = [4, 3]
print(norm(v)) # Euclidean norm (default p=2), should return 5
print(norm(v, 3)) # 3-norm example

# Test cases:
assert round(norm([3, 4]), 6) == 5.0 # Euclidean norm of (3, 4)
assert round(norm([1, 1, 1], 1), 6) == 3.0 # 1-norm (Manhattan norm)
assert round(norm([0, 0, 0]), 6) == 0.0 # Zero vector norm
assert round(norm([-3, -4]), 6) == 5.0 # Euclidean norm with negative values
assert round(norm([2, 3, 4], 3), 6) == round((2**3 + 3**3 + 4**3) ** (1/3), 6) # 3-norm test