import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    if X.ndim!=2:
        return None

    N, _ = X.shape
    if N<2:
        return None

    meu = np.mean(X, axis=0)
    # print("X",X)
    X = X-meu

    # print(N, D, meu.shape)
    # print("meu", meu)
    # print("X_new", X)
    # print(X)
    sigma = np.matmul(np.transpose(X), X)
    sigma = sigma/(N-1)
    # print(sigma.shape)
    # print("sigma", sigma)
    return sigma