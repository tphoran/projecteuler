class Seventeen(object):
    """
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
    are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
    how many letters would be used?
    """

    def __init__(self, max_number):
        self.max_number = max_number
        self.number_dictionary = {1: 'one',
                                  2: 'two',
                                  3: 'three',
                                  4: 'four',
                                  5: 'five',
                                  6: 'six',
                                  7: 'seven',
                                  8: 'eight',
                                  9: 'nine',
                                  10: 'ten',
                                  11: 'eleven',
                                  12: 'twelve',
                                  13: 'thirteen',
                                  14: 'fourteen',
                                  15: 'fifteen',
                                  16: 'sixteen',
                                  17: 'seventeen',
                                  18: 'eighteen',
                                  19: 'nineteen',
                                  20: 'twenty',
                                  30: 'thirty',
                                  40: 'forty',
                                  50: 'fifty',
                                  60: 'sixty',
                                  70: 'seventy',
                                  80: 'eighty',
                                  90: 'ninety',
                                  }

    def write_given_number(self, number):
        """
        Mucho opportunity to refactor
        """
        written_number = str()
        if number < 20:
            written_number += self.number_dictionary[number]
        elif number >= 20 and number < 100:
            if number % 10 == 0:
                written_number += self.number_dictionary[number]
            else:
                units = number % 10
                tens = number - units
                written_number = self.number_dictionary[tens] + self.number_dictionary[units]
        elif number >= 100 and number < 1000:
            if number % 100 == 0:
                hundreds = number / 100
                written_number += self.number_dictionary[hundreds]+'hundred'
            else:
                hundreds = number // 100
                remainder = number % 100
                if remainder < 20:
                    written_number += self.number_dictionary[hundreds]+'hundredand' + \
                                      self.number_dictionary[remainder]
                elif remainder >= 20:
                    if remainder % 10 == 0:
                        written_number += self.number_dictionary[hundreds]+'hundredand' + \
                                          self.number_dictionary[remainder]
                    else:
                        units = remainder % 10
                        tens = remainder - units
                        written_number = self.number_dictionary[hundreds]+'hundredand' +\
                                         self.number_dictionary[tens] + \
                                         self.number_dictionary[units]
        elif number == 1000:
            written_number = 'onethousand'
        return written_number

    def create_string_of_number_words(self, max_number):
        string_of_numbers = str()
        for i in range(1, max_number+1):
            string_of_numbers += self.write_given_number(i)
        return string_of_numbers

    def solve(self):
        string_of_numbers = self.create_string_of_number_words(self.max_number)
        return len(string_of_numbers)


seventeen = Seventeen(1000)
print(seventeen.solve())


