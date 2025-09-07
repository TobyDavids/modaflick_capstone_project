import os

# Read DB settings from environment variables (recommended) with sensible defaults for local dev.
DB_NAME = os.getenv("DB_NAME", "modaflick")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

def conn_string(dbname: str | None = None, driver: str = "postgresql+psycopg2") -> str:
    """Return a SQLAlchemy connection string for the target database."""
    name = dbname or DB_NAME
    return f"{driver}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{name}"
