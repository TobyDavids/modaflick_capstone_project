from sqlalchemy import create_engine
import pandas as pd
from typing import Optional

def to_postgres(
    df: pd.DataFrame,
    table_name: str,
    connection_string: str,
    if_exists: str = "replace",
    dtype: Optional[dict] = None,
) -> None:
    engine = create_engine(connection_string)
    df.to_sql(table_name, engine, if_exists=if_exists, index=False, dtype=dtype)
    print(f"Table '{table_name}' uploaded successfully.")
