def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    n = len(values)
    odd = True if window_size%2==1 else False
    medians = []
    mid = window_size//2
    for i in range(n-window_size+1):
        curr = values[i:i+window_size]
        curr.sort()
        if odd:
            medians.append(curr[mid])
        else:
            medians.append((curr[mid] + curr[mid-1])/2)
    return medians
        