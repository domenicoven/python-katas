from string_calculator import StringCalculator
from random import *
import unittest


class StringCalculatorsTest(unittest.TestCase):
    def test_stringcalculator_emptylist_shouldreturn0(self):
        self.assertEqual(0,StringCalculator.add(""))

    def test_stringcalculator_listof1_shouldreturn1(self):
        self.assertEqual(1,StringCalculator.add("1"))

    def test_stringcalculator_listofN_shouldreturnN(self):
        rand = randint(1,999999)
        self.assertEqual(1,StringCalculator.add("1"))
        self.assertEqual(7,StringCalculator.add("7"))
        self.assertEqual(1234567,StringCalculator.add("1234567"))
        self.assertEqual(0,StringCalculator.add("0"))
        self.assertEqual(rand,StringCalculator.add(str(rand)))

    def test_stringcalculator_listoftwo_shouldreturnsumoftwo(self):
        self.assertEqual(StringCalculator.add("1,2"),3)
        self.assertEqual(StringCalculator.add("5,10"),15)
        self.assertEqual(StringCalculator.add("88,9"),88+9)
        rand1 = randint(1,999999)
        rand2 = randint(1,999999)
        self.assertEqual(StringCalculator.add('{0!s},{1!s}'.format(rand1,rand2)),rand1+rand2)
    
    def test_stringcalculator_listendingwithcomma_shouldnotbreak(self):
        self.assertEqual(StringCalculator.add("1,"),1)

    def test_stringcalculator_liststartingwithcomma_shouldnotbreak(self):
        self.assertEqual(StringCalculator.add(",8"),8)

    def test_stringcalculator_listwithmultipleemptycommas_shouldnotbreak(self):
        self.assertEqual(StringCalculator.add(",,,,8,,,,"),8)
        self.assertEqual(StringCalculator.add(",,3,,,,5,,"),8)
        self.assertEqual(StringCalculator.add("3,,,,,,5,,"),8)
        self.assertEqual(StringCalculator.add(",,3,,,,,,5"),8)
        self.assertEqual(StringCalculator.add("3,,,,,,,,5"),8)

    def test_stringcalculator_multiplenumber_shouldreturnsum(self):
        self.assertEqual(StringCalculator.add("1,2,3,4"),10)
        self.assertEqual(StringCalculator.add("2,2,2,2,2,2,2,2,2,2"),20)

    def test_stringcalculator_newlinesarelikecommas_shouldreturnsum(self):
        self.assertEqual(StringCalculator.add("1\n2,3"),6)
        self.assertEqual(StringCalculator.add("1\n,,"),1)

    def test_stringcalculator_changedelimiterintheformat_shouldreturnsum(self):
        self.assertEqual(StringCalculator.add("//;\n1;2"),3)

  
        
    


        
