

class Seven(object):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10,001st prime number?
    """

    def __init__(self, ith_prime):
        self.ith_prime = ith_prime

    def prime_sieve(self, max_number):
        not_prime = []
        prime = []
        for i in range(2, max_number + 1):
            if i not in not_prime:
                prime.append(i)
                for j in range(i * i, max_number + 1, i):
                    not_prime.append(j)
        return prime

    def solve(self):
        prime_list = self.prime_sieve(200000)
        ith_prime = prime_list[self.ith_prime-1]
        return ith_prime


seven = Seven(10001)
print(seven.solve())
