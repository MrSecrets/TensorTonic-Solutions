import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    d = len(X[0])
    w = np.zeros(d)
    b = 0
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    N = len(X)
    # print(X, y)
    for _ in range(steps):

        z = (np.matmul(X,w) + b)
        p = _sigmoid(z)

        # elem = 0
        # for i in range(N):
        #     Xi = X[i]
        #     yi = y[i]
        #     # zi = Xi*w + b
            
        #     # pi = _sigmoid(zi)
        #     pi = p[i]
            # if pi > 0:
                # print(pi)
            # elem = yi*np.log(pi) + (1-yi)* np.log(1-pi)
        diff = p-y
        # print("diff: ", diff.shape)
        # print("X: ", np.transpose(X).shape)
        grad_wLoss = np.matmul(np.transpose(X), diff)/ N
        grad_bLoss = np.sum(diff)/N

        # loss = -elem/N

        # print("w: ", w.shape)
        # print("gradw: ", grad_wLoss.shape)
        w -= lr*grad_wLoss
        b -= lr*grad_bLoss

    # print(type(w), type(float(b)))
    # print(d, w.shape)
    return (w, float(b))