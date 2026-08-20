def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    n, k = len(values), len(weights)
    wma = [0]*(n-k+1)
    weight = sum(weights)

    for i in range(n-k+1):
        curr = 0
        for j in range(k):
            curr += weights[j] * values[i+j]
        wma[i] = curr/weight

    return wma