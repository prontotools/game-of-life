import unittest

from gof import get_neighbors_of


class GameOfLifeTest(unittest.TestCase):
    def test_get_neighbors_of_cell_should_return_one(self):
        cell = (0, 3)
        result = get_neighbors_of(cell)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
