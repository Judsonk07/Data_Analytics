# HealthPlus Care Enterprise Database Management System

## Executive Summary
**HealthPlus Care** is an integrated regional healthcare delivery network providing outpatient clinics, specialist medical consultations, corporate health wellness programs, telemedicine sessions, diagnostic laboratory services, and insurance claims processing.

This project implements a complete relational database management and business intelligence analytics solution in **SQL (MySQL)**. It encompasses end-to-end data engineering: schema definition (DDL), data transformation and cleaning scripts, relational integrity validation, and 25 analytical SQL queries resolving real-world clinical and operational business challenges.

---

## Database Architecture & Entity Relationships

The `healthplus_care_db` database is structured into **17 relational tables**:

```
                                  +---------------+
                                  |   CLINICS     |
                                  +-------+-------+
                                          | 1:N
                                          v
+------------------+ 1:N         +-----------------+         1:N +-------------------+
|  CORPORATES      | ----------> |  SPECIALISTS    | <---------- |  CONSULTATIONS    |
+--------+---------+             +--------+--------+             +---+-----------+---+
         | 1:N                            | 1:N                      | 1:1       | 1:1
         v                                v                          v           v
+------------------+             +-----------------+         +-----------+   +---------------+
|CORPORATE_MEMBERS |             | CHRONIC_CARE    |         |TELEMEDICINE|  | PRESCRIPTIONS |
+--------+---------+             +-----------------+         +-----------+   +---------------+
         | N:1                            ^                          |
         v                                |                          |
+------------------+ 1:N                  |                          |
|    MEMBERS       | ---------------------+                          |
+--------+---------+                                                 |
         | 1:N                                                       |
         +---------------------------------------+                   |
         |                   |                   |                   |
         v                   v                   v                   v
+------------------+  +---------------+  +---------------+   +---------------+
| PACKAGE_SUBSCRIP |  |   BILLING     |  |    CLAIMS     |   |   FEEDBACK    |
+------------------+  +-------+-------+  +---------------+   +---------------+
                              | 1:N
                              v
                      +---------------+
                      |   PAYMENTS    |
                      +---------------+
```

### Table Definitions & Primary Keys
1. **`clinics`**: Clinic metadata, facility type, city, state, established year, contact.
2. **`specialists`**: Medical doctors, specializations, qualifications, experience years, consultation fees.
3. **`members`**: Patient roster, demographics (age, gender, DOB, city), membership tier (`Gold`, `Silver`, `Bronze`), registration dates.
4. **`corporates`**: Corporate wellness clients, enterprise contract dates, covered employee headcounts.
5. **`corporate_members`**: Link between enterprise corporate contracts and individual insured members.
6. **`consultations`**: Clinical appointments, consultation mode (`In-Person`, `Telemedicine`), completion status.
7. **`telemedicine_sessions`**: Video session technical performance, connection quality, platform metadata.
8. **`chronic_care_programs`**: Long-term illness monitoring (Hypertension, Diabetes, Asthma), review schedules.
9. **`health_packages`**: Preventive care checkup bundles and package pricing.
10. **`package_subscriptions`**: Member package purchase logs.
11. **`lab_tests`**: Pathology and diagnostic investigations, test status, test costs.
12. **`prescriptions`**: Medication orders linked to consultation encounters.
13. **`billing`**: Master patient invoices, gross billing amounts, discounts, tax calculations.
14. **`payments`**: Payment ledger records, transaction modes (UPI, Cards, Cash), settlement status.
15. **`claims`**: Health insurance claim submissions, claim amounts, adjudication statuses.
16. **`feedback`**: Patient satisfaction surveys, NPS ratings, care reviews.
17. **`staff`**: Administrative and nursing personnel registry.

---

## Data Pipeline & SQL Script Organization

