'''
Created on Mar 19, 2012

@author: christom
'''
import unittest
from roman import RomanNumerals

class Test(unittest.TestCase):

    goodValues = ((1, 'I'),
                  (2, 'II'),
                  (50,'L' ),
                  (1226, 'MCCXXVI'))

    def testInt2Rom(self):
        numeral = RomanNumerals()
        for integer, roman in self.goodValues:
            value = numeral.int2rom(integer)
            self.assertEqual(value, roman, "Failed int2rom with value %integer" %integer)

    def testRom2Int(self):
        numeral = RomanNumerals()
        for integer, roman in self.goodValues:
            value = numeral.rom2int(roman)
            self.assertEqual(value, integer, "Failed rom2int with value %roman" %roman)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()