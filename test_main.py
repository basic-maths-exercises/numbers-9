import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_prime_decomposition(self) :
        for N in range(100) : 
          i, student = 2, primeDecomposition( N )
          while i*i <= N :
            if N%i == 0 : 
               N = N / i
               found = False 
               for d in student : 
                 if d==i : found = True
               self.assertTrue( found, "your function is not working correctly" )
            else : 
               i = i + 1 
          if N>1 : 
            found = False
            for d in student : 
               if d==N : found = True
            self.assertTrue( found, "your function is not working correctly" )
