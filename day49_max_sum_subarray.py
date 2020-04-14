# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

# Do this in O(N) time.


def max_sum_of_subarray(alist):
    maxsum = 0
    maxsum_here = 0

    for ele in alist:
        maxsum_here += ele
        if maxsum_here < 0:
            maxsum_here = 0
        elif maxsum_here > maxsum:
            maxsum = maxsum_here

    return maxsum


print(max_sum_of_subarray([34, -50, 42, 14, -5, 86]))
print(max_sum_of_subarray([-5, -1, -8, -9]))
print(max_sum_of_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))
