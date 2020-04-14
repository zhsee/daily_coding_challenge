# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.


def remove_k_ele(myarr, k):
    if k > len(myarr):
        print(f'Argument k: {k} is larger than the length of the list!')
        return 0

    for i in range(k):
        myarr.pop()


aa = [1, 2, 3, 4, 5, 6, 7]
remove_k_ele(aa, 3)
print(aa)
