"""
Compute the Shannon entropy of a list of probabilities.
"""
from typing import Literal

import numpy as np


def entropy(probabilities: list[float], base: Literal[2, 10, "e"] = 2) -> float:
    """
    Compute the Shannon entropy of a list of probabilities.

    The input list of probabilities must sum to one and no
    element should be larger than 1 or less than 0.

    Parameters
    ----------
    probabilities : list of float
        List probabilities.
    base : 2, 10 or "e"
        Logarithm base to use. Should be one of: 2, 10 or "e" for log base 2,
        log base 10 or natural log.

    """
    if base not in [2, 10, "e"]:
        raise ValueError("base must be one of: 2, 10 or 'e'")
    if any([(prob < 0.0) or (prob > 1.0) for prob in probabilities]):
        raise ValueError("At least one input is out of range [0...1]")
    else:
        pass
    if not np.isclose(1, np.sum(probabilities), atol=1e-08):
        raise ValueError("The list of input probabilities does not sum to 1")
    else:
        pass
    # remove the zeros -- they cause NaNs in the logs but should not contribute
    # to the entropy

    non_zero_probs = np.asarray(probabilities)[np.nonzero(probabilities)]
    if base == 2:
        items = non_zero_probs * np.log2(non_zero_probs)
    elif base == 10:
        items = non_zero_probs * np.log10(non_zero_probs)
    else:
        items = non_zero_probs * np.log(non_zero_probs)
    return np.abs(-np.sum(items))
