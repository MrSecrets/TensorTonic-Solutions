import numpy as np
from scipy.special import factorial

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    cdf = 0
    i = np.arange(0, k+1)
    pi_num = np.exp(-lam) * (lam**i)
    pi_den = factorial(i)

    pmf = pi_num[-1]/pi_den[-1]
    cdf = sum(pi_num/pi_den)

    return pmf, cdf