
# Adapted from
# https://gist.github.com/sfaleron/8cabe55fa02e769661a6120be053f87a,
# which is a port to Python 3.x of the code in
# http://logn.org/2009/07/lazy-primes-sieve-in-python.html, which is a
# port to Python 2.x of the Haskell code in
# https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf!

import itertools

from . _inner import primes

class LazyPrimes(object):
    def __init__(self, k=5, skipto=None):
        self._it = primes(k)

        if skipto:
           self.skipto(skipto)

    __next__     = lambda self: next(self._it)

    __iter__     = lambda self: self._it

    def taken(self, n):
        """Iterate the next n primes"""
        return itertools.islice(self, n)

    def takeuntil(self, n):
        """Iterate through primes less than or equal to n"""
        return itertools.takewhile(lambda x: x<=n, self)

    def skipto(self, n):
        """Begin iterating at first prime greater than or equal to n"""
        self._it = itertools.dropwhile(lambda x: x<n, self)
