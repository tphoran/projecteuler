import random


class Dice(object):
    """
    Dice that rolls a random number between a minimum and maximum given integer
    """

    def __init__(self, min_integer, max_integer):
        self.min_integer = min_integer
        self.max_integer = max_integer

    def roll(self):
        return random.randint(self.min_integer, self.max_integer)




