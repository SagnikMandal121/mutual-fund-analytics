import pandas as pd

score = pd.read_csv(
    "data/processed/fund_scorecard.csv"
)

risk = input(
    "Risk (Low/Moderate/High): "
)

if risk == "Low":
    funds = score.nsmallest(
        3,
        "max_drawdown"
    )

elif risk == "Moderate":
    funds = score.nlargest(
        3,
        "sharpe_ratio"
    )

else:
    funds = score.nlargest(
        3,
        "cagr"
    )

print(
    funds[
        [
            "amfi_code",
            "sharpe_ratio",
            "cagr"
        ]
    ]
)