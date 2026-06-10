import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    g = np.asarray(g)
    norm = np.linalg.norm(g)

    if norm>max_norm and norm>0 and max_norm>0:
        g = g*(max_norm/norm)
    return g