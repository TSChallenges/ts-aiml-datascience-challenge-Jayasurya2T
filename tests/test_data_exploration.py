# tests/test_data_exploration.py

import pytest
import pandas as pd
from src.data_exploration import load_data, check_missing_values, generate_summary_statistics

def test_load_data():
    df = load_data('data/bank_churn.csv')
    assert isinstance(df, pd.DataFrame), "Data should be loaded into a pandas DataFrame"


def test_missing_values():
    df = load_data('data/bank_churn.csv')
    # You can call the actual function to test
    check_missing_values(df)
    missing = df.isnull().sum()
    assert missing.sum() == 0, "There should be no missing values in the dataset"

def test_summary_statistics():
    df = load_data('data/bank_churn.csv')
    summary = df.describe()
    # Check if key columns exist in the original DataFrame
    assert 'age' in df.columns, "DataFrame should include 'Age' column"
    assert 'balance' in df.columns, "DataFrame should include 'Balance' column"