```
SQL/HealthPlus_Care_DB/
├── README.md
├── Cleaned/
│   ├── 01.healthplus_care_table_Database_Setup.sql     # DDL: Database creation & table schema
│   ├── 02.healthplus_care_Data_Cleaning.sql            # DML: Data hygiene, casing, NULL handling
│   ├── 03.healthplus_care_Data_Validation.sql          # DQL: Integrity checks & anomaly detection
│   └── 04.healthplus_care_Business_Analysis.sql        # DQL: 25 business intelligence queries
├── CSV/                                                # Normalized CSV data sources (17 tables)
│   ├── Billing.csv
│   ├── Chronic_Care_Programs.csv
│   ├── Claims.csv
│   ├── Clinics.csv
│   ├── Consultations.csv
│   ├── Corporates.csv
│   ├── Feedback.csv
│   ├── Lab_Tests.csv
│   ├── Members.csv
│   ├── Payments.csv
│   ├── Specialists.csv
│   └── ...
├── Images/
└── Raw/
    └── HealthPlus_Care_DB_dataset.xlsx                 # Original uncleaned workbook
```

---

## Key SQL Business Queries & Analytical Insights

The project answers **25 strategic healthcare operational and clinical questions** in `04.healthplus_care_Business_Analysis.sql`. Below is a selection of critical queries:

### 1. Total Network Revenue & Financial Scale
```sql
SELECT 
    COUNT(DISTINCT bill_id) AS total_bills_generated,
    SUM(total_amount) AS total_gross_revenue,
    AVG(total_amount) AS average_bill_size,
    MIN(total_amount) AS min_bill,
    MAX(total_amount) AS max_bill
FROM billing;
```
*Business Value:* Determines aggregate network billing turnover, enabling finance teams to forecast cash flows and identify outlier high-cost medical procedures.

### 2. Specialist Specialization Distribution
```sql
SELECT 
    specialization,
    COUNT(*) AS total_specialists,
    ROUND(AVG(consultation_fee), 2) AS avg_fee
FROM specialists
GROUP BY specialization
ORDER BY total_specialists DESC;
```
*Business Value:* Highlights doctor capacity across cardiology, neurology, pediatrics, and general medicine, revealing departmental recruitment priorities.

### 3. Patient Consultation Modes (Digital Health vs In-Person)
```sql
SELECT 
    consultation_mode,
    COUNT(*) AS total_consultations,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM consultations), 2) AS pct_share
FROM consultations
GROUP BY consultation_mode;
```
*Business Value:* Measures the adoption rate of telemedicine versus traditional brick-and-mortar clinic visits.

### 4. Insurance Claims Settlement & Risk Analysis
```sql
SELECT 
    claim_status,
    COUNT(*) AS total_claims,
    SUM(claim_amount) AS total_claimed_amount,
    ROUND(AVG(claim_amount), 2) AS avg_claim_value
FROM claims
GROUP BY claim_status;
```
*Business Value:* Assesses claim approval, pending, and rejection ratios, mitigating disputes with third-party insurance providers.

### 5. Patient Satisfaction Ratings Analysis
```sql
SELECT 
    rating,
    COUNT(*) AS total_feedback_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM feedback), 2) AS percentage
FROM feedback
GROUP BY rating
ORDER BY rating DESC;
```
*Business Value:* Monitors Net Promoter Score (NPS) and service satisfaction across doctor bedside manner, facility cleanliness, and wait times.

---

## Technical Competencies in SQL
* **DDL Schema Architecture:** Design of primary keys, foreign key relationships, optimal data types (`VARCHAR`, `DECIMAL`, `DATE`, `INT`), and constraint enforcement.
* **Data Cleansing Pipelines:** Implemented string manipulation (`TRIM`, `LOWER`), conditional logic (`CASE WHEN`), and `NULLIF` transformations to standardize gender entries, phone formats, and missing values.
* **Complex Analytical Queries:** Utilized multi-table `JOIN` statements, `GROUP BY`, aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`), `HAVING` filters, and window ranking functions.
