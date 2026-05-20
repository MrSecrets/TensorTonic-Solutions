import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    n = len(y_true)
    
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    equality = y_true==y_pred
    tp = np.sum(equality)

    f1 = tp/(n)

    return f1