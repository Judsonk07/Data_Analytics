# Excel Analytics Projects Portfolio

This directory contains end-to-end commercial analytics projects developed in **Microsoft Excel**, featuring data engineering, relational modeling, advanced formula calculations, pivot architecture, and executive-ready interactive dashboards.

---

## Projects Overview

| Project | Domain | Key Business Focus | Revenue / Scale | Dashboard Preview |
| :--- | :--- | :--- | :--- | :--- |
| **[FreshMart](FreshMart/)** | Supermarket & Retail | Sales Trends, Margin %, Channel Mix, Store Benchmarking | ₹ 28.93 Lakhs Sales | [View Details](FreshMart/) |
| **[TrendKart](TrendKart/)** | Omnichannel Fashion | Omnichannel Profitability, Category Margins, Return Analysis | ₹ 92.27 Lakhs Sales | [View Details](TrendKart/) |

---

## 1. FreshMart Supermarket Sales Analytics

![FreshMart Dashboard](FreshMart/Dashboard/FreshMart%20Dashboard.jpeg)

* **Directory:** [`Excel/FreshMart/`](FreshMart/)
* **Dataset:** Supermarket transactional records, master customer lists, store locations, employee tables, and product catalogs.
* **Core Metrics:**
  * **Total Sales:** `₹ 28,92,988.60`
  * **Total Profit:** `₹ 7,37,358.89`
  * **Profit Margin:** `25.71%`
  * **Total Quantity:** `9,823 units`
  * **Total Transactions:** `2,500`
* **Key Analytical Highlights:**
  * **Channel Performance:** In-Store leads with `69%` share, followed by Web Online (`21%`) and Mobile App (`10%`).
  * **Peak Revenue Hours:** Over `70%` of transaction volume occurs during Afternoon (`₹1,087K`) and Evening (`₹937K`) hours.
  * **Customer Demographics:** Gold tier loyalty members account for `60%` of total revenue.
  * **Interactive Slicers:** Dynamic filtering by Month, Product Category (11 categories), Geographic Region, Channel, and Payment Mode.

---

## 2. TrendKart Fashion Retail Analytics

![TrendKart Dashboard](TrendKart/Dashboard/TrendKart%20Dashboard.jpeg)

* **Directory:** [`Excel/TrendKart/`](TrendKart/)
* **Dataset:** Enterprise fashion retail dataset spanning multi-zone stores, e-commerce orders, product costings, and return logs.
* **Core Metrics:**
  * **Total Sales:** `₹ 92,27,180.00`
  * **Total Profit:** `₹ 18,04,519.00`
  * **Profit Margin:** `19.56% (~20%)`
  * **Total Quantity:** `6,118 units`
  * **Total Transactions:** `2,995`
  * **Return Rate:** `5%`
* **Key Analytical Highlights:**
  * **Omnichannel Revenue Breakdown:** Physical Retail accounts for `66%` while E-Commerce represents `34%`.
  * **Payment Trends:** UPI (`28%`), Credit Cards (`22%`), and Debit Cards (`20%`) dominate consumer payments.
  * **Category & Margin Diagnostics:** Clear segmentation between high-volume drivers (Men Ethnic, Sarees) and low-margin promotional items.
  * **Return Audit:** 95% clean fulfillment rate with focused return tracking by category.

---

## Technical Skills Demonstrated in Excel
* **Data Transformation:** Data cleaning, deduplication, handling missing values, standardizing dates and categorization in Power Query / Excel.
* **Relational Data Modeling:** Multi-table lookups using `XLOOKUP`, `INDEX`, `MATCH`, and nested logical conditions (`IFS`, `SWITCH`).
* **KPI & Aggregation Logic:** Dynamic aggregation tables using `SUMIFS`, `COUNTIFS`, `AVERAGEIFS`, and array formulas.
* **Pivot Table Architecture:** Tabular data consolidation, calculated fields, multi-dimensional grouping, and shared timeline slicer caches.
* **Executive UI/UX Design:** Harmonious color palettes, clear visual hierarchy, custom card shapes, icon integration, and structured grid layout.

---

## Directory Organization
```
Excel/
├── README.md
├── FreshMart/
│   ├── README.md
│   ├── Cleaned/
│   │   ├── Cleaned_FreshMart_Customers.xlsx
│   │   ├── Cleaned_FreshMart_Employess.xlsx
│   │   ├── Cleaned_FreshMart_Products.xlsx
│   │   ├── Cleaned_FreshMart_Stores.xlsx
│   │   ├── Cleaned_FreshMart_Suppliers.xlsx
│   │   └── FreshMart_Project_FINAL.xlsx
│   ├── Dashboard/
│   │   └── FreshMart Dashboard.jpeg
│   └── Raw/
│       └── ...
└── TrendKart/
    ├── README.md
    ├── Cleaned/
    │   └── TrendKart_Data_Cleaning_Final.xlsx
    ├── Dashboard/
    │   └── TrendKart Dashboard.jpeg
    └── Raw/
        └── TrendMart_Fashion_Enterprise_Dataset.xlsx
```
