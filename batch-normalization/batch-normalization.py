import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x = np.asarray(x)
    shape = x.shape
    dims = len(shape)
    if dims ==2:
        mean = np.mean(x, axis=0, keepdims=True)
        variance = np.var(x, axis=0, keepdims=True)
        x_cap = (x-mean)/np.sqrt(variance+eps)
        y = gamma*x_cap + beta
    elif dims==4:
        C = shape[1]
        gamma, beta = np.reshape(gamma, (1,C,1,1,)), np.reshape(beta, (1,C,1,1,))
        mean = np.mean(x, axis=(0,2,3), keepdims=True)
        variance = np.var(x, axis=(0,2,3), keepdims=True)
        x_cap = (x-mean)/np.sqrt(variance+eps)
        y = gamma*x_cap + beta

    return y
        