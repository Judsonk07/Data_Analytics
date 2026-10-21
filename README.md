# Data Analytics Portfolio

Welcome to the **Data Analytics Portfolio repository**. This repository showcases comprehensive, production-grade business intelligence and data engineering projects across three core competencies: **Microsoft Excel**, **Microsoft Power BI**, and **SQL (MySQL)**.

Each project spans the complete analytics lifecycle: raw data ingestion, ETL cleaning pipelines, data modeling, relational schema engineering, DAX and SQL query formulation, and executive dashboard design.

---

## Portfolio Quick Navigation

```
Data_Analytics/
├── 📊 Excel/                          # Advanced Excel Spreadsheets, Pivot Modeling & Dashboards
│   ├── FreshMart/                     # Supermarket Sales, Customer Segments & Margin Analytics
│   └── TrendKart/                     # Omnichannel Fashion Retail & Return Diagnostics
│
├── 📈 PowerBI/                        # Star-Schema Data Models, Complex DAX & Glassmorphic Dashboards
│   ├── AeroHome/                      # Home Appliance Manufacturing & Downtime Root Cause Analysis
│   └── Nova_Tech/                     # High-Tech Component Manufacturing & Supply Chain Performance
│
└── 🗄️ SQL/                            # Relational Database Design, Data Cleaning, Validation & Business Intelligence
    ├── HealthPlus_Care_DB/            # Healthcare Clinic Network, Telemedicine & Claims Database
    └── Hospital_Analytics_DB/         # Multi-Hospital Operations, Inpatient Admissions & Billing DB
```

---

## 📊 1. Microsoft Excel Analytics

Comprehensive retail analytics models developed using Power Query, advanced dynamic formulas (`XLOOKUP`, `INDEX/MATCH`, `SUMIFS`), pivot cache architecture, and synchronized interactive dashboard controls.

### 🛒 [FreshMart Supermarket Sales Analytics](Excel/FreshMart/)
> **Domain:** Supermarket & Retail Chain | **Tools:** Excel, Pivot Tables, Dynamic Slicers, Data Modeling

![FreshMart Dashboard](Excel/FreshMart/Dashboard/FreshMart%20Dashboard.jpeg)

* **Key Performance Indicators:**
  * **Total Sales Revenue:** `₹ 28,92,988.60`
  * **Total Profit:** `₹ 7,37,358.89`
  * **Gross Profit Margin:** `25.71%`
  * **Total Quantity Sold:** `9,823 units`
  * **Total Transactions:** `2,500`
  * **Average Order Value:** `₹ 1,157.20`
* **Key Insights:**
  * **Channel Mix:** In-Store retail dominates with `69%` of volume, followed by Online Web (`21%`) and Mobile App (`10%`).
  * **Peak Revenue Window:** Afternoon (`₹1,087K`) and Evening (`₹937K`) hours contribute >70% of gross store turnover.
  * **Loyalty Contribution:** Gold tier loyalty members drive `60%` of overall revenue.
  * **Regional Concentration:** The South region drives `65%` of revenue, indicating growth opportunity in Northern/Eastern territories.
* 📂 **Explore Project:** [Read FreshMart Project Documentation](Excel/FreshMart/)

---

### 👗 [TrendKart Fashion Retail Analytics](Excel/TrendKart/)
> **Domain:** Omnichannel Apparel & Fashion Retail | **Tools:** Excel, Advanced Formulas, Data Quality Log, Slicers

![TrendKart Dashboard](Excel/TrendKart/Dashboard/TrendKart%20Dashboard.jpeg)

* **Key Performance Indicators:**
  * **Total Sales Revenue:** `₹ 92,27,180.00`
  * **Total Profit:** `₹ 18,04,519.00`
  * **Gross Profit Margin:** `19.56% (~20%)`
  * **Total Units Sold:** `6,118 units`
  * **Total Transactions:** `2,995`
  * **Return Rate:** `5%`
* **Key Insights:**
  * **Omnichannel Performance:** Physical offline retail generates `66%` of gross sales while online e-commerce drives `34%`.
  * **Payment Trends:** Modern payment modes lead sales: UPI (`28%`), Credit Cards (`22%`), Debit Cards (`20%`), and Cash (`19%`).
  * **Seasonal Surge:** October festive sales generated over ₹1.5M in monthly revenue.
  * **Product Health:** Strong 95% clean fulfillment rate with high-margin returns isolated to sizing variations in apparel.
