def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here

    n = len(tokens)

    step = chunk_size - overlap
    start = 0
    res = []
    while start<n:
        end = start+chunk_size
        if end<n:
            elem = tokens[start:end]
        else:
            elem = tokens[start:]
        res.append(elem)
        start = end-overlap
        if end >= n:
            break
    # print(tokens, chunk_size, overlap, res)
    return res