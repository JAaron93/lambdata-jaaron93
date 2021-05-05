"""Lambdata - Collection of Data Science Helper Functions"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle


# Confirms whether or not a DataFrame contains missing values
def null_count(df):
    """This function will return the number of null values contained
    within a DataFrame"""
    return df.isnull().sum().sum()

# Train Test Split   
def train_test_split(df, frac):
    """This function splits data using train_test_split and returns two sets"""
    train, test = train_test_split(
                                   df,
                                   train_size=frac,
                                   random_state =42
                                   )
    return (train, test)

# Randomizer
def randomize(df, seed):
    """What it does is in the comment"""
    randomized = shuffle(
                         df,
                         random_state=seed
                         )
    return randomized

#   TODO - Implement more helper functions by Friday

