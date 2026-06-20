import numpy as np
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    values = np.asarray(values)
    values = np.log(values+1)
    return values