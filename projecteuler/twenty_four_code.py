from itertools import permutations


class TwentyFour(object):
    """
    A permutation is an ordered arrangement of objects. For example, 3124 is
    one possible permutation of the digits 1, 2, 3 and 4. If all of the
    permutations are listed numerically or alphabetically, we call it
    lexicographic order. The lexicographic permutations of 0, 1 and 2
    are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
    4, 5, 6, 7, 8 and 9?
    """
    def __init__(self, list_numbers_for_permutation, permutation_to_return):
        self.list_numbers_for_permutation = list_numbers_for_permutation
        self.permutation_to_return = permutation_to_return

    def permutation_iterator(self, list):
        return permutations(list)

    def solve(self):
        iterator = self.permutation_iterator(self.list_numbers_for_permutation)
        current_permutation = 1
        while current_permutation <= self.permutation_to_return:
            out = next(iterator)
            current_permutation += 1
        return out


list_numbers_for_permutation = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation_to_return = 1000000

twenty_four = TwentyFour(list_numbers_for_permutation, permutation_to_return)
print(twenty_four.solve())
