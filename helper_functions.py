"""Lambdata - Collection of Data Science Helper Functions"""

import pandas as pd
import numpy as np
import pytest
from sklearn.model_selection import train_test_split

# Confirms whether or not a DataFrame contains missing values
def null_count(df):
    """This function will return the number of null values contained
    within a DataFrame"""
    return df.isnull().sum().sum()


# Train/Test split fuction for a DataFrame that returns both training and test sets
def train_test_split(df, frac):
    """Create a Train/Test split function for a dataframe and returns both
    the Training and Testing sets."""
    """Frac referes to the precent of data you would like to set aside for
     training."""
    train, test = train_test_split(
                                   df,
                                   train_size=frac
                                   )

    return train, test


# Randomized function that randomizes all of a DataFrames cells before returning it
def randomize(df, seed):
    df = df.sample(
                   frac = 1,
                   axis = 1,
                   random_state = 42).sample(
                                            frac = 1,
                                            random_state = 59
                                            ).reset_index(drop = True)
    return df


