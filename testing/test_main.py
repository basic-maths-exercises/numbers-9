try:
    from AssCheck import funcchecks as fc
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AssCheck"])
    from AssCheck import funcchecks as fc

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_prime_decomposition(self) :
        inputs, outputs = [], []
        for N in range(100) :
          inputs.append((N,)) 
          i, primes = 2, set([])
          while i*i <= N :
            if N%i == 0 : 
               N = N / i
               primes.add(i)
            else : 
               i = i + 1 
          if N>1 : primes.add(N)
          outputs.append(primes)
        assert( fc.check_func( 'primeDecomposition', inputs, outputs ) )
