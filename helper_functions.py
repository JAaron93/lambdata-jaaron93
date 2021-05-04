"""Lambdata - Collection of Data Science Helper Functions"""

import pandas as pd
import numpy as np
import pytest
from sklearn.model_selection import train_test_split

def null_count(df):
    """This function will return the number of null values contained within a DataFrame"""
    return df.isnull().sum().sum()


def train_test_split(df, frac):
    """Create a Train/Test split function for a dataframe and returns both the Training and Testing sets.""" 
    """Frac referes to the precent of data you would like to set aside for training."""
    train, test = train_test_split(
                                   df,
                                   train_size=frac,
                                   test_size=.20,
                                   shuffle=True, 
                                   random_state=72
                                   )
                                   
    return train, test 