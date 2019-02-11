import random


class Cards(object):
    """
    Set of cards from which to draw from a random item from list and replace
    """

    def __init__(self, set_of_choices):
        self.set_of_choices = set_of_choices

    def draw(self):
        return random.choice(self.set_of_choices)
