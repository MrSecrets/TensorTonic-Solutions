def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    recom = set()
    for row in recommendations:
        recom.update(row)
    

    return len(recom)/n_items