
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time

def job_scheduler(f, n):
    start = time.time()
    time.sleep(n/1000)
    print(f'elapsed {(time.time()-start) * 1000} miliseconds')
    f()


def dummy_function():
    print('dummy_function has been called.')

job_scheduler(dummy_function, 2000)
