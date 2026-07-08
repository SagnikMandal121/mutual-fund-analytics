# 📈 Mutual Fund Analytics Platform

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge&logo=pandas)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?style=for-the-badge&logo=powerbi)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

### End-to-End Mutual Fund Intelligence Platform for Investment Analytics, Risk Modelling and Investor Behaviour Analysis

</div>

---

# 🚀 Project Overview

This project is a complete **Mutual Fund Analytics Platform** built using:

- Data Engineering pipelines
- Financial Performance Analytics
- Quantitative Risk Modelling
- Investor Behaviour Analysis
- Business Intelligence Dashboards
- Recommendation Systems

The objective was to simulate how modern asset management firms and investment research teams analyze fund performance, investor trends, sector allocations and portfolio risks using real-world financial analytics workflows.

---

# 🎯 Business Problem

The Indian mutual fund industry crossed **₹68 lakh crore AUM** with more than **26 crore folios**.

However investors still struggle with:

- Selecting suitable funds
- Understanding portfolio risk
- Tracking SIP behaviour
- Comparing funds against benchmarks
- Identifying sector concentration risks

This platform attempts to solve these problems using analytics and data science.

---

# 🏗 Architecture

```text
Raw CSV Files
      ↓
ETL Pipeline
      ↓
Data Cleaning & Validation
      ↓
SQLite Database
      ↓
EDA & Feature Engineering
      ↓
Risk Analytics Engine
      ↓
Power BI Dashboard
      ↓
Recommendation Engine
```

---

# 📂 Project Structure

```text
mutual-fund-analytics/

├── data/
│   ├── raw/
│   ├── processed/
│   └── db/

├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb

├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── compute_metrics.py
│   └── recommender.py

├── dashboard/
│   └── MutualFundAnalytics.pbix

├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx

└── README.md
```

---

# 📊 Dataset Summary

| Dataset | Records |
|----------|---------|
| NAV History | 46,000+ |
| Investor Transactions | 32,778 |
| Mutual Funds | 40 |
| Fund Houses | 10 |
| Categories | 12 |
| States | 12 |
| Investors | 30,000+ |

---

# ⚡ Features

## Data Engineering

- Automated ETL Pipeline
- Data Validation
- Missing Value Handling
- SQLite Storage Layer
- Live NAV Fetching API Integration

---

## Financial Analytics

- CAGR
- Alpha
- Beta
- Sharpe Ratio
- Maximum Drawdown
- Fund Scoring System

---

## Advanced Risk Analytics

- Historical VaR (95%)
- Conditional VaR (CVaR)
- Rolling 90 Day Sharpe Ratio
- Correlation Analysis
- Portfolio Concentration HHI Index

---

## Investor Intelligence

- Cohort Analysis
- SIP Continuity Analysis
- Geographic Distribution
- Age Demographics
- Gender Segmentation

---

## Recommendation Engine

Risk based recommendations:

- Low Risk
- Moderate Risk
- High Risk

Top funds selected using:

- Sharpe Ratio
- Risk Grade
- Drawdown
- Alpha

---

# 📈 Dashboard Pages

---

# 1️⃣ Industry Overview Dashboard

Provides a macro view of the Indian Mutual Fund Industry.

### KPIs

- Total AUM
- Total SIP Inflows
- Total Folios
- Total Schemes

### Insights

- Industry AUM crossed ₹14.4 lakh crore in 2024.
- Total folios increased to 26.12 crore.
- SIP inflows reached ₹31,002 crore monthly.

![Industry Overview](images/industry_overview.png)

---

# 2️⃣ Performance Analytics Dashboard

Analyzes risk adjusted fund performance.

Features:

- CAGR vs Sharpe Bubble Chart
- Fund Scoring Table
- Benchmark Comparison
- Risk Metrics Ranking

![Performance Dashboard](images/fund_performance.png)

---

# 3️⃣ Investor Behaviour Dashboard

