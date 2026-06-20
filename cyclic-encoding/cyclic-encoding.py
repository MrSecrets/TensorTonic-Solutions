import numpy as np
def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    n = len(values)
    values = np.asarray(values)
    theta = 2 * np.pi * values / period

    sine =  np.sin(theta)
    cose =  np.cos(theta)

    encoded = []
    for i in range(n):
        elem = [sine[i], cose[i]]
        encoded.append(elem)
    return encoded