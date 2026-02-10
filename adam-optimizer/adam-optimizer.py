import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """

    n = len(param)
    mt = [0]*n
    vt = [0]*n
    paramt = [0]*n
    # mcapt = [0]*n
    # vcapt = [0]*n


    for i in range(n):

        mt[i] = beta1*m[i] + (1-beta1)*grad[i]
        vt[i] = beta2*v[i] + (1-beta2)*grad[i]*grad[i]

        mcapt = mt[i]/(1-beta1**t)
        vcapt = vt[i]/(1-beta2**t)

        paramt[i] = param[i] - lr*mcapt/(np.sqrt(vcapt) + eps)


    return paramt, mt, vt