import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    
    # method 1
    # n = len(v)
    # diag_matrix = np.zeros((n,n))
    # for i in range(n):
    #     diag_matrix[i,i] = v[i]
    # return diag_matrix
    
    # method 2
    diag_matrix = np.diag(v)
    return diag_matrix
    
