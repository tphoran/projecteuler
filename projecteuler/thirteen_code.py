class Thirteen(object):
    """
    Work out the first ten digits of the sum of the following one-hundred
    50-digit numbers.

    https://projecteuler.net/problem=13

    First two numbers:
    37107287533902102798797998220837590246510135740250
    46376937677490009712648124896970078050417018260538
    """

    def __init__(self, list_of_numbers_to_add, first_x_digits):
        self.list_of_numbers_to_add = list_of_numbers_to_add
        self.first_x_digits = first_x_digits

    def find_first_x_digits_in_a_number(self, number, x_digits):
        number_string = str(number)
        first_x_digits = int(number_string[:x_digits])
        return first_x_digits

    def solve(self):
        sum_of_list_of_numbers = sum(self.list_of_numbers_to_add)
        solution = self.find_first_x_digits_in_a_number(sum_of_list_of_numbers, self.first_x_digits)
        return solution


list_of_numbers_to_add = []
with open('/Users/tphoran/github/projecteuler/projecteuler/thirteen_input_number.txt') as input_file:
    for line in input_file:
        list_of_numbers_to_add.append(int(line))


thirteen = Thirteen(list_of_numbers_to_add, 10)
print(thirteen.solve())
