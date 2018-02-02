
import pytest

import os.path as osp

from lazyprimes import LazyPrimes

def getKnownPrimes(memo=[]):
    if not memo:
        fn = osp.join(osp.dirname(__file__), 'knownprimes.dat')
        knownprimes = tuple(map(int, open(fn, 'r').readlines()))
        memo.append(knownprimes)

    return tuple(memo[0])
