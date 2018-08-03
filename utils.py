def print_board(board, size=None):
    sizex = sizey = size or 0
    for x, y in board:
        sizex = x if x > sizex else sizex
        sizey = y if y > sizey else sizey
    for i in range(sizex + 1):
        for j in range(sizey + 1):
            print(' x ' if (i, j) in board else ' . ', end='')
        print()


def constrain(board, size):
    return set(cell for cell in board if cell[0] <= size and cell[1] <= size)
