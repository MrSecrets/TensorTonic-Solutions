import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    if rng is None:
        rng = np.random

    x = np.asarray(x)

    # rand = rng.random(x.shape)
    mask = (rng.random(x.shape) < (1-p))
    
    pattern = mask/(1-p)
    out = x*pattern
    # pattern = np.where(rand<p, 0, 1)

    return out, pattern