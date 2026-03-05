import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    total = np.sum(p)
    if total != 1:
        raise ValueError
    
    xp = np.multiply(x, p)
    e = np.sum(xp)
    return e
