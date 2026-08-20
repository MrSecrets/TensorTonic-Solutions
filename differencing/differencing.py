def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    for i in range(order):
        ans = []
        for j in range(len(series) - 1):
            ans.append(series[j+1]-series[j])
        series = ans

    return series