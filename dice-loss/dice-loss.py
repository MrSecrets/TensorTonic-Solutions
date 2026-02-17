import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    p = np.asarray(p)
    y = np.asarray(y)
    py = np.multiply(p, y)
    
    sum_p = np.sum(p)
    sum_y = np.sum(y)
    sum_py = np.sum(py)

    dice = (2*sum_py + eps)/(sum_p + sum_y + eps)
    return 1-dice
    
    
    