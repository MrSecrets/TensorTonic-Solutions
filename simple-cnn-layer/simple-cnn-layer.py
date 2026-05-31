import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    # Write code here
    N , C_in, xH, xW = x.shape
    C_out, _, KH, KW = W.shape
    H_out, W_out = xH-KH+1, xW-KW+1

    out = np.zeros((N,C_out, H_out, W_out))
    for n in range(N):
        for c_out in range(C_out):
            for i in range(H_out):
                for j in range(W_out):
                    patch = x[n, :, i:i+KH, j:j+KW]
                    patch = patch*W[c_out]
                    # patch = patch
                    out[n, c_out, i, j] = np.sum(patch)+b[c_out]

    return out


    