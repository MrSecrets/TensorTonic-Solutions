import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.asarray(x)
    q = np.asarray(q)

    perce = np.percentile(x, q, method='linear')
    return perce