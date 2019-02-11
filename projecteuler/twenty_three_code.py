class TwentyThree(object):
    """
    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors
    of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number.

    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
    number that can be written as the sum of two abundant numbers is 24. By
    mathematical analysis, it can be shown that all integers greater than 28123
    can be written as the sum of two abundant numbers. However, this upper
    limit cannot be reduced any further by analysis even though it is known
    that the greatest number that cannot be expressed as the sum of two
    abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.
    """
    def __init__(self, max_number):
        self.max_number = max_number

    def find_proper_divisors_of_number(self, number):
        proper_divisors = [1, ]
        for i in range(2, number//2 + 1):
            if number%i == 0:
                proper_divisors.append(i)
        return sum(proper_divisors)

    def number_is_abundant_number(self, number):
        sum_of_proper_divisors = self.find_proper_divisors_of_number(number)
        if sum_of_proper_divisors > number:
            return True
        else:
            return False

    def find_list_of_abundant_numbers_between_a_range(self, start_number, stop_number):
        list_of_adundant_numbers = []
        for i in range(start_number, stop_number+1):
            if self.number_is_abundant_number(i):
                list_of_adundant_numbers.append(i)
        return list_of_adundant_numbers

    def find_list_of_all_numbers_that_can_be_sum_of_item_from_2_lists(self, list1, list2):
        set_of_all_numbers = set()
        for x in list1:
            for y in list2:
                set_of_all_numbers.add(x+y)
        return list(set_of_all_numbers)

    def return_sum_of_numbers_in_range_not_in_a_given_list(self, number, list):
        list_of_numbers_not_in_list = []
        for i in range(number):
            if i not in list:
                list_of_numbers_not_in_list.append(i)
        solution = sum(list_of_numbers_not_in_list)
        return solution

    def solve(self):
        list_of_abundant_numbers = self.find_list_of_abundant_numbers_between_a_range(
            1, self.max_number)
        list_of_sums_of_2_abundant_numbers = \
            self.find_list_of_all_numbers_that_can_be_sum_of_item_from_2_lists(
                list_of_abundant_numbers, list_of_abundant_numbers)
        print(list_of_sums_of_2_abundant_numbers)
        solution = self.return_sum_of_numbers_in_range_not_in_a_given_list(
            self.max_number, list_of_sums_of_2_abundant_numbers)
        return solution


max_number = 28124
twenty_three = TwentyThree(max_number)
print(twenty_three.solve())
