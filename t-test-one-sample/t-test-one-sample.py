import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    n = len(x)
    x = np.asarray(x)
    x_mean = np.mean(x)
    
    x_corrected = np.square(np.subtract(x, x_mean))
    x_corrected_sum = np.sum(x_corrected)
    s_square = x_corrected_sum/(n-1)
    s = np.emath.sqrt(s_square)

    t_num = x_mean - mu0
    t_deno= s/np.emath.sqrt(n)
    t = t_num/t_deno

    return t
