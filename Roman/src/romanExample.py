'''
Created on Mar 19, 2012

@author: christom
'''

from roman import RomanNumerals

import sys

if __name__ == '__main__':
    
    numeral = RomanNumerals()
    
    print "Welcome to the Roman Numeral converter..."
    data = "invalid"
    
    while (data != 'q'):
        print "Would you like to use..."
        data = str(input("1) int2rom \n2) rom2int \nq) Quit example \n"))
        
        if (data == "1"):
            value = input("Please input an integer: ")
            roman = numeral.int2rom(value)
            print(str(value) + " in Roman Numeral is " + str(roman))
        elif (data == "2"):
            value = input("Please input an Roman numeral: ")
            integer = numeral.rom2int(value)
            print(str(value) + " in integer is " + str(integer))
        elif (data == "q"):
            print "See ya!"
        else:
            print "Unknown option: " + data
