import numpy as np

def _sigmoid(x):
    """Numerically stable sigmoid function"""
    return np.where(x >= 0, 1.0/(1.0+np.exp(-x)), np.exp(x)/(1.0+np.exp(x)))

def _as2d(a, feat):
    """Convert 1D array to 2D and track if conversion happened"""
    a = np.asarray(a, dtype=float)
    if a.ndim == 1:
        return a.reshape(1, feat), True
    return a, False

def gru_cell_forward(x, h_prev, params):
    """
    Implement the GRU forward pass for one time step.
    Supports shapes (D,) & (H,) or (N,D) & (N,H).
    """
    # Write code here
    x, h_prev = np.asarray(x), np.asarray(h_prev)

    z_t = _sigmoid(
        x@np.asarray(params["Wz"]) + 
        h_prev@np.asarray(params["Uz"]) + 
        np.asarray(params["bz"])
        )

    r_t = _sigmoid(
        x@np.asarray(params["Wr"]) + 
        h_prev@np.asarray(params["Ur"]) + 
        np.asarray(params["br"])
        )

    h_t = np.tanh(
        x@np.asarray(params["Wh"]) + 
        (np.multiply(r_t, h_prev))@np.asarray(params["Uh"]) + 
        np.asarray(params["bh"])
    )

    h_new = (
        np.multiply(1-z_t, h_prev) + 
        np.multiply(z_t, h_t)
    )

    return h_new