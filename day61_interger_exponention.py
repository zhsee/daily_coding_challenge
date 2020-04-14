# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

# Do this faster than the naive method of repeated multiplication.

# For example, pow(2, 10) should return 1024.


# algo:
#                 /   1 if b = 0
#                 |
# int_exp(a, b)  <    a * int_exp(a, b-1) if b is odd number (a^(b) == a*a^(b-1))
#                 |
#                 \   int_exp(a, b/2) * int_exp(a, b/2)

import timeit, functools

def int_exp_naive(a, b):
    r = 1
    while b > 0:
        r *= a
        b -= 1
    return r

def int_exp(a, b):
    if not b:
        return 1

    if b%2:
        return a * int_exp(a, b-1)
    else:
        p = int_exp(a, b/2)
        return p * p


if __name__ == '__main__':
    # timeit.time
    print(timeit.timeit(stmt = functools.partial(pow, 2, 1000), number=10000))
    print(timeit.timeit(stmt = functools.partial(int_exp, 2, 1000), number=10000))
    print(timeit.timeit(stmt = functools.partial(int_exp_naive, 2, 1000), number=10000))
