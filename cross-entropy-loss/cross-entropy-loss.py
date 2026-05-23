import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    n = len(y_true)
    indexing = np.arange(n)

    y_pred = np.asarray(y_pred)
    probs = y_pred[indexing, y_true]

    loss = -1* np.log(probs)
    cross_entropy = np.mean(loss)
    return cross_entropy