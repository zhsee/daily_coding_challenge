# You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end=' ')
        print()


def is_safemove(maze, r, c, sol):
    # important! make sure the new cell is not out of bound and not a blockage in maze or not been in current solution path
    # without sol[r][c] == 1 criteria it may run into infinite loop
    if r not in range(len(maze)) or c not in range(len(maze[0])) or maze[r][c] == 1 or sol[r][c] == 1:
        return False
    return True


def maze_solver_util(maze, r0, c0, r1, c1, sol):
    if r0 == r1 and c0 == c1:
        sol[r0][c0] = 1
        return True

    if is_safemove(maze, r0, c0, sol):
        sol[r0][c0] = 1

        # move forward
        if maze_solver_util(maze, r0+1,c0, r1, c1, sol):
            return True

        # move backward
        if maze_solver_util(maze, r0-1,c0, r1, c1, sol):
            return True

        # move right
        if maze_solver_util(maze, r0,c0+1, r1, c1, sol):
            return True

        # move left
        if maze_solver_util(maze, r0,c0-1, r1, c1, sol):
            return True

        sol[r0][c0] = 0
        return False

    return False

def maze_solver(maze, start, end):
    nrow = len(maze)
    ncol = len(maze[0])

    # verify if start point and end point is valid
    r0, c0 = tuple(start)
    r1, c1 = tuple(end)

    if not all([r0 in range(nrow), c0 in range(ncol)]):
        print(f'-E- startpoint ({start}) is out of range')
        return False
    if not all([r1 in range(nrow), c1 in range(ncol)]):
        print(f'-E- startpoint ({end}) is out of range')
        return False

    solution = [[0]* ncol for _ in range(nrow)]

    if maze_solver_util(maze, r0, c0, r1, c1, solution) == False:
        print('no solution found!')
        return False

    print_grid(solution)


# maze = [[0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
maze = [
    [0,1,0,1,1],
    [0,0,0,0,0],
    [1,0,1,0,1],
    [0,0,1,0,0],
    [1,0,0,1,0],
]

print("========= MAZE =========")
print_grid(maze)
print("\n======= SOLUTION =======")
maze_solver(maze, [0, 0], [1, 4])
