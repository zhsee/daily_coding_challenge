# 4.1 Write out the code for the earlier sum function.
# 4.2 Write a recursive function to count the number of items in a list.
# 4.3 Find the maximum number in a list.
# 4.4 Remember binary search from chapter 1? It’s a divide-and-conquer algorithm, too. Can you come up with the base case and recursive case for binary search?

def sum_of(alist):
    # base case
    if len(alist) == 0:
        return 0
    # recursive case
    return alist[0] + sum_of(alist[1:])

assert sum_of([]) == 0
assert sum_of([1,2,3,4,-5]) == 5
assert sum_of([1,2,3,4,5]) == 15

def size_of(alist):
    # base case
    if not alist:
        return 0
    # recursive case
    return 1 + size_of(alist[1:])

assert size_of([]) == 0
assert size_of(['aa', 'bb', 'cc']) == 3
assert size_of(['aa', 'bb', 'cc', 'dd', 'ee', ['ff', 'gg']]) == 6

def max_of(alist):
    if len(alist) == 2:
        return alist[0] if alist[0] > alist[1] else alist[1]
    sub_max = max(alist[1:])
    return alist[0] if alist[0] > sub_max else sub_max

assert max_of([1,2,3,4,-5]) == 4
assert max_of([1,2,3,4,5]) == 5

# will come back later for recursive solution
def bsearch(alist, item):
    lo = 0
    hi = len(alist) - 1

    while lo <= hi:
        mid = int((hi + lo) / 2)
        guess = alist[mid]
        if guess == item:
            return mid
        if guess > item:
            hi = mid - 1
        else:
            lo = mid + 1
    return None

assert bsearch([44, 55, 66, 77, 88], 55) == 1
assert bsearch([44, 55, 66, 77, 88], 77) == 3
