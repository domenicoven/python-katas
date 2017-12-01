from string_calculator import StringCalculator, NegativeNotAllowedException
from random import *
import unittest


class StringCalculatorsTest(unittest.TestCase):
    def setUp(self):
        self.calculator= StringCalculator()
    
    def test_stringcalculator_emptylist_shouldreturn0(self):
        self.assertEqual(0,self.calculator.add(""))

    def test_stringcalculator_listof1_shouldreturn1(self):
        self.assertEqual(1,self.calculator.add("1"))

    def test_stringcalculator_listofN_shouldreturnN(self):
        rand = randint(1,1000)
        self.assertEqual(1,self.calculator.add("1"))
        self.assertEqual(7,self.calculator.add("7"))
        self.assertEqual(99,self.calculator.add("99"))
        self.assertEqual(0,self.calculator.add("0"))
        self.assertEqual(rand,self.calculator.add(str(rand)))

    def test_stringcalculator_listoftwo_shouldreturnsumoftwo(self):
        self.assertEqual(self.calculator.add("1,2"),3)
        self.assertEqual(self.calculator.add("5,10"),15)
        self.assertEqual(self.calculator.add("88,9"),88+9)
        rand1 = randint(1,1000)
        rand2 = randint(1,1000)
        self.assertEqual(self.calculator.add('{0!s},{1!s}'.format(rand1,rand2)),rand1+rand2)
    
    def test_stringcalculator_listendingwithcomma_shouldnotbreak(self):
        self.assertEqual(self.calculator.add("1,"),1)

    def test_stringcalculator_liststartingwithcomma_shouldnotbreak(self):
        self.assertEqual(self.calculator.add(",8"),8)

    def test_stringcalculator_listwithmultipleemptycommas_shouldnotbreak(self):
        self.assertEqual(self.calculator.add(",,,,8,,,,"),8)
        self.assertEqual(self.calculator.add(",,3,,,,5,,"),8)
        self.assertEqual(self.calculator.add("3,,,,,,5,,"),8)
        self.assertEqual(self.calculator.add(",,3,,,,,,5"),8)
        self.assertEqual(self.calculator.add("3,,,,,,,,5"),8)

    def test_stringcalculator_multiplenumber_shouldreturnsum(self):
        self.assertEqual(self.calculator.add("1,2,3,4"),10)
        self.assertEqual(self.calculator.add("2,2,2,2,2,2,2,2,2,2"),20)

    def test_stringcalculator_newlinesarelikecommas_shouldreturnsum(self):
        self.assertEqual(self.calculator.add("1\n2,3"),6)
        self.assertEqual(self.calculator.add("1\n,,"),1)

    def test_stringcalculator_changedelimiterintheformat_shouldreturnsum(self):
        self.assertEqual(self.calculator.add("//;\n1;2"),3)
        self.assertEqual(self.calculator.add("//kk\n1kk2"),3)
        self.assertEqual(self.calculator.add("///\n1/2"),3)

    def test_stringcalculator_passingnegativenumber_shouldthrowexception(self):
        with self.assertRaises(NegativeNotAllowedException) as ctx:
            self.calculator.add("1,-2")
        exc = ctx.exception
        self.assertEqual("negatives not allowed: -2",str(exc))    


    def test_stringcalculator_numberbiggerthan1000_shouldbeignore(self):
        self.assertEqual(self.calculator.add("1001,1"),1)
        self.assertEqual(self.calculator.add("1000,1"),1001)
    


        
