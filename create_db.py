import pandas as pd
from sqlalchemy import create_engine

print("=" * 60)
print("DATABASE CREATION STARTED")
print("=" * 60)

# Create SQLite database
engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

print("Database created.")

# Load cleaned files
nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

transactions = pd.read_csv(
    "data/processed/transactions_clean.csv"
)

performance = pd.read_csv(
    "data/processed/performance_clean.csv"
)

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

# Save to database
fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("dim_fund:", len(fund_master))
print("fact_nav:", len(nav))
print("fact_transactions:", len(transactions))
print("fact_performance:", len(performance))

print("\nDatabase loaded successfully.")

print("=" * 60)
print("DATABASE CREATION COMPLETED")
print("=" * 60)