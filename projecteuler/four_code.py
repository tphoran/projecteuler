
import itertools


class Four(object):
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
    is 9009 = 91 * 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """

    def __init__(self, digits):
        self.digits = digits

    def is_palindrome(self, n):
        string_of_number = str(n)
        length_of_number_string = len(string_of_number)
        for i in range(0, length_of_number_string/2):
            if string_of_number[i] != string_of_number[-i-1]:
                return False
        return True

    def solve(self):
        first_number = 10 ** (self.digits - 1)
        last_number = 10 ** self.digits
        list_of_numbers = list(range(first_number, last_number))
        largest_palindrome = None
        for combinations in itertools.combinations(list_of_numbers, 2):
            product = combinations[0] * combinations[1]
            if self.is_palindrome(product) and product > largest_palindrome:
                print product,
                print combinations
                largest_palindrome = product
        return largest_palindrome


four = Four(3)
print four.solve()
