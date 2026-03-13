import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    # Your code here

    if d_model%2 == 1:
        model_len = d_model+1
    else:
        model_len = d_model
    
    i = np.arange(0, model_len, 2) 
    
    base =  10000
    base_term = base ** (i / d_model)

    pos = np.arange(0, seq_length)
    
    angles = pos[:, np.newaxis] / base_term
    
    pe = np.zeros((seq_length, d_model))
    pe[:, 0::2] = np.sin(angles[:, :pe[:, 0::2].shape[1]])
    pe[:, 1::2] = np.cos(angles[:, :pe[:, 1::2].shape[1]])

    return pe