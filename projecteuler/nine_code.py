import itertools

class Nine(object):
    """
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """

    def __init__(self, a_plus_b_plus_c):
        self.a_plus_b_plus_c = a_plus_b_plus_c
        self.a_plus_b_max = a_plus_b_plus_c/2
        self.a_b_range = range(1, self.a_plus_b_max)

    def pythaogrean_triplet_check(self, a, b):
        a_squared = a**2
        b_squared = b**2
        c_squared = a_squared + b_squared
        if c_squared**0.5 % 1 == 0.0:
            return True
        else:
            return False

    def collect_all_possible_sets_of_a_and_b(self, a_b_range):
        full_set = [p for p in itertools.product(a_b_range, repeat=2)]
        return full_set

    def calculate_c_given_a_and_b(self, a, b):
        a_squared = a ** 2
        b_squared = b ** 2
        c_squared = a_squared + b_squared
        c = c_squared**0.5
        return c

    def solve(self):
        list_of_possible_sets_of_a_and_b = self.collect_all_possible_sets_of_a_and_b(range(1, self.a_plus_b_max))
        list_of_pythaogrean_triplets = []
        for i in list_of_possible_sets_of_a_and_b:
            if self.pythaogrean_triplet_check(i[0], i[1]):
                list_of_pythaogrean_triplets.append(i)
        for e in list_of_pythaogrean_triplets:
            if e[0] + e[1] + self.calculate_c_given_a_and_b(e[0], e[1]) == self.a_plus_b_plus_c:
                return e + (self.calculate_c_given_a_and_b(e[0], e[1]),)


nine = Nine(1000)
triangle = nine.solve()
answer = triangle[0]*triangle[1]*triangle[2]
print answer
