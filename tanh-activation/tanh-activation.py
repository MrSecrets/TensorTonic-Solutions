import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x)
    ex, ex_ = np.exp(x), np.exp(-x)

    tanh = (ex-ex_)/(ex+ex_)
    return tanh