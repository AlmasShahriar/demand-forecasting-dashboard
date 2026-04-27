# 📦 Demand Forecasting & Inventory Analysis Dashboard

> A Python-powered dashboard for demand forecasting, seasonal analysis, and ABC inventory classification — inspired by real industrial engineering work at **American & Efird (Bangladesh) Ltd.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Chart.js](https://img.shields.io/badge/Chart.js-4.4-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)]()
[![No Dependencies](https://img.shields.io/badge/Zero_Pip_Dependencies-00C2FF?style=for-the-badge)]()
[![HTML Output](https://img.shields.io/badge/Output-Standalone_HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)]()

---

## 📊 What It Does

This tool reads SKU-level demand history from a CSV and generates a fully interactive, standalone HTML dashboard — no web server needed.

### Sections Generated:

| # | Section | What's Inside |
|---|---------|--------------|
| 01 | **Aggregate Demand & Forecast** | Total monthly demand, 3-month moving average, 6-month seasonal forecast |
| 02 | **ABC Classification** | Pareto bar chart, class donut chart, ranked inventory table |
| 03 | **SKU Drill-Down** | Per-SKU demand + forecast + seasonal index grid (interactive selector) |
| 04 | **Forecast Table** | 6-month unit forecast for all SKUs side-by-side |

---

## 🧠 Techniques Used

- **Moving Average (3-month)** — smooths demand noise to reveal trend
- **Seasonal Index Forecasting** — detects peak/trough months per SKU, projects demand using seasonal ratios
- **Trend Detection** — compares H1 vs H2 average to estimate growth/decline
- **ABC Analysis** — classifies SKUs by annual value contribution (A ≈ 70%, B ≈ 20%, C ≈ 10%)

---

## 🚀 Getting Started

**Requirements:** Python 3.8+ only. No pip installs needed — uses only the standard library (`csv`, `json`, `os`).

```bash
# Clone the repo
git clone https://github.com/almasshahriar/demand-forecasting-dashboard.git
cd demand-forecasting-dashboard

# Run the generator
python generate_dashboard.py

# Open the output
open output/dashboard.html      # macOS
start output/dashboard.html     # Windows
xdg-open output/dashboard.html  # Linux
```

---

## 📁 Project Structure

```
demand-forecasting-dashboard/
│
├── generate_dashboard.py   ← Main script (run this)
├── data/
│   └── demand_data.csv     ← Input: SKU demand history (edit this)
├── output/
│   └── dashboard.html      ← Generated dashboard (open in browser)
└── README.md
```

---

## 🗂️ Input Data Format

Edit `data/demand_data.csv` with your own data:

```csv
SKU,Description,Unit_Cost,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec
SKU-001,My Product,12.50,4200,3900,4800,5100,5400,5800,6200,6000,5500,5000,4600,4300
```

| Column | Description |
|--------|-------------|
| `SKU` | Unique SKU identifier |
| `Description` | Product description |
| `Unit_Cost` | Cost per unit ($) |
| `Jan`–`Dec` | Monthly demand (units) |

---

## 💡 Background

This project is directly inspired by my industrial attachment at **American & Efird (Bangladesh) Ltd.**, where I:
- Analyzed **75,000+ historical demand records**
- Built a **seasonal forecasting model** for 20M+ units of sewing thread
- Performed **ABC inventory classification** to prioritize stock management

This dashboard automates and visualizes that exact workflow.

---

## 👤 Author

**Almas Shahriar**  
B.Sc. Industrial & Production Engineering, BUET (Expected 2026)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/almasshahriar/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:almasalif123@gmail.com)
[![Portfolio](https://img.shields.io/badge/IE_Toolkit-0077B6?style=flat-square)](https://almasshahriar.github.io/ie-calc-suite/)

---

*Built with Python + Chart.js · No frameworks, no fluff — just engineering.*
