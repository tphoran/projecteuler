class TwentyFive(object):
    """
    The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn - 1 + Fn - 2, where F1 = 1 F2 = 1.

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
    """
    def __init__(self, max_digits):
        self.max_digits = max_digits

    def output_fib_n(self, n):
        f_1 = 1
        f_2 = 1
        i = 2
        while i < n:
            f = f_1 + f_2
            f_1 = f_2
            f_2 = f
            i += 1
        return f

    def solve(self):
        n = 2
        f = 1
        while f < (10**(self.max_digits-1)):
            n += 1
            f = self.output_fib_n(n)
        return n


max_digits = 1000
twenty_five = TwentyFive(max_digits)
print(twenty_five.solve())