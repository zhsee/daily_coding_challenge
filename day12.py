# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

from itertools import permutations

def staircase_bruteforce(N, step={1, 2}):
    all_combi = []
    sample_space = list(step) * N

    for n in range(1, N+1):
        # find all combi with n ele
        sub_combi = set(permutations(sample_space, n))
        all_combi.extend(list(sub_combi))

    result = [combi for combi in all_combi if sum(combi) == N]
    return result

# bruteforce method took too long for N >= 8
# result = staircase_bruteforce(5, {1, 3, 5})
# print(f'There are total of {len(result)} way to climb the staircase')
# for combi in result:
#     print(combi)

def staircase_fib(N, step={1, 2}):
    if N < 0:
        return 0
    elif N == 1:
        return 1
    elif N in step:
        return 1 + sum(staircase_fib(N - n, step) for n  in step if n < N)
    else:
        return sum(staircase_fib(N - n, step) for n  in step if n < N)

print(staircase_fib(8))
