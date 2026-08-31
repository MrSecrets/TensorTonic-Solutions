def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """
    # Write code here
    stop = set(stopwords)
    # output = []
    # for token in tokens:
    #     if token not in stop:
    #         output.append(token)

    return [token for token in tokens if token  not in stop]
    