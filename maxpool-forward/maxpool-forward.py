def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
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
            j+=stride
        output.append(pooled)
        i+=stride
    
    return output