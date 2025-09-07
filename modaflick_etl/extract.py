import pandas as pd
from sqlalchemy import create_engine
from typing import Optional

def from_csv(path: str, **read_csv_kwargs) -> pd.DataFrame:
    return pd.read_csv(path, **read_csv_kwargs)

def from_excel(path: str, **read_excel_kwargs) -> pd.DataFrame:
    return pd.read_excel(path, **read_excel_kwargs)

def from_google_sheet(sheet_id: str, format: str = "csv") -> pd.DataFrame:
    if format not in ("csv", "xlsx"):
        raise ValueError("Unsupported format. Use 'csv' or 'xlsx'.")
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format={format}"
    if format == "csv":
        return pd.read_csv(url)
    return pd.read_excel(url)

def from_postgres(query: str, connection_string: str) -> pd.DataFrame:
    engine = create_engine(connection_string)
    return pd.read_sql(query, engine)

def table_from_postgres(table: str, connection_string: str) -> pd.DataFrame:
    engine = create_engine(connection_string)
    return pd.read_sql(f"SELECT * FROM {table};", engine)
