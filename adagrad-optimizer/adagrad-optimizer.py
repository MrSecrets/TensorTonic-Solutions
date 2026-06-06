import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    # Write code here
    Gt = G + np.square(g)
    wt = w - np.multiply(np.divide(lr, np.sqrt(Gt + eps)), g)

    return (wt, Gt)