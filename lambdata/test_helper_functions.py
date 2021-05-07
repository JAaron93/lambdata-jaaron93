"""
This .py file is for testing the two functions from helper_functions.py
"""

import pytest

from helper_functions import null_count, randomize, DF


def test_null_count():
    """Testing the null count function for helper_function"""

    assert null_count(df) == 2


def test_randomize():
    """Test the randomize function for helper_function"""

    new_DF = randomize(df, 42)
    assert len(new_df) == len(df)
    