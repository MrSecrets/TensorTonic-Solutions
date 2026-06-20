def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    counter = {}
    for v in values:
        curr = counter.get(v, 0)
        counter[v] = curr+1

    counter_list = sorted(counter.items())

    i=0
    for (key, value) in counter_list:
        rank = ((i+1) + (i+value))/2            
        counter[key] = rank
        i+=value

    encoded = []
    for v in values:
        encoded.append(counter[v])
    return encoded