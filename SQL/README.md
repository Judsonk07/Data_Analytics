# SQL Database Engineering & Analytics Portfolio

This directory contains production-grade relational database management systems (RDBMS) designed and implemented in **SQL (MySQL)**. Each project includes complete relational architecture design (DDL), comprehensive data transformation and sanitization scripts (DML), data consistency validation pipelines, and 25 analytical SQL queries resolving mission-critical business challenges.

---

## Projects Overview

| Database System | Industry / Domain | Tables | Key Analytical Focus | Documentation |
| :--- | :--- | :--- | :--- | :--- |
| **[HealthPlus_Care_DB](HealthPlus_Care_DB/)** | Outpatient Clinic Network & Telehealth | 17 Tables | Consultations, Telemedicine Metrics, Chronic Care Programs, Billing & Insurance Claims | [View Schema & Queries](HealthPlus_Care_DB/) |
| **[Hospital_Analytics_DB](Hospital_Analytics_DB/)** | Multi-Specialty Hospital Network | 15 Tables | Emergency & Elective Inpatient Admissions, Bed Occupancy, Doctor Productivity, Surgery Costs, Pharmacy & Lab Revenue | [View Schema & Queries](Hospital_Analytics_DB/) |

---

## 1. HealthPlus Care Enterprise Database (`healthplus_care_db`)

* **Directory:** [`SQL/HealthPlus_Care_DB/`](HealthPlus_Care_DB/)
* **Scale:** 17 normalized relational tables covering primary care clinics, specialists, insured members, corporate wellness contracts, telemedicine sessions, laboratory diagnostics, and insurance claims.
* **Core Pipeline Files:**
  * `01.healthplus_care_table_Database_Setup.sql`: Complete DDL schema creation with primary/foreign keys.
  * `02.healthplus_care_Data_Cleaning.sql`: Data hygiene scripts standardizing phone numbers, dates, whitespace trimming, and handling missing values.
  * `03.healthplus_care_Data_Validation.sql`: Data integrity checks verifying orphan foreign keys and domain range constraints.
  * `04.healthplus_care_Business_Analysis.sql`: 25 strategic SQL queries evaluating operational volume, revenue streams, doctor consultation fees, and patient feedback ratings.

---

## 2. Hospital Analytics Database System (`HospitalAnalyticsDB`)

* **Directory:** [`SQL/Hospital_Analytics_DB/`](Hospital_Analytics_DB/)
* **Scale:** 15 normalized relational tables monitoring multi-hospital networks, clinical departments, physician staffing, emergency admissions, room bed capacity, medical procedures, pharmacy distribution, and billing.
* **Core Pipeline Files:**
  * `01.Hospital_Analytics_Table_Database_Setup.sql`: Network DDL schema definition and table setup.
  * `02.Hospital_Analytics_Data_Cleaning.sql`: Data sanitization routines, date casting, and room status standardization.
  * `03.Hospital_Analytics_Data_Validation.sql`: Relational consistency verification and constraint audits.
  * `04.Hospital_Analytics_Business_Analysis.sql`: 25 complex business queries uncovering bed occupancy trends, admission volumes, treatment expenses, and laboratory turnover.

---

## Technical Skills Demonstrated in SQL
* **Relational Schema Design (DDL):** Normalized 3NF entity-relationship architectures, primary and foreign key constraints, column data typing (`INT`, `VARCHAR`, `DECIMAL`, `DATE`).
* **Data Cleansing & ETL (DML):** `UPDATE`, `CASE WHEN`, `TRIM`, `NULLIF`, `LOWER`, string replacement, and handling disparate CSV imports.
* **Advanced Analytical Querying:** Multi-table `INNER JOIN` / `LEFT JOIN`, aggregations (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`), grouping (`GROUP BY`, `HAVING`), ordering, and limiting.
* **Data Quality & Validation:** Systematic queries auditing duplicate rows, orphan records across child tables, and domain integrity.

---

## Directory Organization
```
SQL/
├── README.md
├── HealthPlus_Care_DB/
│   ├── README.md
│   ├── Cleaned/
│   │   ├── 01.healthplus_care_table_Database_Setup.sql
│   │   ├── 02.healthplus_care_Data_Cleaning.sql
│   │   ├── 03.healthplus_care_Data_Validation.sql
│   │   └── 04.healthplus_care_Business_Analysis.sql
│   ├── CSV/
│   │   └── (17 CSV data tables)
│   ├── Images/
│   └── Raw/
│       └── HealthPlus_Care_DB_dataset.xlsx
└── Hospital_Analytics_DB/
    ├── README.md
    ├── Cleaned/
    │   ├── 01.Hospital_Analytics_Table_Database_Setup.sql
    │   ├── 02.Hospital_Analytics_Data_Cleaning.sql
    │   ├── 03.Hospital_Analytics_Data_Validation.sql
    │   └── 04.Hospital_Analytics_Business_Analysis.sql
    ├── CSV/
    │   └── (15 CSV data tables)
    ├── Images/
    └── Raw/
        └── Hospital_Analytics_DB_dataset.xlsx
```
