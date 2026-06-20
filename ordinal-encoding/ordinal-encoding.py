def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here
    ordinals = {}
    i = 0
    for elem in ordering:
        ordinals[elem] = i
        i+=1

    encoded = []
    for value in values:
        encoded.append(ordinals[value])

    return encoded
    