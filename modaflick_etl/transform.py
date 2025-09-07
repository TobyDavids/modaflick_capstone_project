import pandas as pd
from typing import Iterable

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()

def convert_to_datetime(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df

def handle_missing_values(df: pd.DataFrame, strategy: str = "ignore") -> pd.DataFrame:
    if strategy == "drop":
        return df.dropna()
    if strategy == "fill_zero":
        return df.fillna(0)
    return df

def left_join(left: pd.DataFrame, right: pd.DataFrame, on: str) -> pd.DataFrame:
    return left.merge(right, on=on, how="left")
