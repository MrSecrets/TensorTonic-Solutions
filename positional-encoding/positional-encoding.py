import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here

    pos = np.arange(0, seq_len)
    
    if d_model%2 == 1:
        model_len = d_model+1
    else:
        model_len = d_model
    
    i = np.arange(0, model_len, 2) 
    base_term = base ** (i / d_model)
    angles = pos[:, np.newaxis] / base_term
    pe = np.zeros((seq_len, d_model))
    # pe[:, 0::2] = np.sin(pos, base_term)
    # pe[:, 1::2] = np.cos(pos, base_term)
    pe[:, 0::2] = np.sin(angles[:, :pe[:, 0::2].shape[1]])
    pe[:, 1::2] = np.cos(angles[:, :pe[:, 1::2].shape[1]])
    
    return pe