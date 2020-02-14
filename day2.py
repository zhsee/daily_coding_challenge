
#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?

from functools import reduce

def product_of_other_members_with_div(inarray):
    product_of_all = reduce(lambda x, y: x * y, inarray)
    outarray = [int(product_of_all/ele) for ele in inarray]
    return outarray


def product_of_other_members_without_div(inarray):
    array_of_array = [inarray[:i] + inarray[i+1:] for i in range(len(inarray))]
    outarray = [reduce(lambda x, y: x * y, array) for array in array_of_array]
    return outarray



print(product_of_other_members_with_div([1, 2, 3, 4, 5]))
print(product_of_other_members_with_div([2, 3, 6]))
print(product_of_other_members_without_div([1, 2, 3, 4, 5]))
print(product_of_other_members_without_div([2, 3, 6]))
