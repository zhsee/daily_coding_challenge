def qsort(alist):
    # base
    if len(alist) < 2:
        return alist
    # recursive
    pivot = alist[0]
    larger = [a for a in alist[1:] if a >= pivot]
    lesser = [a for a in alist[1:] if a < pivot]
    return qsort(lesser) + [pivot] + qsort(larger)


mylist = [5, 4, 8, 2, 1, 9, 3, 2, 7]
print(qsort(mylist))
