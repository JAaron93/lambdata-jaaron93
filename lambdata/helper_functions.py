"""
This .py file contains two functions for common data cleaning tasks. These functions can be used with
data loaded into a pandas DataFrame.
"""

import pandas as pd
import numpy as np
from sklearn.utils import shuffle


# Confirms whether or not a DataFrame contains missing values
def null_count(df):
    """
    This function will return the number of null values contained
    within a DataFrame
    """
    return df.isnull().sum().sum()

# Randomizer
def randomize(df, seed):
    """
    Eponymous Comment. Function will return a reproducible
    randomized varibale via a seed. Shuffle from sklearn and it's
    random_state parameter do the heavy lifting
    """
    randomized = shuffle(
                         df,
                         random_state=seed
                         )
    return randomized
