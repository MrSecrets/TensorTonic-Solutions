import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    a,b = len(x), len(y)
    if a!=b:
        raise ValueError
    
    dot = 0
    for i in range(a):
        dot += x[i]*y[i]
    return dot