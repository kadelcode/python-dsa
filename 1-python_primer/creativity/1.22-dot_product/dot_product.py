def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Array a and b must have the same length")

    # Compute the dot product
    c = [a[i] * b[i] for i in range(len(a))]

    return c

# Example usage
a = [1, 2, 3]
b = [4, 5, 6]

result = dot_product(a, b)
print("Dot product:", result)