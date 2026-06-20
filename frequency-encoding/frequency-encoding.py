def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    count = {}
    for value in values:
        if value in count:
            count[value]+=1
        else:
            count[value]=1

    n = len(values)
    for key, value in count.items():
        count[key] = value/n
        
    encoded = []
    for value in values:
        encoded.append(count[value])

    return encoded
        

    