import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    # Write code here
    X_2 = np.square(X)
    distance_square = np.sum(X_2, axis=1, keepdims=True) + np.sum(X_2, axis=1) -2*np.dot(X,X.T)
    dist = np.sqrt(distance_square)

    n = X.shape[0]
    a = np.zeros(n)
    b = np.full(n, np.inf)

    ulabels = np.unique(labels)
    clusters = len(ulabels)

    for i in range(n):
        current_label = labels[i]
        mask = (labels==current_label)
        mask[i] = False

        if np.sum(mask)>0:
            a[i] = np.mean(dist[i, mask])
        else:
            a[i] = 0

        for other_label in ulabels:
            if other_label == current_label:
                continue
            else:
                other_mask = (labels==other_label)
                mean_dist = np.mean(dist[i, other_mask])
                b[i] = min(b[i], mean_dist)

            
    max_ab = np.maximum(a, b)
    sil_samples = np.where(max_ab > 0, (b - a) / max_ab, 0.0)
    ans = np.mean(sil_samples)
    return ans
    
    