import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    n = len(x)
    x = np.asarray(x)
    x_ = np.mean(x)
    var = np.sum(np.square(x-x_))/(n-1)
    std = np.sqrt(var)
    return (var, std)