
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def add_two_sum_check(nums, sum_num):
    return any([True for i in range(len(nums)) for num in nums[i+1:] if nums[i] + num == sum_num])


print(add_two_sum_check([10, 15, 3, 7, 19], 29))
