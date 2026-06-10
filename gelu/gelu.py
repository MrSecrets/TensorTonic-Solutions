import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x = np.asarray(x)
    verf = np.vectorize(math.erf)
    erfterm = verf(x/math.sqrt(2))
    # print(erf)
    gelu = x*(1+erfterm)/2
    return gelu
    # return [0]
    
