
# Adapted from
# https://gist.github.com/sfaleron/8cabe55fa02e769661a6120be053f87a,
# which is a port to Python 3.x of the code in
# http://logn.org/2009/07/lazy-primes-sieve-in-python.html, which is a
# port to Python 2.x of the Haskell code in
# https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf!

# Now supporting Python v2.6 and v2.7

from __future__ import absolute_import

from .core import LazyPrimes

__all__ = ('LazyPrimes',)
