# You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

def findfilledwater(alist):
    size = len(alist)
    water = 0

    left = [0] * size
    right = [0] * size

    # find the max height at the left side and right side of each position
    for i in range(size):
        left[i] = max(alist[:i]) if alist[:i] else 0
        right[i] = max(alist[i+1:]) if alist[i+1:] else 0

    # find the diff of each position with the min(tallest at the left, tallest at the right)
    for i in range(size):
        water += max(min(left[i], right[i]) - alist[i], 0)

    return water


print(findfilledwater([2, 1, 2]))
print(findfilledwater([3, 0, 1, 3, 0, 5]))
print(findfilledwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


def findfilledwater2(alist):
    size = len(alist)
    water = 0

    left = [0] * size
    right = [0] * size

    # find the max height at the left side and right side of each position including itself.
    for i in range(size):
        left[i] = max(alist[:i+1])
        right[i] = max(alist[i:])

    for i in range(size):
        water += min(left[i], right[i]) - alist[i]

    return water

print(findfilledwater2([2, 1, 2]))
print(findfilledwater2([3, 0, 1, 3, 0, 5]))
print(findfilledwater2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
