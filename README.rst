Unbounded prime iterator class for Python.

Based on Melissa O'Neill's paper, by way of incremental translations:

- `Python2 to Python3`_
- `Haskell to Python2`_
- `Original paper`_, with Haskell implementation

This implementation presents a slightly simplified interface with support for skipping ahead and setting an upper bound. A test suite is included, and support for pickling is planned.

Pure Python. There are `faster ways`_ to do this.

.. _Python2 to Python3: https://gist.github.com/sfaleron/8cabe55fa02e769661a6120be053f87a
.. _Haskell to Python2: http://logn.org/2009/07/lazy-primes-sieve-in-python.html
.. _Original paper: http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf

-- _faster ways: https://github.com/hickford/primesieve-python