Provides insights into investor demographics and behavior.

Features:

- State Distribution
- Age Group Analysis
- Transaction Analysis
- Monthly Transaction Volume

![Investor Dashboard](images/investor_analysis.png)

---

# 4️⃣ Market Flow Dashboard

Tracks capital movement across categories.

Features:

- SIP vs Market Trends
- Category Inflows
- Heatmap Analysis
- Category Rankings

![Market Flow Dashboard](images/sip&market_trends.png)

---

# 📉 Advanced Analytics

## Historical VaR and CVaR

Calculated 95% historical Value at Risk for all schemes.

```text
VaR(95) = 5th Percentile(Return Distribution)

CVaR = Mean(Returns below VaR threshold)
```

---

## Rolling Sharpe Ratio

90 Day rolling risk adjusted returns.

```text
Sharpe = Mean(Returns) / Std(Returns) × √252
```

---

## HHI Concentration Analysis

Measures sector concentration risk.

```text
HHI = Σ(weight²)
```

---

# 📷 Visual Analytics

## Category Inflow Heatmap

![Heatmap](images/category_heatmap.png)

---

## Return Correlation Matrix

![Correlation](images/correlation.png)

---

## Daily Return Distribution

![Returns](images/daily_return_distribution.png)

---

## Investor Age Distribution

![Age](images/age_distribution.png)

---

## AUM Growth

![AUM](images/aum_growth.png)

---

## Benchmark Comparison

![Benchmark](images/benchmark_comparison.png)

---

## Industry Folio Growth

![Folio](images/folio_growth.png)

---

## Gender Distribution

![Gender](images/gender_split.png)

---

## NAV Trend

![NAV](images/nav_trend.png)

---

## Rolling Sharpe Ratio

![Sharpe](images/rolling_sharpe_chart.png)

---

## Sector Allocation

![Sector](images/sector_donut.png)

---

## SIP Trend

![SIP](images/sip_trend.png)

---

## SIP Distribution by State

![State](images/state_distribution.png)

---

## SIP Amount by Age Group

![Age SIP](images/sip_age_boxplot.png)

---

## T30 vs B30 Distribution

![T30B30](images/t30_b30.png)

---

# 💡 Key Findings

### 📌 Liquid Funds dominate category inflows.

### 📌 Investors aged 26-35 account for more than 41% of investments.

### 📌 SIP inflows grew from ₹11,000 Cr to ₹31,002 Cr.

### 📌 Banking and IT dominate equity sector allocations.

### 📌 T30 cities contribute nearly two thirds of total investments.

### 📌 Certain equity funds demonstrated sustained superior Sharpe ratios.

---

# 🛠 Technology Stack

| Layer | Technology |
|-------|-----------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Plotly |
| Dashboard | Power BI |
| Database | SQLite |
| Notebook | Jupyter |
| Version Control | Git, GitHub |

---

# 📅 Development Roadmap

## Day 1
- Project setup
- Data ingestion
- ETL pipeline creation

## Day 2
- Data cleaning
- Feature engineering
- SQLite integration

## Day 3
- Exploratory Data Analysis
- Statistical summaries
- Visualization generation

## Day 4
- Performance metrics
- Sharpe ratio
- Beta and Alpha calculations

## Day 5
- Power BI dashboard development
- Four dashboard pages
- Interactive slicers

## Day 6
- Advanced analytics
- VaR/CVaR
- Cohort analysis
- Recommendation engine

## Day 7
- Final report
- Presentation deck
- Project documentation

---

# 👨‍💻 Author

## Sagnik Mandal

Final Year Electronics & Communication Engineering Student  
Founder — MedXpress  
CMO — DGEN Technologies  
Product Builder • Data Enthusiast • AI Engineer

### Connect With Me

- LinkedIn: www.linkedin.com/in/sagnik-mandal
- GitHub: https://github.com/SagnikMandal121

---

## ⭐ If you found this project useful, consider giving it a star.