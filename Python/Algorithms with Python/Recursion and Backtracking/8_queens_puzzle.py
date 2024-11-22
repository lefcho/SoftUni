def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def can_place_queen(row, col, rows, cols, diagonal_1, diagonal_2):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in diagonal_1:
        return False
    if (row + col) in diagonal_2:
        return False

    return True


def set_queen(row, col, board, rows, cols, diagonal_1, diagonal_2):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    diagonal_1.add(row - col)
    diagonal_2.add(row + col)


def remove_queen(row, col, board, rows, cols, diagonal_1, diagonal_2):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    diagonal_1.remove(row - col)
    diagonal_2.remove(row + col)


def put_queens(row, board, rows, cols, diagonal_1, diagonal_2):
    if row == 8:
        print_board(board)
        return
    for col in range(8):
        if can_place_queen(row, col, rows, cols, diagonal_1, diagonal_2):
            set_queen(row, col, board, rows, cols, diagonal_1, diagonal_2)
            put_queens(row + 1, board, rows, cols, diagonal_1, diagonal_2)
            remove_queen(row, col, board, rows, cols, diagonal_1, diagonal_2)


n = 8
board = []
[board.append(['-'] * n) for _ in range(n)]

put_queens(0, board, set(), set(), set(), set())
