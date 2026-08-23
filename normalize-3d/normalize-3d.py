import numpy as np

def normalize_3d(v: list) -> np.ndarray:
    """Return unit-length 3D vectors while preserving zero vectors."""
    # Write code here
    v = np.asarray(v)
    n = v.ndim
    if n==1:
        norm = np.sqrt(np.sum(v**2))
    else: 
        norm_s = np.sum(v**2, axis=1, keepdims=True)
        norm = np.sqrt(norm_s)

    normalize = np.divide(v, norm, out=np.float64(np.zeros_like(v)), where=norm!=0)
    return  normalize
    