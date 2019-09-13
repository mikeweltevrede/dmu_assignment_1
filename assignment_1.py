""" Decision Making Under Uncertainty - Assignment 1

Group 2:
Martijn Ketelaars (ANR: xxxxxx)
Robbie Reyerse (ANR: xxxxxx)
Rosalien Timmerhuis (ANR: xxxxxx)
Mike Weltevrede (ANR: xxxxxx)
"""

import math
import numpy as np

# Part 1
# From lab 2, we have seen that the function `poisson()` from the `numpy.random` library is the fastest
item_size = 10

i = range(item_size)

lam = math.ceil(i/2)
gamma = np.random.poisson(lam)
dl = min(gamma, 10)
dh = np.random.triangular(90+g-i, 100+g-i, 110+g-i)
pi = 0.5 + 0.05*i - 0.001
r = 51 - i

u = np.random.uniform(size=1)
w = dl if(u < pi) else dh

def part_1():
    pass
