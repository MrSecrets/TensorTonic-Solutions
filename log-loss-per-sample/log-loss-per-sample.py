import math
import numpy as np 

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    p_cap = np.clip(y_pred, eps, 1-eps)

    log_lss = - (y_true*np.log(p_cap) + (1-y_true)*(np.log(1-p_cap)))
    return list(log_lss)