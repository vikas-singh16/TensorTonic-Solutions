import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    mean = np.mean(x)
    _len = len(x)
    std = np.sqrt(np.sum((x-mean) **2)/(_len - 1))
    var = std **2
    return  var, std