from unittest import TestCase

from projecteuler.monopoly.board import Board


class TestBoard(TestCase):
    def test_move_x_spaces(self):
        spaces = ['a', 'b', 'c', 'd']
        start_location = spaces[1]
        num_spaces_to_move = 3

        board = Board(spaces, start_location)

        board.move(num_spaces_to_move)

        new_location = board.get_location()

        expected_new_location = 'a'

        self.assertEqual(new_location, expected_new_location)

    def test_set_location(self):
        spaces = ['a', 'b', 'c', 'd']
        start_location = spaces[1]

        set_location = 'c'

        board = Board(spaces, start_location)
        board.set_location(set_location)

        expected_new_location = set_location

        new_location = board.get_location()

        self.assertEqual(new_location, expected_new_location)

    def test_go_to_next_X_space(self):
        spaces = ['a', 'X1', 'b', 'c', 'd', 'X2']
        start_location = spaces[2]

        board = Board(spaces, start_location)

        expected_new_location = 'X2'

        board.go_to_next_x_space('X')

        new_location = board.get_location()

        self.assertEqual(new_location, expected_new_location)