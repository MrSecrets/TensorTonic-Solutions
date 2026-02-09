def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here

    tree = len(predictions)
    samples = len(predictions[0])
    preds = []

    for i in range(samples):
        votes = {}
        for t in range(tree):
            label =  predictions[t][i]
            if label not in votes:
                votes[label] = 1
            else:
                votes[label]+=1
        winner = max(votes.items(), key=lambda x: (x[1], -x[0]))[0]
        preds.append(winner)
    # max_ = max(votes)
    # for i, vote in enumerate(votes):
    #     if vote==max_:
    #         return i
    return preds