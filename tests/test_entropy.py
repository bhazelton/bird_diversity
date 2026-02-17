"""
Tests for the entropy function
"""

import pytest
import numpy as np

from bird_diversity.entropy import entropy


def test_smoke():
    """
    Simple smoke test to make sure function runs.
    """
    entropy([1])
    return


def test_args_dont_sum_to_1():
    """
    Edge test: ensure a ValueError raised if probabilities do not sum to one.
    """
    with pytest.raises(
        ValueError, match="The list of input probabilities does not sum to 1"
    ):
        entropy([0.9, 0.9])
    return


def test_args_out_of_range():
    """
    Edge test: ensure ValueError raised if probabilities are < 0 or > 1.
    """
    with pytest.raises(ValueError, match="At least one input is out of range"):
        entropy([-1, 2])
    return


def test_four_equal_likelihood_states():
    """
    One shot test: 4 states with equal probability in base 2. Should return 2 bits.
    """
    np.testing.assert_allclose(entropy([0.25, 0.25, 0.25, 0.25], base=2), 2.0)
    return


def test_ten_equal_likelihood_states():
    """
    One shot test: 10 states with equal probability in base 10. Should return 1.
    """
    np.testing.assert_allclose(entropy([0.1] * 10, base=10), 1.0)
    return


def test_equal_probability():
    """
    Pattern test: use the known relationship for equal probabilities.
    """

    def test(count, base):
        prob = 1.0 / count
        probabilities = np.repeat(prob, count)
        if base == 2:
            func = np.log2
        if base == 10:
            func = np.log10
        if base == "e":
            func = np.log
        assert np.isclose(entropy(probabilities, base=base), -func(prob))
        return

    # run the test for a large number of iterations
    for base in [2, 10, "e"]:
        for count in range(10, 100000, 10000):
            test(count, base)
    return


def test_invalid_base():
    """
    Edge test: ensure ValueError raised if base is not 2, 10 or "e".
    """
    with pytest.raises(ValueError, match="base must be one of: 2, 10 or 'e'"):
        entropy([1], base=3)
    return

