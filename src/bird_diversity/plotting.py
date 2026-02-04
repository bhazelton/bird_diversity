"""
Plotting functions.
"""

import matplotlib.pyplot as plt

def scatter(
    xvals: list[float],
    yvals: list[float],
    xlabel: str,
    ylabel: str,
):
    """
    Make a scatter plot.
    
    Parameters
    ----------
    xvals, yvals : array-like of float
        Values to scatter plot.
    xlabel, ylabel : str
        Descriptions to use as axis labels.

    """
    ax = plt.axes()
    ax.scatter(
        xvals,
        yvals,
    )
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)