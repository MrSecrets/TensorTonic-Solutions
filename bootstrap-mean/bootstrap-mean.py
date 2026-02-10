import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    x = np.asarray(x)
    boot_means = np.zeros(n_bootstrap)
    D = x.shape[0]
    if rng is None:
        rng = np.random.default_rng()

    for i in range(n_bootstrap):
        idx = rng.integers(low=0, high=D, size=D)
        boot_means[i] = x[idx].mean()
    
    alpha = (1-ci)/2
    lower = np.quantile(boot_means, alpha)
    upper = np.quantile(boot_means, 1-alpha)

    return (boot_means, lower, upper)