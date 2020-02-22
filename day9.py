# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

def max_non_adjacent_sum(nums):
    incl = 0
    excl = 0

    for i in nums:

        # create new_excl to temporary hold the value as current excl value will be used in new_incl calculation.
        # new_excl = max between {previous excl} and {previous incl}
        new_excl = max(incl, excl)

        # new_incl = max between {previous excl + current value} and {previous incl}
        incl = max(excl + i, incl)
        excl = new_excl

    return max(incl, excl)


print(max_non_adjacent_sum([5, 1, 1, 5]))
print(max_non_adjacent_sum([2, 4, 6, 2, 5]))
