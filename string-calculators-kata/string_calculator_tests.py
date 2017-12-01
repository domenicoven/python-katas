from string_calculator import StringCalculator
import unittest


class StringCalculatorsTest(unittest.TestCase):
    def test_stringcalculator_emptylist_shouldreturn0(self):
        
        self.assertEqual(0,StringCalculator.add(""))
