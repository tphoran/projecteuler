import pytest
from projecteuler.monopoly_board import Board


def test_move_x_spaces():
    spaces = ['a', 'b', 'c', 'd']
    start_location = spaces[1]
    num_spaces_to_move = 3

    board = Board(spaces, start_location)

    board.move(num_spaces_to_move)

    new_location = board.get_location()

    expected_new_location = 'a'

    assert new_location == expected_new_location


def test_set_location():
    spaces = ['a', 'b', 'c', 'd']
    start_location = spaces[1]

    set_location = 'c'

    board = Board(spaces, start_location)
    board.set_location(set_location)

    expected_new_location = set_location

    new_location = board.get_location()

    assert new_location == expected_new_location


def test_go_to_next_X_space():
    spaces = ['a', 'X1', 'b', 'c', 'd', 'X2']
    start_location = spaces[2]

    board = Board(spaces, start_location)

    expected_new_location = 'X2'

    board.go_to_next_x_space('X')

    new_location = board.get_location()

    assert new_location == expected_new_location
