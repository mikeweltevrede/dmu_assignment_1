"""Decision Making Under Uncertainty - Assignment 1

Group 2:
Martijn Ketelaars (ANR: 120975)
Robbie Reyerse (ANR: 109997)
Rosalien Timmerhuis (ANR: 520618)
Mike Weltevrede (ANR: 756479)
"""

import random

import math
import numpy as np
from scipy import stats

# Generation of Problem Instances
# # Part 1


def generate_instance(num_items, g, seed):
    """Generate a dictionary of `num_items` possible item sizes

    Parameters
    ----------
    num_items : int
        Number of items to generate weights for
    g : int
        Group number

    Returns
    -------
    item_sizes : dict
        Dictionary containing the possible item sizes
    """

    # Assert inputs are of correct form
    assert isinstance(num_items, int), "num_items is not an int"
    assert isinstance(g, int), "g is not an int"

    # Generate possible item sizes.
    # # From Lab 2, we know that the `numpy.random` library is the fastest.

    # TODO: Note about i+1 instead of i

    # TODO: We need to check if we are indeed allowed to use another library or if we need to write
    # it ourselves
    # np.random.seed(seed)
    lam = [math.ceil((i+1)/2) for i in range(num_items)]
    dl = np.minimum(np.random.poisson(lam), 10)
    dh = [np.random.triangular(90+g-(i+1), 100+g-(i+1), 110+g-(i+1)) for i in range(num_items)]

    item_sizes = {"dl": dl, "dh": dh}

    return item_sizes


def skp(num_instances, num_items, g):
    """Generates `num_instances` instances of a Stochastic Knapsack Problem (SKP).

    Parameters
    ----------
    num_instances : int
        Number of instances of the SKP to generate
    num_items : int
        Number of items to consider per instance
    g : int
        Group number

    Returns
    -------
    instance : tuple
        Tuple containing the unit excess weight penalty `p`, knapsack capacity `K`, item size
        probability vector `pi`, revenue vector `r`, and possible item sizes `item_sizes`,
        respectively.
    """

    # Assert inputs are of correct form
    assert isinstance(num_instances, int), "num_instances is not an int"
    assert isinstance(num_items, int), "num_items is not an int"
    assert isinstance(g, int), "g is not an int"

    # Generate instance variables
    p = math.floor(60 + 0.1*g)  # Unit excess weight penalty
    K = 400 + 4*g  # Knapsack capacity

    pi = [0.5 + 0.05*(i+1) - 0.001 for i in range(num_items)]  # Item size probabilities
    r = [51-(i+1) for i in range(num_items)]  # Revenues

    item_sizes = {j: generate_instance(num_items, g, j) for j in range(num_instances)}  # dl, dh

    instance = (p, K, pi, r, item_sizes)

    return instance


num_instances = 10
num_items = 10
g = 2

p, K, pi, r, item_sizes = skp(num_instances, num_items, g)

# Heuristic Algorithm
# # Part 2


# Monte Carlo Simulation
# # Part 3
# np.random.seed(42) # TODO: remove this
x = np.random.binomial(1, 0.5, size=num_items)  # TODO: Get these from Martijn's function
j = 0

# Slide 62 van lecture 1 -> krijg number of runs
alpha = 0.05
z = stats.norm.ppf(1-alpha/2)
epsilon = 0.01
num_runs = math.ceil((1/2)**2 * (z/epsilon)**2)

num_runs = 5

profits = []

print(x)

for run in range(num_runs):
    u = np.random.uniform(size=num_items)
    print(u)
    w = [item_sizes[j]["dl"][i] if u[i] < pi[i] else item_sizes[j]["dh"][i]
         for i in range(num_items)]

    print(w)

    total_weight = np.dot(x, w)
    excess = max(total_weight-K, 0)

    profit = np.dot(x, r) - excess*p
    profits.append(profit)

print(profits)
print(np.percentile(profits, 0.025))
print(np.percentile(profits, 0.975))

# Stochastic Programming Models
# # Part 4
# # Part 5
# # Part 6

# Sample Average Approximation
# # Part 7

# Analysis
# # Part 8

# # Part 9

# # Bonus

