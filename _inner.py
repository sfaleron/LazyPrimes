
# Adapted from
# https://gist.github.com/sfaleron/8cabe55fa02e769661a6120be053f87a,
# which is a port to Python 3.x of the code in
# http://logn.org/2009/07/lazy-primes-sieve-in-python.html, which is a
# port to Python 2.x of the Haskell code in
# https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf!

import heapq
import operator
import itertools

from functools import reduce

class Item(int):
    def __new__(cls, value, it):
        o = super().__new__(cls, value)
        o._it = it

        return o

    __next__ = lambda self: next(self._it)

def primes(k):
    # Generate primes with the sieve and wheel factorization, which filters
    # multiples of the first k primes.
    smallprimes = list(itertools.islice(sieve(itertools.count(2)), k + 1))
    factors     = smallprimes[:-1]
    next        = smallprimes[-1]

    return itertools.chain(factors, sieve(spin(factors, next)))

def sieve(xs):
    # Generate the prime numbers, given an iterable of candidate numbers.
    # Cross off multiples of prime numbers incrementally using iterators.
    table = []
    while True:
        candidate = next(xs)
        if table == [] or candidate < table[0]:
            yield candidate
            xs, ys = itertools.tee(xs)
            timesx = (lambda x: lambda y: x*y)(candidate)
            heapq.heappush(table, Item(candidate**2, map(timesx, ys)))
        else:
            while table[0] <= candidate:
                heapq.heapreplace(table, Item(next(table[0]), table[0]))

def spin(factors, next):
    # Generate candidates by making a wheel and cycling through it.
    for gap in itertools.cycle(wheel(factors, next)):
        yield next
        next += gap

def wheel(factors, next):
    # Generate the distances between numbers not divisible by a list of small
    # primes, from the next prime up to the product of the list.
    circumference = reduce(operator.mul, factors)

    prev  = next
    next += 1

    end = next + circumference

    while next < end:
        if not any(next % factor == 0 for factor in factors):
            yield next - prev
            prev = next

        next += 1
