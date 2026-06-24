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

#FUND MASTER

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

fund_master["launch_date"] = pd.to_datetime(
    fund_master["launch_date"]
)

fund_master = fund_master.drop_duplicates()

fund_master = fund_master.dropna(
    subset=["amfi_code", "scheme_name"]
)

#AUM BY FUND HOUSE

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum["date"] = pd.to_datetime(
    aum["date"]
)

aum = aum.drop_duplicates()

aum = aum[
    aum["aum_crore"] > 0
]

#SIP INFLOWS

sip = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
)

sip["month"] = pd.to_datetime(
    sip["month"]
)

sip["yoy_growth_pct"] = (
    sip["yoy_growth_pct"]
    .fillna(0)
)

sip = sip.drop_duplicates()

#CATEGORY INFLOWS

category = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

category["month"] = pd.to_datetime(
    category["month"]
)

category = category.drop_duplicates()

#INDUSTRY FOLIOS

folios = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

folios["month"] = pd.to_datetime(
    folios["month"]
)

folios = folios.drop_duplicates()

#PORTFOLIO HOLDINGS

holdings = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

holdings["portfolio_date"] = pd.to_datetime(
    holdings["portfolio_date"]
)

holdings = holdings.drop_duplicates()

holdings = holdings[
    holdings["weight_pct"] > 0
]

#BENCHMARK INDICES

benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

benchmark = benchmark.sort_values(
    ["index_name", "date"]
)

benchmark = benchmark.drop_duplicates()



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

fund_master.to_csv(
    "data/processed/fund_master_clean.csv",
    index=False
)

aum.to_csv(
    "data/processed/aum_clean.csv",
    index=False
)

sip.to_csv(
    "data/processed/sip_clean.csv",
    index=False
)

category.to_csv(
    "data/processed/category_clean.csv",
    index=False
)

folios.to_csv(
    "data/processed/folios_clean.csv",
    index=False
)

holdings.to_csv(
    "data/processed/holdings_clean.csv",
    index=False
)

benchmark.to_csv(
    "data/processed/benchmark_clean.csv",
    index=False
)

print("\nFILES SAVED")

print("="*60)
print("DATA CLEANING COMPLETED")
print("="*60)