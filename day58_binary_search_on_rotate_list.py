# An sorted array of integers was rotated an unknown number of times.

# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

# You can assume all the integers in the array are unique.


# 1) Find middle point mid = (l + h)/2
# 2) If key is present at middle point, return mid.
# 3) Else If arr[l..mid] is sorted
#     a) If key to be searched lies in range from arr[l]
#        to arr[mid], recur for arr[l..mid].
#     b) Else recur for arr[mid+1..h]
# 4) Else (arr[mid+1..h] must be sorted)
#     a) If key to be searched lies in range from arr[mid+1]
#        to arr[h], recur for arr[mid+1..h].
#     b) Else recur for arr[l..mid]


def bsearch_r(alist, lo, hi, key):
    print(f'processing {alist[lo:hi+1]}')
    if lo > hi:
        return -1

    mid = (hi + lo) // 2
    print(f'mid_ele: {mid} {alist[mid]}')
    if alist[mid] == key:
        return mid

    if alist[mid] >= alist[lo]:
        # lower list is sorted
        if key >= alist[lo] and key <= alist[mid]:
            return bsearch_r(alist, lo, mid-1, key)
        return bsearch_r(alist, mid+1, hi, key)

    else:
        # upper list is sorted
        if key >= alist[mid] and key <= alist[hi]:
            return bsearch_r(alist, mid+1, hi, key)
        return bsearch_r(alist, lo, mid-1, key)

mylist = [13, 18, 25, 2, 6, 7, 8, 10]
print(bsearch_r(mylist, 0, len(mylist)-1, 8))
mylist = [13, 18, 23, 25, 1, 2, 6, 8, 8, 8, 8, 8, 8, 8, 10]
print(bsearch_r(mylist, 0, len(mylist)-1, 23))
