# Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.


def powerset(aset):
    length = len(aset)
    binary_length = 2 ** length

    aset = list(aset)
    pset = []
    for i in range(binary_length):
        decoded = list(bin(i)[2:].zfill(length))
        subset = [aset[j] for j in range(length) if decoded[j] == '1']
        pset.append(subset)

    return pset


def equal_partition(alist):
    total = sum(alist)

    if total%2:
        return None

    div2 = total/2
    psets = powerset(alist)

    for pset in psets:
        if sum(pset) == div2:
            first_part = pset
            break
    else:
        print('no answer')

    for ele in first_part:
        alist.remove(ele)

    print(f'first partition: {first_part}')
    print(f'second partition: {alist}')


equal_partition([15, 5, 20, 10, 35, 15, 10])
equal_partition([15, 5, 20, 10, 35])

