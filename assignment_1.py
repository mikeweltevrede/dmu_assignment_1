"""Decision Making Under Uncertainty - Assignment 1

Group 2:
Martijn Ketelaars (ANR: xxxxxx)
Robbie Reyerse (ANR: xxxxxx)
Rosalien Timmerhuis (ANR: xxxxxx)
Mike Weltevrede (ANR: 756479)
"""

import math
import numpy as np

# Generation of Problem Instances
# # Part 1


def generate_w(num_items, g):
    """Generate a set of `num_items` weights

    Parameters
    ----------
    num_items : int
        Number of items to generate weights for
    g : int
        Group number

    Returns
    -------
    w : list
        List of weights
    """

    # Assert inputs are of correct form
    assert isinstance(num_items, int), "num_items is not an int"
    assert isinstance(g, int), "g is not an int"

    items = range(num_items)

    # Generate possible item sizes.
    # # From Lab 2, we know that the `numpy.random` library is the fastest.
    lam = [math.ceil(i/2) for i in items]
    dl = np.minimum(np.random.poisson(lam), 10)
    dh = [np.random.triangular(90+g-i, 100+g-i, 110+g-i) for i in items]

    u = np.random.uniform(size=num_items)
    pi = [0.5 + 0.05*i - 0.001 for i in items]

    w = [dh[i] if u[i] < pi[i] else dl[i] for i in items]

    return w


def generate_instance(num_instances, num_items, g):
    """Generates instances of a Stochastic Knapsack Problem (SKP).

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
        Tuple containing the unit excess weight penalty `p`, knapsack capacity `K`,
        revenue vector `r`, and weights `w`, respectively.
    """

    # Assert inputs are of correct form
    assert isinstance(num_instances, int), "num_instances is not an int"
    assert isinstance(num_items, int), "num_items is not an int"
    assert isinstance(g, int), "g is not an int"

    # Generate instance variables
    p = math.floor(60 + 0.1*g)  # Unit excess weight penalty
    K = 400 + 4*g  # Knapsack capacity
    r = {i: 51-i for i in range(num_items)}  # Revenues
    w = {j: generate_w(num_items, g) for j in range(num_instances)}  # Weights

    instance = (p, K, r, w)

    return instance


p, K, r, w = generate_instance(num_instances=10, num_items=10, g=2)
