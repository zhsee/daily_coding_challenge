# You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

def print_board(board):
    N = len(board)
    border = '|' + '+'.join(['---'] * N) + '|'

    print()
    print("-" * (N * 4 + 1))
    for r in range(len(board)):
        for c in range(len(board)):
            print(f'| {board[r][c]} ' ,end='')
        print('|')
        if r != N - 1:
            print(border)
    print("-" * (N * 4 + 1))
    print()


def is_safe(board, r, c):
    N = len(board)
    if any(board[r][j] == "Q" for j in range(N)):
        return False
    if any(board[i][c] == "Q" for i in range(N)):
        return False
    if any(board[i][j] == "Q" for i in range(N) for j in range(N) if abs(i - r) == abs(j - c)):
        return False
    return True


def n_queen_util(board, row):
    res = False

    if row >= len(board):
        print_board(board)
        return True
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            res = n_queen_util(board, row + 1) or res
            board[row][col] = " "
    return res


def n_queen(N):
    board = [[" "] * N for _ in range(N)]
    if n_queen_util(board, 0) == False:
        print(f'No solution when N = {N}!')


n_queen(8)
