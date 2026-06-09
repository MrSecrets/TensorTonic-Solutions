import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x = np.asarray(x)

    pmf = np.where(x==1, p, 1-p)
    var = p*(1-p)

    # result = {
    #     "pmf" : pmf,
    #     "mean" : x
    #     "var" :var
    # }
    
    return (pmf, p, var)
    
    