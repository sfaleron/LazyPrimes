
import os.path as osp

from .. import LazyPrimes

def getKnownPrimes(memo=[]):
    if not memo:
        fn = osp.join(osp.dirname(__file__), 'knownprimes.dat')
        knownprimes = tuple(map(int, open(fn, 'r').readlines()))
        memo += knownprimes

    return tuple(memo)

def test_validate():
    assert getKnownPrimes() == tuple(LazyPrimes(upperBnd=1000))
