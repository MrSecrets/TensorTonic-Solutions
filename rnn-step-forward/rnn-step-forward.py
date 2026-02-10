import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    x_t = np.asarray(x_t)
    h_prev = np.asarray(h_prev)
    Wx = np.asarray(Wx)
    Wh = np.asarray(Wh)
    b = np.asarray(b)

    a = np.matmul(x_t, Wx)
    c = np.matmul(h_prev, Wh)

    t = np.tanh(a + b + c)

    return t
