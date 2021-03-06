.. image:: https://travis-ci.org/sfaleron/LazyPrimes.svg?branch=master
    :target: https://travis-ci.org/sfaleron/LazyPrimesUnbounded prime iterator class for Python.

.. image:: https://codecov.io/gh/sfaleron/LazyPrimes/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/sfaleron/LazyPrimes

Based on Melissa O'Neill's paper, by way of incremental portings:

- `Python2 to Python3`_
- `Haskell to Python2`_
- `Original paper`_, with Haskell implementation

This implementation presents a slightly simplified interface (with input validation) with support for skipping ahead and setting an upper bound. Python versions 2.7 and 3.4 through 3.7 are supported. A test suite is included. Support for 2.6 and 3.0 though 3.3 is expected, but not verified.

Pure Python. There are `faster ways`_ to do this.

.. _Python2 to Python3: https://gist.github.com/sfaleron/8cabe55fa02e769661a6120be053f87a
.. _Haskell to Python2: http://logn.org/2009/07/lazy-primes-sieve-in-python.html
.. _Original paper: http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf

.. _faster ways: https://github.com/hickford/primesieve-python
