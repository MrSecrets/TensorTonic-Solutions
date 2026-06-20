def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    w =1.0
    W = []
    for r in returns:
        w = w*(1+r)
        W.append(w-1)
    return W
    