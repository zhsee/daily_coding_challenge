# Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

# Do this in O(N) time and O(1) space.

from collections import Counter
from functools import reduce

def find_non_duplicate_ele(alist):
    ele_counter = Counter(alist)
    for a in ele_counter:
        if ele_counter[a]==1:
            return a


assert find_non_duplicate_ele([13, 19, 13, 13]) == 19
assert find_non_duplicate_ele([6, 1, 3, 3, 3, 6, 6]) == 1

def find_single_ele_among_duplet(alist):
    return reduce(lambda x, y: x ^ y, alist)

print(find_single_ele_among_duplet([11, 12, 11]))
print(find_single_ele_among_duplet([7, 8, 7, 8, 9, 10, 11, 11, 10]))


def find_single_ele_among_tripet(alist):
    one = 0
    two = 0

    for ele in alist:
        two = two | one & ele       ;# store bit which happened twice
        one = one ^ ele             ;# store bit which happened once
        not_three = ~(one & two)    :# mask for none '1' bit in both one and two
        one = one & not_three
        two = two & not_three

    return one

print(find_single_ele_among_tripet([13, 19, 13, 13]))
print(find_single_ele_among_tripet([6, 1, 3, 3, 3, 6, 6]))
