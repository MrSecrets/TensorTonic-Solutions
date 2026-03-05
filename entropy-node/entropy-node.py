import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    val, counts = np.unique(y, return_counts=True)
    # print(val, count)

    p = counts / np.sum(counts)

    h = np.sum(p * np.log2(p))
    
    return -h