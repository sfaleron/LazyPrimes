
import heapq
import operator
import itertools

from functools import reduce

if hasattr(itertools, 'imap'):
    imap = itertools.imap
else:
    imap = map

class Item(int):
    def __new__(cls, value, it):
        o = int.__new__(cls, value)
        o._it = it

        return o

    __next__ = lambda self: next(self._it)

    next     = __next__

def primes(k):
    # Generate primes with the sieve and wheel factorization, which filters
    # multiples of the first k primes.
    if k == 0:
        return baresieve()

    else:
        firstprimes = list(itertools.islice(baresieve(), k + 1))
        smallprimes = firstprimes[:-1]
        nextprime   = firstprimes[-1]

        return itertools.chain(smallprimes, sieve(spin(smallprimes, nextprime)))

def baresieve():
    return sieve(itertools.count(2))

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
            heapq.heappush(table, Item(candidate**2, imap(timesx, ys)))
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
