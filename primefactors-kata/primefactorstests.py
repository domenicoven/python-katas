from primefactors import primefactors
import unittest

class PrimeFactorsTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual([], primefactors(1))

    def test_2(self):
        self.assertEqual([2], primefactors(2))

    def test_3(self):
        self.assertEqual([3], primefactors(3))

    def test_4(self):
        self.assertEqual([2,2], primefactors(4))

    def test_5(self):
        self.assertEqual([5], primefactors(5))

    def test_6(self):
        self.assertEqual([2,3], primefactors(6))

    def test_7(self):
        self.assertEqual([7], primefactors(7))

    def test_8(self):
        self.assertEqual([2,2,2], primefactors(8))

    def test_9(self):
        self.assertEqual([3,3], primefactors(9))
    
    def test_25(self):
        self.assertEqual([5,5], primefactors(25))
        
    def test_complex(self):
        self.assertEqual([5,5,7,7,11,19], primefactors(19*11*7*7*5*5))
        self.assertEqual([71, 73, 79, 83, 89, 97], 
            primefactors(71*73*79*83*89*97))


    
        