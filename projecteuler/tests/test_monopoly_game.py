import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import pytest
from projecteuler.monopoly_game import Game


def test_blocks_visited():
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

    assert visited_blocks == expected_visited_blocks


def test_cc_card():
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

    assert visited_blocks == expected_visited_blocks


def test_chance_card():
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

    assert visited_blocks == expected_visited_blocks


def test_doubles():
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

    assert visited_blocks == expected_visited_blocks


def test_top_five():
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
    assert top_two == expected_top_two
