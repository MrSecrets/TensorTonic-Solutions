import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    y_mean = np.mean(y_true, keepdims=True)

    ss_tot = np.sum(np.square(y_true-y_mean))
    if ss_tot == 0:
        return 1.0 if np.array_equal(y_true, y_pred) else 0.0
    ss_res = np.sum(np.square(y_true-y_pred))
    
    r2 = 1 - (ss_res/ss_tot)
    return r2