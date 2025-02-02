We provided three different implementations of a generator that computes factors of a given integer. The third of those implementations:
```
def factors(n): # generator that computes factors
    k=1
    while k * k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k    
        k += 1
    if k * k == n: # special case if n is perfect square
        yield k
```
was the most efficient, but we noted that it did not yield the factors in increasing order.

- Modify the generator so that it reports factors in increasing order, while maintaining its general performance advantages.