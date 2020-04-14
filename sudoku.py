
def is_valid(grid, r, c, val):
    # global grid
    # return False if found the value in same row or same column
    for i in range(9):
        if grid[r][i] == val or grid[i][c] == val:
            return False
    # return False if found the value in the sub-aisle
    for rr in range(r//3 * 3, r//3 * 3 + 3):
        for cc in range(c//3 * 3, c//3 * 3 + 3):
            if grid[rr][cc] == val:
                return False
    return True

def solve(grid):
    # global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for val in range(1, 10):
                    if is_valid(grid, i, j, val):
                        grid[i][j] = val
                        solve(grid)
                        grid[i][j] = 0
                return
    print_grid(grid)
    # input('more')


def print_grid(grid):
    for i in range(0, len(grid)):
        for j in range(len(grid[i])):
            if j > 0 and j % 3 == 0:
                print('|', end='')
            val = str(grid[i][j]) if grid[i][j] != 0 else '.'
            print(val, end=' ')
        if i > 0 and i in (2, 5):
            print('\n' + '-'*6 + '+' + '-'*6 + '+' + '-'*6, end='')
        print()
    print()

# grid = [
#     [4,0,0,0,0,0,8,0,5],
#     [0,3,0,0,0,0,0,0,0],
#     [0,0,0,7,0,0,0,0,0],
#     [0,2,0,0,0,0,0,6,0],
#     [0,0,0,0,8,0,4,0,0],
#     [0,0,0,0,1,0,0,0,0],
#     [0,0,0,6,0,3,0,7,0],
#     [5,0,0,2,0,0,0,0,0],
#     [1,0,4,0,0,0,0,0,0],
# ]

grid = [
    [0,0,3,0,2,0,6,0,0],
    [9,0,0,3,0,5,0,0,1],
    [0,0,1,8,0,6,4,0,0],
    [0,0,8,1,0,2,9,0,0],
    [7,0,0,0,0,0,0,0,8],
    [0,0,6,7,0,8,2,0,0],
    [0,0,2,6,0,9,5,0,0],
    [8,0,0,2,0,3,0,0,9],
    [0,0,5,0,1,0,3,0,0],
]

# grid = [
#     [5,3,0,0,7,0,0,0,0],
#     [6,0,0,1,9,5,0,0,0],
#     [0,9,8,0,0,0,0,6,0],
#     [8,0,0,0,6,0,0,0,3],
#     [4,0,0,8,0,3,0,0,1],
#     [7,0,0,0,2,0,0,0,6],
#     [0,6,0,0,0,0,2,8,0],
#     [0,0,0,4,1,9,0,0,5],
#     [0,0,0,0,8,0,0,0,9],
# ]

print_grid(grid)
solve(grid)
# print_grid(grid)
# print(is_valid(another_puzzle, 4, 4, 5))
