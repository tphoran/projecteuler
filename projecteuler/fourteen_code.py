class Fourteen(object):
    """
    The following iterative sequence is defined for the set of positive integers:

    n  - n/2 (n is even)
    n  - 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?
    """

    def __init__(self, max_starting_number):
        self.max_starting_number = max_starting_number

    def generate_collatz_sequence(self, starting_number):
        n = starting_number
        collatz_sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n /= 2
                collatz_sequence.append(n)
            else:
                n = (3 * n + 1)
                collatz_sequence.append(n)
        return collatz_sequence

    def solve(self):
        max_len_collatz_seqence = 0
        max_len_collatz_number = 0
        for i in range(2, self.max_starting_number):
            temp_collatz_sequence = self.generate_collatz_sequence(i)
            temp_len_collatz_sequence = len(temp_collatz_sequence)
            if temp_len_collatz_sequence > max_len_collatz_seqence:
                max_len_collatz_seqence = temp_len_collatz_sequence
                max_len_collatz_number = i
        return max_len_collatz_number


max_starting_number = 1000000
fourteen = Fourteen(max_starting_number)
print(fourteen.solve())
