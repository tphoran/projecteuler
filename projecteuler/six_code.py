import numpy as np


class Six(object):
    """
    The sum of the squares of the first ten natural numbers is, 385

    The square of the sum of the first ten natural numbers is, 3025

    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
    385-3025=2640

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the
    sum.
    """

    def __init__(self, sequence):
        self.sequence = sequence

    def list_of_number_squared_and_summed(self, sequence):
        array_sequence = np.array(sequence)
        array_squared = array_sequence**2
        array_squared_and_summed = sum(array_squared)
        return array_squared_and_summed

    def list_of_numbers_summed_and_squared(self, sequence):
        array_sequence = np.array(sequence)
        array_summed = sum(array_sequence)
        array_summed_and_squared = array_summed**2
        return array_summed_and_squared

    def solve(self):
        square_and_summed = self.list_of_number_squared_and_summed(self.sequence)
        summed_and_squared = self.list_of_numbers_summed_and_squared(self.sequence)
        output = summed_and_squared - square_and_summed
        return output


one_to_one_hundred = list(range(1, 101))
six = Six(one_to_one_hundred)
print six.solve()