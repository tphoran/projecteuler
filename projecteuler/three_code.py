

class Three(object):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """

    def __init__(self, input_number):
        self.input_number = input_number

    def largest_prime_factor(self, n):
        """
        http: // code.jasonbhill.com / c / project - euler - problem - 3 /
        """
        largest_factor = 1

        # remove any factors of 2 first
        while n % 2 == 0:
            largest_factor = 2
            n = n / 2

        # now look at odd factors
        p = 3
        while n != 1:
            while n % p == 0:
                largest_factor = p
                n = n / p
            p += 2

        return largest_factor

    def solve(self):
        return self.largest_prime_factor(self.input_number)


euler_three = Three(600851475143)
print(euler_three.solve())
