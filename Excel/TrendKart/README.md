# TrendKart Fashion Retail Analytics

![TrendKart Dashboard](Dashboard/TrendKart%20Dashboard.jpeg)

## Executive Summary
**TrendKart** is an omnichannel fashion and apparel retail enterprise operating across physical stores and e-commerce platforms. This project delivers a comprehensive sales, profitability, return behavior, and multi-channel performance intelligence dashboard engineered in **Microsoft Excel**.

The solution enables retail merchandisers, inventory managers, and regional directors to identify high-margin fashion categories, track return rates, compare offline vs. online sales performance, and optimize channel profitability.

---

## Key Performance Indicators (KPIs)
* **Total Sales Revenue:** `₹ 92,27,180` (~₹92.27 Lakhs)
* **Total Profit:** `₹ 18,04,519` (~₹18.05 Lakhs)
* **Gross Profit Margin:** `19.56%` (~20%)
* **Total Units Sold:** `6,118 units`
* **Total Cost of Goods Sold (COGS):** `₹ 65,96,441`
* **Total Transactions:** `2,995 transactions`
* **Unique Customers:** `364 customers`
* **Return Rate:** `5%` (Low return rate indicating healthy product satisfaction)

---

## Dashboard Architecture & Visualizations

```
+-------------------------------------------------------------------------------------------------------+
|                                  TRENDKART FASHION SALES DASHBOARD                                    |
+-------------------------------------------------------------------------------------------------------+
|  Total Sales       Total Quantity      Total Profit       Profit Margin      Total Cost    Total Trans|
|  ₹ 92,27,180            6,118         ₹ 18,04,519             20%          ₹ 65,96,441        2,995   |
+-------------------------------------------------------------------------------------------------------+
|  [SLICERS]      |  Monthly Sales vs Profit Trend  |  Online vs Offline      |  Sales by Payment Mode  |
|  - Month        |  (Apr 2024 - Mar 2025)          |  - Offline: 66%         |  - UPI: 28%             |
|  - Category     |  Peak: Oct 2024 (~₹1.5M sales)  |  - Online:  34%         |  - Credit Card: 22%     |
|  - Region       |                                 |                         |  - Debit Card:  20%     |
|  - Channel      +---------------------------------+-------------------------+  - Cash:        19%     |
|  - Payment Mode |  Category Sales vs Profit       |  Store & Regional Profit|  - Net Banking:  7%     |
|                 |  Top: Men Ethnic, Sarees, Jeans |  - South Zone 1 (Leader)|  - EMI:          4%     |
|                 +---------------------------------+-------------------------+-------------------------+
|                 |  High Sales vs Low Profit Prod  |                         |  Return Analysis        |
|                 |  Margin optimization focus      |                         |  - Not Returned: 95%    |
|                 |                                 |                         |  - Returned:      5%    |
+-------------------------------------------------------------------------------------------------------+
```

### Visual Breakdown
1. **Monthly Sales vs Profit Trend (Dual Line Chart):** Tracks monthly trajectories over 2024–2025. Illustrates a massive surge in October (festive festive peak exceeding ₹1.5M) followed by consistent post-holiday revenue stability.
2. **Online vs Offline Performance (Donut Chart):**
   * **Offline Physical Stores:** `66%` of total gross volume
   * **Online E-Commerce:** `34%` of total sales
3. **Sales by Payment Mode (Donut Chart):**
   * **UPI:** `28%`
   * **Credit Card:** `22%`
   * **Debit Card:** `20%`
   * **Cash:** `19%`
   * **Net Banking:** `7%`
   * **EMI:** `4%`
4. **Category Sales vs Profit (Clustered Bar Chart):** Compares revenue against bottom-line profitability across fashion categories: *Accessories, Footwear, Jewellery, Men Ethnic, Men Shirts, Wallets, Winter Wear, Women Jeans, and Women Sarees*.
5. **Store & Regional Profitability:** Horizontal stacked chart evaluating performance across *South Zone 1*, *South Zone 2*, and *South Zone 3*, with South Zone 1 leading across both volume and profit margin.
6. **High Sales vs Low Profit Product Matrix:** Identifies high-volume products yielding suboptimal profit margins (e.g. promotional apparel lines, third-party accessories) that require price renegotiation or markdown adjustments.
7. **Return Rate Analysis (Donut Chart):** Highlights that `95%` of orders are successfully fulfilled without returns, while `5%` undergo return processing.

---

## Data Pipeline & Modeling

### Directory Structure
```
Excel/TrendKart/
├── Cleaned/
│   └── TrendKart_Data_Cleaning_Final.xlsx   # Full analytical model, data quality log & dashboard
├── Dashboard/
│   └── TrendKart Dashboard.jpeg             # High-resolution dashboard screenshot
└── Raw/
    └── TrendMart_Fashion_Enterprise_Dataset.xlsx
```

### Workbook Sheets & Pipeline Architecture
* **`Sales_Transactions` / `Customers` / `Products` / `Stores` / `Employees` / `Suppliers`:** Cleaned relational tables forming a normalized business schema.
* **`Data_Quality_Log`:** Systematic audit tracking handling of duplicates, currency standardization, inconsistent sizing tags, and return status flags.
* **`kpi` & `monthly` Sheets:** Pre-aggregated metrics feeding KPI cards and time-series visual components.
* **`region`, `channel`, `discount return analysis`:** Specialized analytical pivot data structures powering donut and bar charts.
* **`slicer` & `Dashboard` Sheets:** Central presentation layer equipped with synchronized slicers.

---

## Strategic Business Insights & Recommendations
1. **Omnichannel Synergy:** With physical retail driving `66%` and online driving `34%`, TrendKart has an opportunity to roll out "Buy Online, Pick Up In Store" (BOPIS) to cross-sell accessories during pickup.
2. **Festive Demand Capitalization:** October generates over 25% of annual profit. Supply chain inventory ramp-up must begin in August to mitigate stockouts during festive peaks.
3. **Return Rate Containment:** Although returns are healthy at `5%`, sizing inconsistencies in Women Jeans and Footwear represent over 60% of returned volume. Implementing accurate sizing charts and customer fit guides will further reduce return costs.
4. **Margin Protection:** High-sales/low-profit product analysis reveals volume items being heavily discounted. Shift promotional focus toward high-margin ethnic wear and accessories.
