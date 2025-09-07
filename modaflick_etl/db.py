from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from typing import Optional
from . import config

def create_database_if_not_exists(
    dbname: Optional[str] = None,
    user: Optional[str] = None,
    password: Optional[str] = None,
    host: Optional[str] = None,
    port: Optional[str] = None,
) -> bool:
    """Create the database if it does not already exist.
    Returns True if created, False if it already existed.
    """
    dbname = dbname or config.DB_NAME
    user = user or config.DB_USER
    password = password or config.DB_PASSWORD
    host = host or config.DB_HOST
    port = port or config.DB_PORT

    # Connect to default 'postgres' DB to run CREATE DATABASE
    conn = connect(database="postgres", user=user, password=password, host=host, port=port)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (dbname,))
    exists = cur.fetchone()
    created = False
    if not exists:
        # Quote dbname to allow names with hyphens etc.
        cur.execute(f'CREATE DATABASE "{dbname}"')
        created = True
    cur.close()
    conn.close()
    return created
