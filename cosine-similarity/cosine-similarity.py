import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.asarray(a)
    b = np.asarray(b)

    nume = np.dot(a, b)
    # print(nume)
    denoa = np.linalg.norm(a)
    denob = np.linalg.norm(b)
    deno = denoa*denob
    # print(deno)
    # return nume/deno
    if deno == 0:
        return 0
    return nume/deno
