import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    # Write code here
    vocab_set = set()
    tf_dict = {}
    N = len(documents)
    pos = 0
    for i, document in enumerate(documents):
        words = document.lower().split()
        total_terms = len(words)
        counter = Counter(words)
        for key, val in counter.items():
            counter[key] = val/total_terms
            vocab_set.add(key)
        tf_dict[i] = counter

    vocab_list = sorted(list(vocab_set))
    vocab = {}
    for i, word in enumerate(vocab_list):
        vocab[word] = i
    
    token_count = len(vocab)
    tf = np.zeros((N, token_count))
    df = np.zeros((token_count))
    for d, counter in tf_dict.items():
        for key, val in counter.items():
            t = vocab[key]
            tf[d, t] = val
            df[t] += 1

    # idf = np.log((N+1)/(idf_before+1)) +1
    idf = np.log(N/df)

    
    tf_idf = tf*idf

    return tf_idf, vocab_list
    

    