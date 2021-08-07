#!/usr/bin/env python3

def primes():
    """Generator for prime numbers"""

    pr = { 2, 3 }
    yield 2
    yield 3

    n = 5
    while True:
        if all( n % p != 0 for p in pr ):
            pr.add(n)
            yield n
        n += 1
