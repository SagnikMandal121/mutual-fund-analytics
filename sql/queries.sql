-- 1 Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV per fund
SELECT amfi_code,
       AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3 Transactions by state
SELECT state,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 4 Average transaction amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- 5 Expense ratio below 1%
SELECT amfi_code,
       expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6 Highest 5-year returns
SELECT amfi_code,
       return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 7 Gender distribution
SELECT gender,
       COUNT(*)
FROM fact_transactions
GROUP BY gender;

-- 8 Category distribution
SELECT category,
       COUNT(*)
FROM dim_fund
GROUP BY category;

-- 9 Risk category distribution
SELECT risk_category,
       COUNT(*)
FROM dim_fund
GROUP BY risk_category;

-- 10 Average income by age group
SELECT age_group,
       AVG(annual_income_lakh)
FROM fact_transactions
GROUP BY age_group;