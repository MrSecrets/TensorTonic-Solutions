import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # # Write code here
    # anchor = np.reshape(np.asarray(anchor), (2,))
    # positive = np.reshape(np.asarray(positive), (2,))
    # negative = np.reshape(np.asarray(negative), (2,))

    anchor = np.asarray(anchor)
    positive = np.asarray(positive)
    negative = np.asarray(negative)

    axis = 1 if anchor.ndim == 2 else None
    dap = np.sum((anchor-positive)**2, axis=axis)
    dan = np.sum((anchor-negative)**2, axis=axis)

    L = np.maximum(0, dap-dan+margin)

    return np.mean(L)