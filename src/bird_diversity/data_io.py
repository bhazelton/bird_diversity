"""
Read in the data.
"""
import pathlib

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