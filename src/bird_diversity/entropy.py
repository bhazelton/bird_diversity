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
    if base == 2:
        items = probabilities * np.log2(probabilities)
    elif base == 10:
        items = probabilities * np.log10(probabilities)
    else:
        items = probabilities * np.log(probabilities)
    # don't keep NaNs -- they come from zeros, so do not contribute to the entropy
    new_items = []
    for item in items:
        if np.isnan(item):
            new_items.append(0)
        else:
            new_items.append(item)
    return np.abs(-np.sum(new_items))
