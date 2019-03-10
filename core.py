
from __future__ import absolute_import

from    numbers import Integral, Real

import  itertools
import  math

from . _inner import primes

# accepts plus/minus infinity
# complex values with zero imaginary part are not
def realTest(n):
    if not isinstance(n, Real):
        return False

    if math.isnan(n):
        return False

    return True

class LazyPrimes(object):
    """All methods, except copy(), update internal state.
    They return self to support method chains. Once added,
    these constraints will always be in effect."""

    def copy(self):
        a, b = itertools.tee(self)

        dupe = LazyPrimes()
        dupe._it = a
        self._it = b

        return dupe

    def __init__(self, k=5, lowerBnd=None, upperBnd=None, n=None):
        # itertools.islice() requires that k is valid, but
        # that's an implementation detail, not an interface
        if not isinstance(k, Integral) or k<0:
            raise ValueError('k must be a non-negative integer.')

        self._it = primes(k)

        if not lowerBnd is None:
            self.skipto(lowerBnd)

        if not upperBnd is None:
            self.takeuntil(upperBnd)

        if not n is None:
            self.taken(n)

    __iter__ = lambda self: self._it

    __next__ = lambda self: next(self._it)
    next     = __next__

    def skipto(self, lowerBnd):
        """Begin iterating at the next prime greater than or equal to lowerBnd.

        Accepts plus or minus infinity: Minus: no change; Plus: iterator
        becomes empty."""

        if not realTest(lowerBnd):
            raise ValueError('lowerBnd must be a real number.')

        if math.isinf(lowerBnd):
            if lowerBnd>0:
                self._it = iter([])

        else:
            self._it = itertools.dropwhile(lambda x: x<lowerBnd, self)

        return self

    def takeuntil(self, upperBnd):
        """End iterating at the next prime greater than or equal to upperBnd.

        Accepts plus or minus infinity: Plus: no change; Minus: iterator
        becomes empty."""

        if not realTest(upperBnd):
            raise ValueError('upperBnd must be a real number.')

        if math.isinf(upperBnd):
            if upperBnd>0:
                return self

        self._it = itertools.takewhile(lambda x: x<=upperBnd, self)

        return self

    def taken(self, n):
        """Iterate the next n primes"""

        if not isinstance(n, Integral) or n<0:
            raise ValueError('n must be a non-negative integer.')

        self._it = itertools.islice(self, n)

        return self
