# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def find_first_missing_positive_interger(nums):
    q = len(nums)
    l = min([num for num in nums if num > 0])
    for i in range(l, l + q):
        if not i in nums:
            return i


print(find_first_missing_positive_interger([3, 4, -1 ,1, 1]))
print(find_first_missing_positive_interger([1, 2, 0]))
