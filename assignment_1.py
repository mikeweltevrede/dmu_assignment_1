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
    p = math.floor(60 + 0.1 * g)  # Unit excess weight penalty
    K = 400 + 4 * g  # Knapsack capacity

    pi = np.asarray([0.5 + 0.05 * (i + 1) - 0.001 for i in range(num_items)])
    r = np.asarray([51 - (i + 1) for i in range(num_items)])

    item_sizes = {j: generate_instance(num_items, g, seed=j) for j in range(num_instances)}

    instance = (p, K, pi, r, item_sizes)

    return instance