* 📂 **Explore Project:** [Read TrendKart Project Documentation](Excel/TrendKart/)

---

## 📈 2. Microsoft Power BI Dashboards

High-impact executive manufacturing intelligence dashboards engineered with star-schema dimensional data models, robust DAX calculations, and high-contrast glassmorphic design systems.

### 🏭 [AeroHome Manufacturing — Operations & Downtime Intelligence](PowerBI/AeroHome/)
> **Domain:** Home Appliance Manufacturing | **Theme:** Futuristic Dark Neon-Purple Glassmorphism

![AeroHome Dashboard](PowerBI/AeroHome/Images/Aero%20Home%20Dashboard.png)

* **Key Performance Indicators:**
  * **Total Machine Downtime:** `122,329 minutes` (~2,039 hours)
  * **Production Attainment:** `96.26%`
  * **Product Defect Rate:** `1.71%`
  * **Production Shortfall:** `-41,425 units`
  * **Supplier Delay Rate:** `16.55%`
* **Key Insights:**
  * **Downtime Root Cause Analysis:** Material shortages are the #1 driver of lost factory uptime (`23,000 minutes`), followed by preventive maintenance (`22,000 minutes`) and machine breakdowns (`21,000 minutes`).
  * **Plant Shortfall Comparison:** Chennai (`-12.2K`) and Coimbatore (`-11.1K`) recorded the steepest attainment gaps.
  * **Line Health:** Compressor Station leads attainment at `97.28%`, while Assembly Line 2 lags at `94.17%`.
* 📂 **Explore Project:** [Read AeroHome Project Documentation](PowerBI/AeroHome/)

---

### ⚙️ [Nova Tech Manufacturing — Plant & Supply Chain Performance](PowerBI/Nova_Tech/)
> **Domain:** High-Tech & Precision Engineering | **Theme:** Crimson Red Neon Glassmorphism

![Nova Tech Dashboard](PowerBI/Nova_Tech/Images/Nova%20Tech%20Dashboard.png)

* **Key Performance Indicators:**
  * **Total Finished Production:** `1,029,692 units` (>1.02 Million)
  * **Quality Defect Rate:** `1.71%`
  * **MoM Production Change:** `-16.92%`
  * **Supplier Delay Rate:** `10.69%`
* **Key Insights:**
  * **Decline Diagnostic:** Unravels the mid-year -16.92% production drop, pinpointing Munich Electronics (`-13K units`) and Monterrey Stamping (`-7K units`) as the primary bottlenecks.
  * **Defect Exposure:** Avionics Control Systems exhibit a `4.02%` defect rate—more than double the plant average.
  * **Supplier Risk:** Global Parts (`18.63%` delay) and MexiStamp (`18.23%` delay) require renegotiated SLAs to stabilize material flow.
* 📂 **Explore Project:** [Read Nova Tech Project Documentation](PowerBI/Nova_Tech/)

---

## 🗄️ 3. SQL Relational Database Engineering & Analytics

Enterprise relational database architectures implemented in **SQL (MySQL)**. Each project includes DDL database creation, ETL data cleaning scripts, validation constraints, and 25 business analysis queries.

### 🏥 [HealthPlus Care Enterprise Database System](SQL/HealthPlus_Care_DB/)
> **Domain:** Outpatient Clinics, Telehealth & Insurance Processing | **Scale:** 17 Relational Tables

* **Architecture:** 17 normalized tables: `clinics`, `specialists`, `members`, `corporates`, `corporate_members`, `consultations`, `telemedicine_sessions`, `chronic_care_programs`, `health_packages`, `package_subscriptions`, `lab_tests`, `prescriptions`, `billing`, `payments`, `feedback`, `staff`, `claims`.
* **Engineering Pipeline:**
  * `01.healthplus_care_table_Database_Setup.sql`: Normalized DDL schema definition.
  * `02.healthplus_care_Data_Cleaning.sql`: Data hygiene routines (string trimming, gender normalization, NULL handling).
  * `03.healthplus_care_Data_Validation.sql`: Relational constraint audits and orphan key detection.
  * `04.healthplus_care_Business_Analysis.sql`: 25 strategic SQL queries evaluating operational volume, revenue streams, doctor consultation fees, and patient feedback ratings.
