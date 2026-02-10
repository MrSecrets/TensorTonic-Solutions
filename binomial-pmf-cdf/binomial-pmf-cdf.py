import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    pmf = comb(n,k, exact=True) * (p**k) * ((1-p)**(n-k))

    cdf = 0
    for i in range(k):
        cdf_elem = comb(n, i, exact=True) * (p**i) * ((1-p)**(n-i))
        cdf += cdf_elem
    cdf += pmf 
    
    return (pmf, cdf)