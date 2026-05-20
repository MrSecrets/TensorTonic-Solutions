def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = set(recommended[:k])
    relevan = set(relevant)

    intersect = top_k.intersection(relevan)
    precision = len(intersect)/k
    recall = len(intersect)/len(relevant)
    return [precision, recall]
    