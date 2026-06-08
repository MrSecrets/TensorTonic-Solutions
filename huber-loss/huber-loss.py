import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    e = np.abs(y_true-y_pred)

    huber = np.where(e<=delta, e*e/2, delta*(e - delta/2))
    return np.mean(huber)