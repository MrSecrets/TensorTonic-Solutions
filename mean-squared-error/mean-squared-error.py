import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_p, y_t = np.asarray(y_pred), np.asarray(y_true)

    sqr = (y_p-y_t)**2
    n = y_p.shape[0]
    mse = np.sum(sqr)/n
    return mse
