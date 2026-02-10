def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    n, m  = len(X), len(X[0])
    output = []
    i= 0
    while i+pool_size<=n:
        j = 0
        pooled = []
        while j+pool_size<=m:
            max_ = float('-inf')
            for r in range(i, i+pool_size):
                if r<n:
                    for c in range(j, j+pool_size):
                        if c<m:
                            max_ = max(max_, X[r][c])
            pooled.append(max_)
            j+=pool_size
        output.append(pooled)
        i+=pool_size
    
    return output