import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code here
    x = np.asarray(x)
    dims  = len(x.shape)
    if dims!=3 and dims!=4:
        raise ValueError

    # print(x.shape)
    if dims==3:
        average = np.average(x, axis=(1,2))
        # print(average.shape)
        return average
    else:
        average = np.average(x, axis=(2,3))        
        return average
        
    return 0
    