n = int(input())

board = []
knights = []
removed_knights = 0
# read
for row in range(n):
    board.append([x for x in input()])
    for col in range(n):
        if board[row][col] == 'K':
            knights.append([row, col])
moves = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))

while True:
    max_hits = 0
    remove_knight = [0, 0]
    for k_row, k_col in knights:
        hits = 0
        for m_row, m_col in moves:
            new_row = m_row + k_row
            new_col = m_col + k_col
            if 0 <= new_row < n and 0 <= new_col < n:
                if board[new_row][new_col] == 'K':
                    hits += 1
            if hits > max_hits:
                max_hits = hits
                remove_knight = [k_row, k_col]
    if max_hits == 0:
        break

    board[remove_knight[0]][remove_knight[1]] = "0"
    knights.remove(remove_knight)
    removed_knights += 1

print(removed_knights)