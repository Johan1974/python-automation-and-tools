import os
import sys
import pandas as pd

# Add src folder to Python path so imports work
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, "../src")
sys.path.insert(0, src_dir)

from cleaner import (
    normalize_column_names,
    auto_detect_numeric,
    fill_strings,
    fill_numbers,
    remove_duplicates
)

def test_normalize_column_names():
    df = pd.DataFrame({" Name ": [1], " Age ": [2]})
    df = normalize_column_names(df)
    assert list(df.columns) == ["name", "age"]

def test_auto_detect_numeric():
    df = pd.DataFrame({"numbers": ["1", "2", "3"]})
    df = auto_detect_numeric(df)
    assert pd.api.types.is_numeric_dtype(df["numbers"])

def test_fill_strings():
    df = pd.DataFrame({"city": ["New York", None, ""]})
    df = fill_strings(df)
    assert all(df["city"] == ["New York", "Unknown", "Unknown"])

def test_fill_numbers():
    df = pd.DataFrame({"age": [10, None, 20]})
    df = fill_numbers(df, method="zero")
    assert df["age"].tolist() == [10, 0, 20]

def test_remove_duplicates():
    df = pd.DataFrame({"x": [1,1,2]})
    df = remove_duplicates(df)
    assert len(df) == 2
