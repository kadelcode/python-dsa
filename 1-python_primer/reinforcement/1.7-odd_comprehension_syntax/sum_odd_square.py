def sum_of_squares_of_odds(n):
    return sum(i**2 for i in range(1, n) if i % 2 != 0)

# Example usage
print(sum_of_squares_of_odds(10)) # 165
