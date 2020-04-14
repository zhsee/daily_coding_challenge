# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def dutch_flag(alist):
    low = 0
    reader = 0
    hi = len(alist) - 1

    while hi >= reader:
        if alist[reader] == 'G':
            reader += 1
        elif alist[reader] == 'R':
            alist[reader], alist[low] = alist[low], alist[reader]
            low += 1
            reader += 1
        else:
            alist[reader], alist[hi] = alist[hi], alist[reader]
            hi -= 1
        # print(f'{low} {reader} {hi} {alist}')
    return alist

print(dutch_flag(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
print(dutch_flag(['G', 'B', 'R', 'R', 'B', 'R', 'R']))
print(dutch_flag(['G', 'G', 'R', 'G', 'B', 'R', 'R']))
