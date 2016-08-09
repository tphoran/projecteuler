from unittest import TestCase

from projecteuler.monopoly.game import Game


class TestGame(TestCase):
    def test_blocks_visited(self):
        location = 'A'
        board_spaces = ['A', 'B', 'C', 'D']
        dice_min_integer = 1
        dice_max_integer = 1
        cards_in_cc = ['A1', 'B2']
        cards_in_chance = ['A1', 'C1']

        game = Game(location, board_spaces, dice_min_integer, dice_max_integer, cards_in_cc, cards_in_chance)
        game.turn()

        expected_visited_blocks = 'C'

        visited_blocks = game.get_blocks_visited()[0]

        self.assertEqual(visited_blocks, expected_visited_blocks)

    def test_cc_card(self):
        location = 'A'
        board_spaces = ['A', 'B', 'CC', 'JAIL']
        dice_min_integer = 1
        dice_max_integer = 1
        cards_in_chance = ['JAIL', 'JAIL']
        cards_in_cc = ['JAIL', 'JAIL']

        game = Game(location, board_spaces, dice_min_integer, dice_max_integer, cards_in_cc, cards_in_chance)
        game.turn()

        expected_visited_blocks = 'JAIL'

        visited_blocks = game.get_blocks_visited()[0]

        self.assertEqual(visited_blocks, expected_visited_blocks)

    def test_chance_card(self):
        location = 'A'
        board_spaces = ['A', 'B', 'CH', 'C1']
        dice_min_integer = 1
        dice_max_integer = 1
        cards_in_chance = ['C1', 'C1']
        cards_in_cc = ['JAIL', 'JAIL']

        game = Game(location, board_spaces, dice_min_integer, dice_max_integer, cards_in_cc, cards_in_chance)
        game.turn()

        expected_visited_blocks = 'C1'

        visited_blocks = game.get_blocks_visited()[0]

        self.assertEqual(visited_blocks, expected_visited_blocks)

    def test_doubles(self):
        location = 'A'
        board_spaces = ['A', 'B', 'C', 'JAIL']
        dice_min_integer = 1
        dice_max_integer = 1
        cards_in_chance = ['C1', 'C1']
        cards_in_cc = ['GTJ', 'GTJ']

        game = Game(location, board_spaces, dice_min_integer, dice_max_integer, cards_in_cc, cards_in_chance)
        game.turn()
        game.turn()
        game.turn()

        expected_visited_blocks = 'JAIL'

        visited_blocks = game.get_blocks_visited()[2]

        self.assertEqual(visited_blocks, expected_visited_blocks)

    def test_top_five(self):
        location = 'JAIL'
        board_spaces = ['JAIL', 'B', 'A', 'C']
        dice_min_integer = 1
        dice_max_integer = 1
        cards_in_chance = ['C1', 'C1']
        cards_in_cc = ['GTJ', 'GTJ']

        game = Game(location, board_spaces, dice_min_integer, dice_max_integer, cards_in_cc, cards_in_chance)
        game.turn()
        game.turn()
        game.turn()
        game.turn()
        game.turn()
        game.turn()
        game.turn()
        game.turn()
        game.turn()
        game.turn()

        expected_top_two = '0002'

        top_two = game.get_top_five()[0:4]
        self.assertEqual(top_two, expected_top_two)
