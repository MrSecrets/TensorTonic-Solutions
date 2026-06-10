import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    matrix = np.asarray(matrix, dtype='float64')
    # n = matrix.ndim
    if axis != None and axis>=matrix.ndim:
        return None
    elif matrix.ndim!=2:
        return None
    base = 1
    match norm_type:
        case "l2":
            base = np.sqrt(np.sum(matrix**2, keepdims=True, axis=axis))
        case "l1":
            base = np.sum(np.abs(matrix), keepdims=True, axis=axis)
        case "max":
            base = np.max(np.abs(matrix), keepdims=True, axis=axis)
        case _:
            return None

    # print(base)
    normalized = np.divide(matrix, base, out=np.zeros_like(matrix), where=base!=0)
    return normalized