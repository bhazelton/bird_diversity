"""
Read in the data.
"""

import pathlib

import numpy as np
import pandas as pd


def read_bird_counts(file: str | pathlib.Path) -> pd.DataFrame:
    """
    Read in the bird counts file and returns a dataframe with probabilities.

    Parameters
    ----------
    file : file, str, pathlib.Path, list of str, generator
        File containing bird counts to read in.

    Returns:
    --------
    bird_df : pd.DataFrame
        A dataframe with bird probabilities. Columns are sites, rows are species.
        Columns should sum to 1.

    """
    bird_df = pd.read_csv(file, header=0, index_col=0)
    # replace NaNs with zeros
    bird_df.fillna(0, inplace=True)

    # convert from counts to probilities
    for site in bird_df:
        bird_df[site] = bird_df[site] / bird_df[site].sum()

    return bird_df


def read_foliage_density(file: str | pathlib.Path) -> pd.DataFrame:
    """
    Read in the foliage density file and returns a dataframe with probabilities.

    Parameters
    ----------
    file : file, str, pathlib.Path, list of str, generator
        File containing bird counts to read in.

    Returns:
    --------
    foliage_df : pd.DataFrame
        A dataframe with foliage density probabilities. Columns are sites, rows
        are layers. Columns should sum to 1.

    """
    density_df = pd.read_csv(file, header=0, index_col=0)

    # setup df for total foliage, computed as a trapezoidal area:
    #  (height change) * (sum of densities at top & bottom) / 2
    total_df = pd.DataFrame(0, index=density_df.index, columns=density_df.columns)

    # add a zero row for area calc
    density_df.loc[0] = [0] * len(density_df.columns)
    density_df.sort_index()

    height_range = np.asarray(density_df.index[1:] - density_df.index[:-1])
    for site in density_df:
        density_sum = density_df[site][:-1].values + density_df[site][1:].values
        total_df[site] = (height_range * density_sum) / 2

    # convert to probability
    for site in total_df:
        total_df[site] = total_df[site] / total_df[site].sum()

    return total_df
