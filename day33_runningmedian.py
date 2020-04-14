# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

def running_median(alist):
    blist = []

    for ele in alist:
        blist.append(ele)
        blist.sort()
        length = len(blist)
        if length%2 == 1:
            median = blist[length//2]
        else:
            median = 0.5 * (blist[length//2 - 1] + blist[length//2])
        print(median)


running_median([2, 1, 5, 7, 2, 0, 5])
