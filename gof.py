import copy
import os
import time

from utils import (
    constrain,
    print_board,
)


INITIAL_BOARD = {
    (0, 2), (0, 3), (0, 4), (0, 8), (0, 9), (0, 10),
    (2, 0), (2, 5), (2, 7), (2, 12),
    (3, 0), (3, 5), (3, 7), (3, 12),
    (4, 0), (4, 5), (4, 7), (4, 12),
    (5, 2), (5, 3), (5, 4), (5, 8), (5, 9), (5, 10),
    (7, 2), (7, 3), (7, 4), (7, 8), (7, 9), (7, 10),
    (8, 0), (8, 5), (8, 7), (8, 12),
    (9, 0), (9, 5), (9, 7), (9, 12),
    (10, 0), (10, 5), (10, 7), (10, 12),
    (12, 2), (12, 3), (12, 4), (12, 8), (12, 9), (12, 10),
}


def get_neighbors_of(cell):
    """
    Return the neighbors of cell.
    """
    x, y = cell
    neighbors = []

    distance = 1
    r = range(0 - distance, 1 + distance)
    for row in r:
        for col in r:
            if not row == col == 0:
                neighbors.append((x + row, y + col))

    return set(neighbors)


def evaluate_rule_1(cell, current_board):
    next_board = copy.deepcopy(current_board)

    cell_neighbors = get_neighbors_of(cell)
    if len(current_board & cell_neighbors) < 2:
        next_board.remove(cell)

    return next_board


def advance(board):
    """
    Advance the board one step and return it.
    """
    new_board = set()
    for cell in board:
        # your code below
        pass

    return new_board


def start(board, steps=100, size=20):
    for i in range(1, steps + 1):
        os.system('clear')
        print('step:', i, '/', steps)
        print_board(board, size)
        time.sleep(0.1)
        board = constrain(advance(board), size)


if __name__ == '__main__':
    start(INITIAL_BOARD)
