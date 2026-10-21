# FreshMart Supermarket Sales Analytics

![FreshMart Dashboard](Dashboard/FreshMart%20Dashboard.jpeg)

## Executive Summary
**FreshMart** is a multi-category supermarket and retail chain providing fresh produce, groceries, household items, and personal care products. This project delivers an end-to-end sales performance, customer demographic, and operational analytics solution developed in **Microsoft Excel**.

The interactive dashboard empowers retail store managers, category planners, and regional directors to monitor revenue trends, evaluate profit margins, track store efficiency, and identify high-value customer segments.

---

## Key Performance Indicators (KPIs)
* **Total Sales Revenue:** `₹ 28,92,988.60` (~₹28.93 Lakhs)
* **Total Profit:** `₹ 7,37,358.89` (~₹7.37 Lakhs)
* **Gross Profit Margin:** `25.71%`
* **Total Units Sold:** `9,823 units`
* **Total Cost of Goods Sold (COGS):** `₹ 21,55,163.05`
* **Total Completed Transactions:** `2,500 transactions`
* **Average Order Value (AOV):** `₹ 1,157.20`

---

## Dashboard Architecture & Visualizations

```
+-------------------------------------------------------------------------------------------------------+
|                                     FRESHMART SALES DASHBOARD                                         |
+-------------------------------------------------------------------------------------------------------+
|  Total Sales      Total Quantity      Total Profit       Profit Margin      Total Cost    Total Trans |
|  ₹ 28,92,988.60        9,823         ₹ 7,37,358.89          25.71%        ₹ 21,55,163.05     2,500    |
+-------------------------------------------------------------------------------------------------------+
|  [SLICERS]      |  Sales & Profit Trend Monthly   |  Sales By Channel       |  Payment Mode           |
|  - Month        |  (Mar 2025 - Mar 2026)          |  - In-Store (69%)       |  - UPI (19%)            |
|  - Category     |  Peak: Oct 2025 (445K Sales)    |  - Online (21%)         |  - Credit Card (17%)    |
|  - Region       |                                 |  - Mobile App (10%)     |  - Debit Card (17%)     |
|  - Channel      +---------------------------------+-------------------------+-------------------------+
|  - Payment Mode |  Customer Membership            |  Sales By Region        |  Order Time Breakdown   |
|                 |  - Gold: 60%                    |  - South: 65%           |  - Afternoon: 1,087K    |
|                 |  - Silver: 24%                  |  - West: 24%            |  - Evening: 937K        |
|                 |  - Bronze: 16%                  |  - North: 9% | East: 2% |  - Morning: 662K        |
+-------------------------------------------------------------------------------------------------------+
```

### Visual Breakdown
1. **Sales & Profit Trend Monthly:** Clustered column visualization showing monthly sales vs. profit trajectories from March 2025 to March 2026, highlighting seasonal demand spikes (October festive peak reaching ₹445K).
2. **Sales by Channel (Donut Chart):**
   * **In-Store:** `69%` (Core revenue driver)
   * **Online Web:** `21%`
   * **Mobile App:** `10%`
3. **Payment Mode Distribution (Donut Chart):**
   * **UPI:** `19%` | **Credit Card:** `17%` | **Debit Card:** `17%` | **Wallet:** `17%` | **Net Banking:** `15%` | **Cash:** `15%` (Demonstrates modern digital payment adoption).
4. **Customer Membership Analysis (Donut Chart):**
   * **Gold Tier:** `60%`
   * **Silver Tier:** `24%`
   * **Bronze Tier:** `16%`
5. **Sales by Geographic Region:**
   * **South:** `65%` | **West:** `24%` | **North:** `9%` | **East:** `2%`
6. **Top 10 Stores by Sales:** Bar chart benchmarking highest grossing store branches (`STR006`, `STR025`, `STR032`, `STR019`, `STR007`, `STR009`, etc.).
7. **Order Time Analysis:**
   * **Afternoon:** `₹ 1,087K`
   * **Evening:** `₹ 937K`
   * **Morning:** `₹ 662K`
   * **Night:** `₹ 182K`

---

## Data Pipeline & Modeling

### Directory Structure
```
Excel/FreshMart/
├── Cleaned/
│   ├── Cleaned_FreshMart_Customers.xlsx
│   ├── Cleaned_FreshMart_Employess.xlsx
│   ├── Cleaned_FreshMart_Products.xlsx
│   ├── Cleaned_FreshMart_Stores.xlsx
│   ├── Cleaned_FreshMart_Suppliers.xlsx
│   └── FreshMart_Project_FINAL.xlsx      # Master analytical workbook & dashboard
├── Dashboard/
│   └── FreshMart Dashboard.jpeg          # High-resolution dashboard screenshot
└── Raw/
    ├── FreshMart_Customers.xlsx
    ├── FreshMart_Employess.xlsx
    ├── FreshMart_Products.xlsx
    ├── FreshMart_Sales_Transactions.xlsx
    ├── FreshMart_Stores.xlsx
    └── FreshMart_Suppliers.xlsx
```

### Data Transformation & Engineering Steps
* **Data Hygiene:** Handled missing customer demographic entries, standardizing date-time stamps, and trimming inconsistent text entries across retail store locations.
* **Relational Joins:** Implemented `XLOOKUP` and `INDEX/MATCH` to enrich transaction records with unit cost, category pricing, store branch names, and customer membership tiers.
* **Calculated Columns:** Computed line-item Gross Sales, Cost of Goods Sold (COGS), Profit Margin %, and Order Time Classification (`Morning`, `Afternoon`, `Evening`, `Night`).
* **Pivot Architecture:** Designed independent pivot cache structures feeding linked KPI scorecards and dynamic chart visualizers.
* **Interactive Slicers:** Connected multi-select timeline, category, regional, and payment slicers across all visual panels.

---

## Strategic Business Insights & Recommendations
1. **Channel Expansion:** While In-Store purchases dominate (`69%`), the combined digital channels (`31%`) show rapid growth. Targeted in-app promotions could convert footfall into digital recurring orders.
2. **Loyalty Program Success:** Gold loyalty members generate `60%` of overall sales. Implement targeted tiered rewards to migrate Silver (`24%`) and Bronze (`16%`) members into Gold status.
3. **Staffing Optimization:** Peak revenue occurs between Afternoon and Evening hours (`₹2,024K` combined, over 70% of daily revenue). Staff scheduling and stock replenishments should prioritize the 12 PM - 8 PM window.
4. **Regional Strategy:** South represents `65%` of revenue; East represents only `2%`. Evaluate supply chain logistics and marketing reach in the Northern and Eastern clusters to unlock untapped market potential.
