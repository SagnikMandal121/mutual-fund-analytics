import pandas as pd

print("="*60)
print("DATA CLEANING STARTED")
print("="*60)

# NAV HISTORY

nav = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

print("\nCleaning NAV history...")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
    .ffill()
)

nav = nav[nav["nav"] > 0]

print("NAV records:", len(nav))


# TRANSACTIONS

transactions = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("\nCleaning transactions...")

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

transactions = transactions[
    transactions["transaction_type"]
    .isin(valid_types)
]

transactions = transactions[
    transactions["amount_inr"] > 0
]

print("Transactions:", len(transactions))


# PERFORMANCE

performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("\nCleaning performance...")

performance = performance[
    performance["expense_ratio_pct"]
    .between(0.1, 2.5)
]

print("Performance records:", len(performance))


# SAVE FILES
nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

transactions.to_csv(
    "data/processed/transactions_clean.csv",
    index=False
)

performance.to_csv(
    "data/processed/performance_clean.csv",
    index=False
)

print("\nFILES SAVED")

print("="*60)
print("DATA CLEANING COMPLETED")
print("="*60)