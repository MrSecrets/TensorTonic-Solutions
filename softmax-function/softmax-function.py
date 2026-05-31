import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.asarray(x)

    if len(x.shape)==1:
        max_ = np.max(x)
        exp_x = np.exp(x-max_)
        deno = np.sum(exp_x)
    else:
        max_ = np.max(x, axis=1, keepdims=True)
        exp_x = np.exp(x-max_)
        deno = np.sum(exp_x, axis=1, keepdims=True)

    # print(max_, exp_x, deno)

    soft_max = exp_x/deno
    return soft_max