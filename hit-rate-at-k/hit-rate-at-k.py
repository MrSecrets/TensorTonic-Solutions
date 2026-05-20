def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    users = len(ground_truth)
    if users == 0:
        return 0

    count = 0
    for i in range(users):
        recom = set(recommendations[i][:k])
        input = set(ground_truth[i])

        intersect = not recom.isdisjoint(input)
        if intersect:
            count+=1

    return count/users