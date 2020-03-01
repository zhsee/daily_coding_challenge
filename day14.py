# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.
import random
from math import sqrt

def root_sum_square(x, y):
    return sqrt(x**2 + y**2)


def find_pi_with_mc(sample):
    # πr^2 / unit_square_area = num_of_dot_within_circle/total_dot
    # π =~ 4 * num_of_dot_within_circle/sample
    sample_dots = (root_sum_square(random.random() - 0.5, random.random() - 0.5) for i in range(sample))
    return 4.0 * sum(map(lambda x: True if x <= 0.5 else False, sample_dots))/sample


for n in [10, 100, 1000, 10000, 100000, 10000000, 10000000000]:
    print(find_pi_with_mc(n))