* 📂 **Explore Project:** [Read HealthPlus Care Documentation & Queries](SQL/HealthPlus_Care_DB/)

---

### 🏨 [Hospital Analytics Database System](SQL/Hospital_Analytics_DB/)
> **Domain:** Multi-Specialty Hospital Network Operations | **Scale:** 15 Relational Tables

* **Architecture:** 15 normalized tables: `hospitals`, `departments`, `doctors`, `employees`, `patients`, `appointments`, `admissions`, `rooms`, `treatments`, `laboratory`, `medicines`, `pharmacy`, `billing`, `payments`, `insurance`.
* **Engineering Pipeline:**
  * `01.Hospital_Analytics_Table_Database_Setup.sql`: Multi-facility network schema setup.
  * `02.Hospital_Analytics_Data_Cleaning.sql`: Inpatient admission date casting, room status normalization, and cost validations.
  * `03.Hospital_Analytics_Data_Validation.sql`: Foreign key and duplicate record validation.
  * `04.Hospital_Analytics_Business_Analysis.sql`: 25 complex analytical queries evaluating bed occupancy, admission flows (Emergency vs Elective), physician fee structures, and laboratory profitability.
* 📂 **Explore Project:** [Read Hospital Analytics Documentation & Queries](SQL/Hospital_Analytics_DB/)

---

## 🛠️ Technology Stack & Tools

| Area | Technologies & Tools |
| :--- | :--- |
| **Spreadsheet Analytics** | Microsoft Excel, Power Query, Pivot Tables, Slicers, `XLOOKUP`, `INDEX/MATCH`, `SUMIFS`, Data Quality Audit Logs |
| **Business Intelligence** | Microsoft Power BI Desktop, DAX (Data Analysis Expressions), Star Schema Dimensional Modeling, UI/UX Glassmorphism |
| **Database Engineering** | SQL, MySQL Workbench, Relational Data Modeling (3NF), DDL/DML/DQL, Aggregations, Window Functions |
| **Data Formats** | `.xlsx`, `.pbix`, `.sql`, `.csv` |

---

## 📁 Repository Directory Structure

```
Data_Analytics/
├── README.md                          # Root Repository Documentation (You are here)
│
├── Excel/
│   ├── README.md                      # Excel Category Overview
│   ├── FreshMart/
│   │   ├── README.md                  # FreshMart Project Deep Dive
│   │   ├── Cleaned/                   # Transformed datasets & master workbook
│   │   ├── Dashboard/                 # FreshMart Dashboard.jpeg
│   │   └── Raw/                       # Original supermarket data files
│   └── TrendKart/
│       ├── README.md                  # TrendKart Project Deep Dive
│       ├── Cleaned/                   # TrendKart_Data_Cleaning_Final.xlsx
│       ├── Dashboard/                 # TrendKart Dashboard.jpeg
│       └── Raw/                       # Source fashion retail dataset
│
├── PowerBI/
│   ├── README.md                      # Power BI Category Overview
│   ├── AeroHome/
│   │   ├── README.md                  # AeroHome Project Deep Dive
│   │   ├── Dashboard/                 # Aero_home.pbix
│   │   ├── Images/                    # Aero Home Dashboard.png
│   │   └── Raw/                       # AeroHome_Manufacturing_Dataset.xlsx
│   └── Nova_Tech/
│       ├── README.md                  # Nova Tech Project Deep Dive
│       ├── CSV/                       # Normalized dimension & fact CSVs
│       ├── Dashboard/                 # NovaTech.pbix
│       └── Images/                    # Nova Tech Dashboard.png
│
└── SQL/
    ├── README.md                      # SQL Category Overview
    ├── HealthPlus_Care_DB/
    │   ├── README.md                  # HealthPlus Care DB Deep Dive
    │   ├── Cleaned/                   # 01 Setup, 02 Cleaning, 03 Validation, 04 Analysis
    │   ├── CSV/                       # 17 normalized source CSV tables
    │   └── Raw/                       # HealthPlus_Care_DB_dataset.xlsx
    └── Hospital_Analytics_DB/
        ├── README.md                  # Hospital Analytics DB Deep Dive
        ├── Cleaned/                   # 01 Setup, 02 Cleaning, 03 Validation, 04 Analysis
        ├── CSV/                       # 15 normalized source CSV tables
        └── Raw/                       # Hospital_Analytics_DB_dataset.xlsx
```
