"""Lambdata - Collection of Data Science Helper Functions"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import pytest


# Confirms whether or not a DataFrame contains missing values
def null_count(df):
    """This function will return the number of null values contained
    within a DataFrame"""
    return df.isnull().sum().sum()

# Adress Split 
def addy_split(addy_series):
    """Splits addresses into these three columns (df['city'], df['state'],
    & df['zip']"""
    cities = []
    states = []
    zips = []
    for addy in addy_series:
        split_addy_1 = addy.split(",")
        cities.append(split_addy_1[0].split("\n")[1])
        states.append(split_addy_1[1].split(" ")[1])
        zips.append(split_addy_1[1].split(" ")[2])

    df = pd.DataFrame({
                       "city": cities,
                       "state": states,
                       "zip": zips
                       })
    return df

# Third function. Train Test Split
def train_test_split(df, frac):
    """Create a train/test split function for a data frame that returns both the
    training and test sets.  'frac' refers to the percent of data you would
    like to set aside for training"""
    cutoff = df.index < int(df.shape[0] * frac)
    df_train = df.loc[cutoff]
    df_test = df.loc[~cutoff]
    return df_train, df_test

#   TODO - Implement more helper functions by Friday

