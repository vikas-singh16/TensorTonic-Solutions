import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    sample_mean = np.mean(x)
    _len = len(x)
    sample_std = np.sqrt(np.sum((x-sample_mean)**2)/(_len - 1))

    t = (sample_mean - mu0)/(sample_std/np.sqrt(_len))

    return t