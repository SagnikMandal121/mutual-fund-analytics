import os
import requests
import pandas as pd

# Output folder
OUTPUT_DIR = "data/raw"

# Only AMFI codes (do not assume names)
amfi_codes = [
    119551,
    120503,
    118632,
    119092,
    120841
]

print("=" * 60)
print("LIVE NAV FETCH STARTED")
print("=" * 60)

for code in amfi_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    print(f"\nFetching AMFI Code: {code}")

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        # Actual scheme name returned by API
        scheme_name = data["meta"]["scheme_name"]

        print(f"Actual Scheme: {scheme_name}")

        # Convert NAV data to DataFrame
        nav_df = pd.DataFrame(data["data"])

        # Add metadata columns
        nav_df["amfi_code"] = code
        nav_df["scheme_name"] = scheme_name

        # Create safe filename from actual scheme name
        filename = (
            scheme_name
            .lower()
            .replace(" ", "_")
            .replace("-", "")
            .replace("/", "_")
        )

        filepath = os.path.join(
            OUTPUT_DIR,
            f"{filename}_live_nav.csv"
        )

        # Save CSV
        nav_df.to_csv(filepath, index=False)

        print("SUCCESS")
        print(f"Records saved: {len(nav_df)}")
        print(f"Saved as: {filepath}")

    except Exception as e:
        print("FAILED")
        print(f"Error: {e}")

print("\n" + "=" * 60)
print("LIVE NAV FETCH COMPLETED")

print("=" * 60) 