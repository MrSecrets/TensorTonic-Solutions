import math

def winsorize(values, lower_pct, upper_pct):
    """
    Clip values at the given percentile bounds.
    """
    v_sorted = sorted(values)
    n = len(values)
    l_k = (n-1)*lower_pct/100 
    l_bound = v_sorted[math.floor(l_k)] + (l_k-math.floor(l_k))*(v_sorted[math.ceil(l_k)] - v_sorted[math.floor(l_k)])

    u_k = (n-1)*upper_pct/100
    u_bound = v_sorted[math.floor(u_k)] + (u_k-math.floor(u_k))*(v_sorted[math.ceil(u_k)] - v_sorted[math.floor(u_k)])

    # print(l_bound, u_bound)
    for i in range(n):
        if values[i]<l_bound:
            values[i] = l_bound
        elif values[i]>u_bound:
            values[i] = u_bound

    # print(l_bound, u_bound, lower_pct, upper_pct, values)
    return values