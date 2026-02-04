"""
Tests for the entropy function
"""
from pathlib import Path

from bird_diversity.data_io import read_bird_counts

bird_testfile = Path(__file__).parent.parent / "data/bird_census.csv"

def test_read_bird_counts():
    bird_df = read_bird_counts(bird_testfile)

    for site in bird_df:
        assert bird_df[site].sum() == 1