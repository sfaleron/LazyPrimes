
from lazyprimes.tests.testsyms import *

def test_constructor_valid_k():
    g = LazyPrimes(k = 0)
    assert next(g) == 2

    g = LazyPrimes(k = 1)
    assert next(g) == 2

    g = LazyPrimes(k = 2)
    assert next(g) == 2

def test_constructor_invalid_k():
    with pytest.raises(ValueError):
        g = LazyPrimes(k = -0.0)

    with pytest.raises(ValueError):
        g = LazyPrimes(k = 0.0)

    with pytest.raises(ValueError):
        g = LazyPrimes(k = -0.2)

    with pytest.raises(ValueError):
        g = LazyPrimes(k = -1)

    with pytest.raises(ValueError):
        g = LazyPrimes(k = -2)

    with pytest.raises(ValueError):
        g = LazyPrimes(k = 1.23)

    with pytest.raises(ValueError):
        g = LazyPrimes(k = -2.34)

def test_constructor_valid_lowerBnd_valid():
    g = LazyPrimes(lowerBnd=0)
    assert next(g) == 2

    g = LazyPrimes(lowerBnd=0.0)
    assert next(g) == 2

    g = LazyPrimes(lowerBnd=-1)
    assert next(g) == 2

    g = LazyPrimes(lowerBnd=-0.2)
    assert next(g) == 2

    g = LazyPrimes(lowerBnd=-1.23)
    assert next(g) == 2

    g = LazyPrimes(lowerBnd=0.4)
    assert next(g) == 2

    g = LazyPrimes(lowerBnd=0.8)
    assert next(g) == 2

    g = LazyPrimes(lowerBnd=1)
    assert next(g) == 2

    g = LazyPrimes(lowerBnd=1.0)
    assert next(g) == 2

    g = LazyPrimes(lowerBnd=2.0)
    assert next(g) == 2

    g = LazyPrimes(lowerBnd=2.01)
    assert next(g) == 3

    g = LazyPrimes(lowerBnd=2.99)
    assert next(g) == 3

    g = LazyPrimes(lowerBnd=2.01)
    assert next(g) == 3

    g = LazyPrimes(lowerBnd=3)
    assert next(g) == 3

    g = LazyPrimes(lowerBnd=3.0)
    assert next(g) == 3

    g = LazyPrimes(lowerBnd=3+1e-6)
    assert next(g) == 5

    g = LazyPrimes(lowerBnd=float('-inf'))
    assert next(g) == 2

    with pytest.raises(StopIteration):
        g = LazyPrimes(lowerBnd=float('inf'))
        next(g)

def test_constructor_valid_lowerBnd_invalid():
    with pytest.raises(ValueError):
        g = LazyPrimes(lowerBnd=float('nan'))

    with pytest.raises(ValueError):
        g = LazyPrimes(lowerBnd='foo')

    with pytest.raises(ValueError):
        g = LazyPrimes(lowerBnd=[])

    with pytest.raises(ValueError):
        g = LazyPrimes(lowerBnd=object)

    with pytest.raises(ValueError):
        g = LazyPrimes(lowerBnd=complex(0,1))

    with pytest.raises(ValueError):
        g = LazyPrimes(lowerBnd=complex(1,1))
