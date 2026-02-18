import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    N = len(seqs)
    L = max_len if max_len else max(len(seq) for seq in seqs)
    result = np.full((N,L), pad_value)

    # for i in range(N):
    #     result[i] = seqs[i]

    for i, s in enumerate(seqs):
        n = len(s)
        if n < L:
            result[i, :n] = s
        else:
            result[i, :L] = s[:L]


    return result