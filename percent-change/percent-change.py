def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    pct = []
    n = len(series)
    for i in range(1, n):
        if series[i-1] == 0:
            pct.append(0.0)
        else:
            p = (series[i] - series[i-1])/series[i-1]
            pct.append(p)

    return pct