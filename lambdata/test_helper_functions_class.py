"""
This .py file is for testing the two functions from helper_functions.py
"""

import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import pytest
from lambdata.helper_functions_class import CleanData

# Reference Dataframe for CleanData testing
df = pd.DataFrame(
    np.array(
             [
              [1, np.nan, 3, 4, np.nan],
              [4, np.nan, 6, np.nan, 42],
              [7, 8, np.nan, 27, 72]
             ]
            ),
    columns=['A', 'B', 'C', 'D', 'E']
                  )


# Testing CleanData class
def test_type_int():
    '''
    Confirming that null_count returns an int
    '''
    null_count = CleanData().null_count(df)
    assert isinstance(null_count, np.int64)


def test_null_count():
    '''
    Confirming that null_count returns correct number of missing values
    '''
    null_count = CleanData().null_count(df)
    assert null_count == 2


def test_randomize():
    '''
    Confirming length of randomized df
    '''
    df_random = CleanData().randomize(df, 27)
    assert len(df_random) == len(df)
