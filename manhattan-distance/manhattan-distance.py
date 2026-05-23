import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x, y = np.asarray(x), np.asarray(y)

    dist = np.absolute(x-y)
    manhattan = np.sum(dist)
    return int(manhattan)