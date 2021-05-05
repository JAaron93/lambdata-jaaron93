"""Lambdata - Collection of Data Science Helper Functions"""

import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import pytest


# Confirms whether or not a DataFrame contains missing values
def null_count(df):
    """This function will return the number of null values contained
    within a DataFrame"""
    return df.isnull().sum().sum()


# Develops a randomized function that shuffles around a DataFrames cells before returning it.
# Function takes a randomized seed for reproducibility
def randomize(seed):
        """
        Randomize takes df and an integer as arguments before randomly
        shuffling dfs values
        """
        return shuffle(df, random_state=seed)

#   TODO - Implement more helper functions by Friday

