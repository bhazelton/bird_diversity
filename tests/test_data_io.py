"""
Tests for the entropy function
"""

from pathlib import Path

import numpy as np

from bird_diversity.data_io import read_bird_counts, read_foliage_density

bird_testfile = Path(__file__).parent.parent / "data/bird_census.csv"
foliage_testfile = Path(__file__).parent.parent / "data/foliage_density.csv"


def test_read_bird_counts():
    bird_df = read_bird_counts(bird_testfile)

    for site in bird_df:
        assert np.isclose(bird_df[site].sum(), 1)


def test_read_foliage_density():
    foliage_df = read_foliage_density(foliage_testfile)

    for site in foliage_df:
        assert np.isclose(foliage_df[site].sum(), 1)
