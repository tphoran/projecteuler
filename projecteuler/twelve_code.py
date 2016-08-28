

class Twelve(object):
    """
    The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle
    number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?
    """

    def __init__(self, target_number_of_divisors):
        self.target_number_of_divisors = target_number_of_divisors

    def find_nth_triangle_number(self, nth):
        if nth % 2 == 0:
            outcome = ((nth/2) * nth) + (nth - (nth / 2))
        else:
            outcome = ((nth//2) + 1) * nth
        return outcome

    def find_number_of_factors(self, number):
        """
        http://codereview.stackexchange.com/questions/32686/finding-number-of-factors-efficiency
        """
        result_set = set()
        sqrtn = int(number ** 0.5)
        for i in range(1, sqrtn + 1):
            q, r = number / i, number % i
            if r == 0:
                result_set.add(q)
                result_set.add(i)
        return len(result_set)

    def solve(self):
        factors = 0
        nth_triangle_number = 1
        temp_triangle_number = 0

        while factors < self.target_number_of_divisors:
            temp_triangle_number = self.find_nth_triangle_number(nth_triangle_number)
            nth_triangle_number += 1
            factors = self.find_number_of_factors(temp_triangle_number)

        return int(temp_triangle_number)


target_number_of_divisors = 500
test_twelve = Twelve(target_number_of_divisors)
print(test_twelve.solve())