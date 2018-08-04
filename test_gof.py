import unittest

from gof import (
    evaluate_rule_1,
    get_neighbors_of,
)


class GameOfLifeTest(unittest.TestCase):
    def test_get_neighbors_of_cell_should_return_all_neighbors(self):
        cell = (1, 1)
        result = get_neighbors_of(cell)

        expected = {
            (0, 0), (0, 1), (0, 2),
            (1, 0),         (1, 2),
            (2, 0), (2, 1), (2, 2),
        }
        self.assertEqual(result, expected)

    def test_cell_dies_if_there_are_fewer_than_two_neighbors(self):
        cell = (1, 1)
        current_board = {
            (0, 1), (1, 1),
        }
        result = evaluate_rule_1(cell, current_board)

        expected = {
            (0, 1),
        }
        self.assertEqual(result, expected)

    def test_cell_lives_if_there_are_not_fewer_than_two_neighbors(self):
        cell = (1, 1)
        current_board = {
            (0, 1), (1, 1), (1, 2),
        }
        result = evaluate_rule_1(cell, current_board)

        expected = {
            (0, 1), (1, 1), (1, 2),
        }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
