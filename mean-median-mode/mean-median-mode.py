import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """

    counter = Counter(x)
    mode, curr = 0, 0
    for key, val in counter.items() :
        if val>curr:
            mode, curr = key,val
    
    x = np.asarray(x)
    mean, median = np.mean(x), np.median(x)

    return mean, median, mode