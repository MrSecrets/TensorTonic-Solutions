import math
import numpy as np 

def cosine_embedding_loss(x1: list, x2: list, label: int, margin: float) -> float:
    """
    Returns the cosine embedding loss as a float.
    """
    # Write code here
    x1, x2 = np.asarray(x1), np.asarray(x2)
    cos_x12  = np.dot(x1, x2) / (np.linalg.norm(x1) * np.linalg.norm(x2))
    
    L = 0
    if label == 1:
        L = 1-cos_x12
    else:
        L = max(0, cos_x12-margin)
    return L