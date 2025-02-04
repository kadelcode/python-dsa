def factors(n): # generator that computes factors in increasing order
    k = 1
    large_factors = [] # List to store larger factors

    while k * k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            if k != n // k: # Avoid duplicate for perfect squares
                large_factors.append(n // k)

        k += 1
    if k * k == n:
        yield k
    while large_factors:
        yield large_factors.pop() # Yield larger factors in order