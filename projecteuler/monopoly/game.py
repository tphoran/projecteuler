from projecteuler.monopoly.board import Board
from projecteuler.monopoly.cards import Cards
from projecteuler.monopoly.dice import Dice
import collections


class Game(object):
    """
    Game tracks a single game
    """
    def __init__(self, start_location, board_spaces, dice_min_integer, dice_max_integer, cards_in_CC, cards_in_Chance):
        self.start_location = start_location
        self.dice_min_integer = dice_min_integer
        self.dice_max_integer = dice_max_integer
        self.cards_in_CC = cards_in_CC
        self.cards_in_Chance = cards_in_Chance
        self.last_turn = False
        self.second_two_last_turn = False
        self.blocks_visited = []
        self.spaces = board_spaces
        self.double_counter = 0

        self.board = Board(self.spaces, self.start_location)
        self.comm_chest = Cards(self.cards_in_CC)
        self.chance = Cards(self.cards_in_Chance)
        self.dice_1 = Dice(self.dice_min_integer, self.dice_max_integer)
        self.dice_2 = Dice(self.dice_min_integer, self.dice_max_integer)

    def turn(self):
        roll_1 = self.dice_1.roll()
        roll_2 = self.dice_2.roll()

        if roll_1 == roll_2:
            self.double_counter += 1
        else:
            self.double_counter = 0

        if self.double_counter == 3:
            self.board.set_location('JAIL')
            self.double_counter = 0
            self.blocks_visited.append(self.board.get_location())
        else:
            self.board.move(roll_1 + roll_2)

            if self.board.get_location()[0:2] == 'CH':
                card_drawn = self.chance.draw()
                if card_drawn in ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1']:
                    self.board.set_location(card_drawn)
                elif card_drawn == 'Next R':
                    self.board.go_to_next_x_space('R')
                elif card_drawn == 'Next U':
                    self.board.go_to_next_x_space('U')
                elif card_drawn == 'Back 3':
                    self.board.move(-3)

            if self.board.get_location() == 'GTJ':
                self.board.set_location('JAIL')

            if self.board.get_location()[0:2] == 'CC':
                card_drawn = self.comm_chest.draw()
                if card_drawn in ['GO', 'JAIL']:
                    self.board.set_location(card_drawn)

            self.blocks_visited.append(self.board.get_location())

    def get_blocks_visited(self):
        return self.blocks_visited

    def get_top_five(self):
        counter = collections.Counter(self.blocks_visited)
        top_five = counter.most_common(5)
        top_five_string = ''
        for item in top_five:
            space_str = str(self.spaces.index(item[0]))
            if len(space_str) == 1:
                space_str = '0'+space_str
            top_five_string += space_str
        return top_five_string

    def get_top_five_strings(self):
        counter = collections.Counter(self.blocks_visited)
        top_five = counter.most_common(5)
        top_five_string = ''
        for item in top_five:
            space_str = str((item[0]))
            if len(space_str) == 1:
                space_str = '0'+space_str
            top_five_string += space_str+'  '
        return top_five_string
        
    def get_top_five_prob(self):
        counter = collections.Counter(self.blocks_visited)
        top_five = counter.most_common(5)
        top_five_string = ''
        for item in top_five:
            space_str = str((item[1]))
            if len(space_str) == 1:
                space_str = '0'+space_str
            top_five_string += space_str+'  '
        return top_five_string

    def get_length_visited(self):
        return len(set(self.blocks_visited))
