

class Eight(object):
    """
    The four adjacent digits in the 1000-digit number that have the greatest
    product are 9 * 9 * 8 * 9 = 5832.

    Find the thirteen adjacent digits in the 1000-digit number that have the
    greatest product. What is the value of this product?
    """

    def __init__(self, input_number, x_long):
        self.input_number = input_number
        self.x_long = x_long

    def find_high_product_of_x_adjacent_numbers_in_input_number(self, input_number, x_long):
        high_product = 0
        for i in range(len(input_number)-x_long):
            set = input_number[i:i+x_long]
            current_product = 1
            for e in set:
                current_product *= int(e)
            if current_product >= high_product:
                high_product = current_product
        return high_product

    def solve(self):
        high_product = self.find_high_product_of_x_adjacent_numbers_in_input_number(self.input_number, self.x_long)
        return high_product


input_number = str()
with open('/Users/tphoran/github/projecteuler/projecteuler/eight_input_number.txt') as input_file:
    for line in input_file:
        input_number += line

test = Eight(input_number, 13)

print(test.solve())
