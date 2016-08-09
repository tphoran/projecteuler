class One(object):
    """
    Euler problem 1

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    def __init__(self, multiple_list, less_than_number):
        self.multiple_list = multiple_list
        self.less_than_number = less_than_number

    def solve(self):
        multiple_list = []
        for i in range(self.less_than_number):
            if i % self.multiple_list[0] == 0 or i % self.multiple_list[1] == 0:
                multiple_list.append(i)
        cumulative_multiples = sum(multiple_list)
        return cumulative_multiples


euler_one = One([3,5], 1000).solve()
print euler_one