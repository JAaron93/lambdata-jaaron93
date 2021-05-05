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
    arr_rand = np.random.rand(df.shape[0])
    split = arr_rand < np.percentile(arr_rand, (frac*100))
    df_test = df[split]
    df_train = df[~split]
    return df_train, df_test


