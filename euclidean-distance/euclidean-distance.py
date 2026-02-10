import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    n = len(x)
    x = np.asarray(x)
    y = np.asarray(y)
    diff = x-y
    diff2 = np.square(diff)
    total = np.sum(diff2)
    res = np.sqrt(total)    

    return res