# There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

# Right, then down
# Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

from math import factorial

def mn_diagonal_paths(m, n):
    num_right = m - 1
    num_down = n - 1
    total_step = num_right + num_down
    return factorial(total_step)/(factorial(num_down) * factorial(num_right))


assert mn_diagonal_paths(2, 2) == 2
assert mn_diagonal_paths(5, 5) == 70
assert mn_diagonal_paths(2, 3) == 3
assert mn_diagonal_paths(3, 3) == 6
