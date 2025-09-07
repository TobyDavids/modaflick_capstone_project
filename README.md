# ModaFlick Analysis & ETL Package

This repo contains the Jupyter notebook for the ModaFlick case study and a local Python package `modaflick_etl` for reusable ETL functions, including optional database creation.

# Project Overview

ModaFlick is a growing fashion brand. The goal of this project was to:

1. Create a database to centralize customer, order, product, and inventory data.

2. Extract & load data from PostgreSQL, CSV files, and Google Sheets.

3. Clean & transform datasets to prepare for analysis.

4. Analyze sales, customers, and inventory to uncover actionable insights.

5. Provide strategic business recommendations.

#Key Insights

- Top-selling products contributed the majority of revenue, with a few items dominating sales volume.

- Physical stores outperformed online sales, both in revenue and order frequency, indicating customer preference for in-store experiences.

- Average Order Value (AOV) varied significantly across cities and age groups, with younger demographics and urban locations generating higher revenue.

- Several popular products are at risk of stock-outs, as their demand exceeds available inventory levels.

- Male customers contributed ~2x the revenue of female customers, highlighting an opportunity to increase female customer engagement.

#Recommendations

1. Focus marketing campaigns on top-performing products and replicate their success across underperforming items.
2. Reallocate inventory to avoid low-stock issues for high-demand products.
3. Enhance the online shopping experience (e.g., discounts, delivery perks) to close the gap with physical store sales.
4. Target urban cities and high-value age groups with personalized offers to maximize AOV.
5. Develop engagement strategies for female customers, including tailored promotions and product lines.

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
