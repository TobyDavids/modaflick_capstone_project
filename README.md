# ModaFlick Analysis & ETL Package

This repo contains the Jupyter notebook for the ModaFlick case study and a local Python package `modaflick_etl` for reusable ETL functions, including optional database creation.

## Quickstart (macOS)

```bash
# 1) Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) (Optional) Create DB if it doesn't exist (uses env or defaults)
python -c "from modaflick_etl.db import create_database_if_not_exists; print('Created:', create_database_if_not_exists())"
```

## Environment Variables
Create a `.env` file (not committed) or export shell variables:

- `DB_NAME` (default: `modaflick`)
- `DB_USER` (default: `postgres`)
- `DB_PASSWORD` (default: `admin`)
- `DB_HOST` (default: `localhost`)
- `DB_PORT` (default: `5432`)

## Example Usage in Notebook

```python
from modaflick_etl import extract, transform, load, config, db

# Ensure DB exists
db.create_database_if_not_exists()

CONN = config.conn_string()

# Extract
customers = extract.from_csv('customers.csv')
orders = extract.table_from_postgres('orders', CONN)

# Transform
customers = transform.remove_duplicates(customers)
customers = transform.convert_to_datetime(customers, ['signup_date'])

# Load
load.to_postgres(customers, 'customers', CONN, if_exists='replace')
```

## Structure
```
modaflick_etl/
  __init__.py
  config.py
  db.py
  extract.py
  transform.py
  load.py
  utils.py
modaflick_analysis.ipynb
requirements.txt
.gitignore
README.md
```
