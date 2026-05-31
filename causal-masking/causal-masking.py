import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    # Write code here
    seq_len = scores.shape[-1]
    mask = np.triu(np.ones((seq_len, seq_len), dtype=bool), k=1)
    casual_mask = np.where(mask, mask_value, scores)

    return casual_mask