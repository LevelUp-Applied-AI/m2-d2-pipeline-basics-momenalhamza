"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    series = pd.Series([10, 20, np.nan, 40])

    cleaned = clean_column(series)

    assert cleaned.isna().sum() == 0
    assert cleaned.iloc[2] == 20

def test_compute_revenue():
    quantity = pd.Series([2, 3, 4])
    price = pd.Series([10, 5, 8])

    revenue = compute_revenue(quantity, price)

    expected = pd.Series([20, 15, 32])

    assert revenue.equals(expected)
