class Sixteen(object):
    """
    215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
    """

    def __init__(self, power):
        self.power = power

    def sum_of_digits_2_to_x_power(self, power):
        number = 2**power
        str_number = str(number)
        sum_of_digits = 0
        for i in str_number:
            sum_of_digits += int(i)
        return sum_of_digits

    def solve(self):
        solution = self.sum_of_digits_2_to_x_power(self.power)
        return solution


sixteen = Sixteen(1000)
print(sixteen.solve())
