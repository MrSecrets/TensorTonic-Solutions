import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    s = np.asarray(s)
    
    s = beta*s + (1-beta)*np.multiply(g, g)
    w = w - np.multiply((lr/np.sqrt((s + eps))), g)

    return w,s