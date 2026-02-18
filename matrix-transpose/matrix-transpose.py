import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.asarray(A)
    n,m = A.shape

    AT = np.zeros((m,n))

    for i in range(n):
        AT[:, i] = A[i]
    
    return AT
