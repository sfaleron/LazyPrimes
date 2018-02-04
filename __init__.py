
# Adapted from
# https://gist.github.com/sfaleron/8cabe55fa02e769661a6120be053f87a,
# which is a port to Python 3.x of the code in
# http://logn.org/2009/07/lazy-primes-sieve-in-python.html, which is a
# port to Python 2.x of the Haskell code in
# https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf!

import itertools

from . _inner import primes

import math

from numbers import Integral, Real

# accepts plus/minus infinity
# complex values with zero imaginary part are not
def realTest(n):
    if not isinstance(n, Real):
        return False

    if math.isnan(n):
        return False

    return True

class LazyPrimes(object):
    def __init__(self, k=5, lowerBnd=None, upperBnd=None):

        # itertools.islice() requires that k is valid, but
        # that's an implementation detail, not an interface
        if not isinstance(k, Integral) or k<0:
            raise ValueError('k must be a non-negative integer.')

        self._it = primes(k)

        if not lowerBnd is None:
           if not realTest(lowerBnd):
               raise ValueError('lowerBnd must be a real number.')

           self.skipto(lowerBnd)

        if not upperBnd is None:
           if not realTest(upperBnd):
               raise ValueError('upperBnd must be a real number.')

           self.takeuntil(upperBnd)

    __next__     = lambda self: next(self._it)

    __iter__     = lambda self: self._it

    def taken(self, n):
        """Iterate the next n primes"""
        return itertools.islice(self, n)

    def takeuntil(self, upperBnd):
        """Iterate through primes less than or equal to upperBnd"""

        if math.isinf(upperBnd):
            if upperBnd>0:
                return self

        return itertools.takewhile(lambda x: x<=upperBnd, self)

    def skipto(self, lowerBnd):
        """Begin iterating at the next prime greater than or equal to lowerBnd.
           Accepts plus or minus infinity: Minus: no change; Plus: iterator becomes empty."""

        if math.isinf(lowerBnd):
            if lowerBnd>0:
                self._it = iter('')

        else:
            self._it = itertools.dropwhile(lambda x: x<lowerBnd, self)

__all__ = ('LazyPrimes',)
