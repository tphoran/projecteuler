class Twentyone(object):
    """
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly
    into n).
    If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b
    are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
    therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    """
    def __init__(self, max_number):
        self.max_number = max_number

    def find_proper_divisors_of_number(self, number):
        proper_divisors = [1, ]
        for i in range(2, number//2 + 1):
            if number%i == 0:
                proper_divisors.append(i)
        return sum(proper_divisors)

    def capture_amiable_numbers_between_range(self, min_number, max_number):
        sums_of_proper_divisors = {}
        amiable_numbers = []
        for i in range(min_number, max_number+1):
            sum_of_proper_divisors = self.find_proper_divisors_of_number(i)
            sums_of_proper_divisors[i] = sum_of_proper_divisors
            if sum_of_proper_divisors in sums_of_proper_divisors.keys():
                if sums_of_proper_divisors[sum_of_proper_divisors] == i and i != \
                        sum_of_proper_divisors:
                    amiable_numbers.append(i)
                    amiable_numbers.append(sum_of_proper_divisors)
        return amiable_numbers

    def solve(self):
        amiable_numbers = self.capture_amiable_numbers_between_range(1, self.max_number)
        return sum(amiable_numbers)

max_number = 10000
twentyone = Twentyone(max_number)
print(twentyone.solve())