from math import factorial


class Twenty(object):
    """
    n! means n * (n - 1) * ... * 3 * 2 * 1

    For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    """

    def __init__(self, input_number):
        self.input_number = input_number

    def calculate_factorial(self, number):
        factorial_of_number = factorial(number)
        return factorial_of_number

    def sum_of_digits_in_number(self, number_to_add_digits):
        string_of_number = str(number_to_add_digits)
        sum_of_digits_in_number = 0
        for i in string_of_number:
            sum_of_digits_in_number += int(i)
        return sum_of_digits_in_number

    def solve(self):
        factorial = self.calculate_factorial(self.input_number)
        solution = self.sum_of_digits_in_number(factorial)
        return solution


input_number = 100
twenty = Twenty(input_number)
print(twenty.solve())
