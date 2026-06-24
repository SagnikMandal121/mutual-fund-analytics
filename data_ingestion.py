import os
import pandas as pd


# Path to raw data folder
DATA_PATH = "data/raw"

# Dictionary to store all datasets
datasets = {}

# Get all CSV files from raw folder
csv_files = [
    file for file in os.listdir(DATA_PATH)
    if file.endswith(".csv")
]

print("=" * 60)
print("DATA INGESTION STARTED")
print("=" * 60)


for file in csv_files:
    print(f"\nProcessing file: {file}")
    print("-" * 60)

    file_path = os.path.join(DATA_PATH, file)

    try:
        # Load CSV
        df = pd.read_csv(file_path)

        # Save dataframe
        datasets[file] = df

        # Basic information
        print(f"Shape: {df.shape}")

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        # Data quality checks
        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error loading {file}: {e}")


print("\n" + "=" * 60)
print("DATA INGESTION COMPLETED")
print(f"Successfully loaded {len(datasets)} datasets")
print("=" * 60)

print("\n" + "=" * 60)
print("FUND MASTER ANALYSIS")
print("=" * 60)

fund_master = datasets["01_fund_master.csv"]

print("\nFund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Categories:")
print(fund_master["risk_category"].unique())

print("\nSEBI Category Codes:")
print(fund_master["sebi_category_code"].unique())

print("\n" + "=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

nav_history = datasets["02_nav_history.csv"]

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print(f"Total fund_master codes: {len(fund_codes)}")
print(f"Total nav_history codes: {len(nav_codes)}")

if len(missing_codes) == 0:
    print("All AMFI codes exist in NAV history.")
else:
    print("Missing AMFI Codes:")
    print(missing_codes)