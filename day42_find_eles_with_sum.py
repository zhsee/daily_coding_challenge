# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

# Integers can appear more than once in the list. You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.


def powerset(S):
    length = len(S)
    binary_length = 2 ** length

    pset = []
    for i in range(binary_length):
        decoded = list(bin(i)[2:].zfill(length))
        subset = {S[j] for j in range(length) if decoded[j] == '1'}
        pset.append(subset)

    return pset

def find_subset_sum_equal_k(S, k):
    for cset in powerset(S):
        if sum(cset) == k:
            return cset

    return None


print(find_subset_sum_equal_k([12, 1, 61, 5, 9, 2], 24))
