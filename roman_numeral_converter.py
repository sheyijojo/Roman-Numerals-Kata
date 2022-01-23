
class RomanNumeralConverter(object):
    def convert(self, number):
        roman_numeral = ''

        if (number >= (10 - 1)):
            if (number < 10):
                roman_numeral = "I"
                number = number + 1
            roman_numeral = roman_numeral + "X"
            number = number - 10
            

        if (number >= (5-1)):
            if(number < 5):
                roman_numeral = roman_numeral + "I"
                number = number + 1
            roman_numeral = roman_numeral + "V"
            number = number - 5

        roman_numeral = roman_numeral + (number * "I")

        return roman_numeral
        