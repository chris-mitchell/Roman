'''
Created on Mar 19, 2012

@author: christom
'''
class RomanNumerals(object):
    '''
    classdocs
    '''
    import re
    
    class RomanError(Exception): pass
    class NotIntegerError(RomanError): pass
    class OutOfRangeError(RomanError): pass
    class InvalidRomanNUmeralError(RomanError): pass
    
    '''
    Map to store possible roman numeral and their integer values
    '''
    roman2intMap = (('M',  1000),
       ('CM', 900),
       ('D',  500),
       ('CD', 400),
       ('C',  100),
       ('XC', 90),
       ('L',  50),
       ('XL', 40),
       ('X',  10),
       ('IX', 9),
       ('V',  5),
       ('IV', 4),
       ('I',  1))


    '''
    Utilize regex to find matching patterns
    '''
    romanNumeralPattern = re.compile('''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    ''' ,re.VERBOSE)


    def __init__(self):
        '''
        Constructor
        '''
        
    def int2rom(self, n):    
        
        if not (0 < n < 4000):
            raise self.OutOfRangeError, "Valid Roman Numerals must be 0 < n < 4000"
        
        if int(n) <> n:
            raise self.NotIntegerError, "Attempting to convert a non-integer value!"
        
        roman = ""
        '''
        Uses a greedy algo to grab the largest value that we can, cycling back to get the next best, etc
        '''
        for numeral, integer in self.roman2intMap:
                while n >= integer:
                    roman += numeral
                    n -= integer
        return roman
    
    def rom2int(self, rom):
        if not rom:
            raise self.InvalidRomanNumeralError, "Input must contains a string of valid Roman numerals"
        if not self.romanNumeralPattern.search(rom):
            raise self.InvalidRomanNumeralError, "Invalid Roman numeral: %rom" %rom
        
        result = 0
        index = 0
        
        for numeral, integer in self.roman2intMap:
            while rom[index:index+len(numeral)] == numeral:
                result += integer
                index += len(numeral)
        
        return result