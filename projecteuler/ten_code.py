
class Ten(object):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """

    def __init__(self, primes_below_number):
        self.primes_below_number = primes_below_number

    def sieve_for_primes_to(self, n):
        """
        http://stackoverflow.com/questions/16004407/a-fast-prime-number-sieve-in-python
        """
        size = n // 2
        sieve = [1] * size
        limit = int(n ** 0.5)
        for i in range(1, limit):
            if sieve[i]:
                val = 2 * i + 1
                tmp = ((size - 1) - i) // val
                sieve[i + val::val] = [0] * tmp
        return [2] + [i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0]

    def solve(self):
        prime_list = self.sieve_for_primes_to(self.primes_below_number)
        sum_of_prime_list = sum(prime_list)
        return sum_of_prime_list


ten = Ten(2000000)
solution = ten.solve()
print(solution)
