# Data Dictionary

## dim_fund

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company |
| scheme_name | Text | Fund scheme name |
| category | Text | Equity/Debt |
| sub_category | Text | Fund subtype |
| risk_category | Text | Risk classification |

---

## fact_nav

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | Integer | Scheme code |
| date | Date | NAV date |
| nav | Real | Net asset value |

---

## fact_transactions

| Column | Type | Description |
|--------|------|-------------|
| investor_id | Text | Investor identifier |
| transaction_date | Date | Transaction date |
| amount_inr | Real | Transaction amount |

---

## fact_performance

| Column | Type | Description |
|--------|------|-------------|
| return_1yr_pct | Real | 1-year return |
| return_3yr_pct | Real | 3-year return |
| return_5yr_pct | Real | 5-year return |
| expense_ratio_pct | Real | Expense ratio |
| aum_crore | Real | Assets under management |