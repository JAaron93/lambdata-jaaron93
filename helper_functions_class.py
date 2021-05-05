"""Lambdata - Collection of Data Science Helper Functions"""

import pandas as pd
import numpy as np
from sklearn.utils import shuffle

# Creating a Class


class CleanData:
    def__init__(self):
        """
        Init function for instantiation of objects
        """
        return


# Confirms whether or not a DataFrame contains missing values
    def null_count(self, df):
        """
        This function will return the number of null values contained
        within a DataFrame
        """
        return df.isnull().sum().sum()

    # Randomizer
    def randomize(self, df, seed):
        """
        What it does is stated by the comment
        """
        randomized = shuffle(
                             df,
                             random_state=seed
                             )
        return randomized
