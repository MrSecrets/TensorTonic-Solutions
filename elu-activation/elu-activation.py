import numpy as np
import math

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    x = np.asarray(x)
    elu = np.where(x<0, alpha*(np.exp(x) -1), x)
    return list(elu)