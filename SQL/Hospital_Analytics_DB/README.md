# Hospital Analytics Database System (HospitalAnalyticsDB)

## Executive Summary
**Hospital Analytics Database System (`HospitalAnalyticsDB`)** is an enterprise data management and clinical intelligence solution designed for a network of multi-specialty regional hospitals. The database monitors patient admissions, doctor assignments, hospital bed availability, emergency treatments, diagnostic laboratory tests, in-house pharmacy disbursements, billing, and insurance settlements.

This project covers the full database lifecycle in **SQL (MySQL)**: comprehensive schema engineering, data sanitization and format normalization, data consistency validation, and 25 analytical SQL scripts answering critical operational questions for hospital administrators.

---

## Database Architecture & Entity Relationships

The `HospitalAnalyticsDB` database is structured into **15 normalized relational tables**:

```
                              +------------------+
                              |    HOSPITALS     |
                              +--------+---------+
                                       | 1:N
                                       v
                              +------------------+
                              |   DEPARTMENTS    |
                              +--------+---------+
                                       | 1:N
                                       v
+------------------+ 1:N      +------------------+      1:N +-------------------+
|    EMPLOYEES     | <------- |     DOCTORS      | <------- |   APPOINTMENTS    |
+------------------+          +--------+---------+          +---+-----------+---+
                                       | 1:N                    |           |
                                       v                        v           v
+------------------+ 1:N      +------------------+          +---------------+
|     ROOMS        | <------- |    ADMISSIONS    |          |   PATIENTS    |
+------------------+          +--------+---------+          +---+---+---+---+
                                       | 1:N                    |   |   |
                                       v                        |   |   |
+------------------+ 1:N      +------------------+              |   |   |
|   MEDICINES      | <------- |    PHARMACY      | <------------+   |   |
+------------------+          +------------------+                  |   |
                                                                    |   |
+------------------+          +------------------+                  |   |
|    TREATMENTS    | <----------------------------------------------+   |
+------------------+ 1:N                                                |
                                                                        |
+------------------+          +------------------+                      |
|    LABORATORY    | <--------------------------------------------------+
+------------------+ 1:N
         |
         v
+------------------+ 1:N      +------------------+
|     BILLING      | -------> |    INSURANCE     |
+--------+---------+          +------------------+
         | 1:N
         v
+------------------+
|    PAYMENTS      |
+------------------+
```

### Table Definitions & Primary Keys
1. **`hospitals`**: Network branches, location cities, regional tags, established year, total bed capacities.
2. **`departments`**: Clinical divisions (Cardiology, Orthopedics, Pediatrics, Oncology, ICU, Emergency), floor locations, head doctors.
3. **`doctors`**: Physician profiles, credentials, specializations, consultation fees, department IDs, joining dates.
4. **`employees`**: Nursing, technical, and administrative staff supporting clinical operations.
5. **`patients`**: Master patient registry, demographics (age, gender, address, contact).
6. **`appointments`**: Outpatient scheduling, doctor consultation bookings, appointment statuses (`Completed`, `Scheduled`, `Cancelled`).
7. **`admissions`**: Inpatient admission encounters, admission type (`Emergency`, `Elective`, `Urgent`), admission/discharge dates, admission status.
8. **`rooms`**: Hospital bed inventory, room categories (`General Ward`, `Semi-Private`, `Private ICU`), occupancy status.
9. **`treatments`**: Medical procedures, surgeries, clinical therapies, assigned doctor, associated treatment costs.
10. **`laboratory`**: Diagnostic tests ordered (Blood Panels, Radiology, MRI, CT Scans), test costs, completion status.
11. **`medicines`**: Pharmaceutical formulary catalog, dosage types, manufacturer, unit prices.
12. **`pharmacy`**: Medication dispense records, quantities, prescription billing links.
13. **`billing`**: Master patient financial invoices, line-item treatment, room and test charges.
14. **`payments`**: Payment execution ledger, payment methods (Cash, Card, UPI, Insurance), payment statuses.
15. **`insurance`**: Third-party health insurance policies, policy providers, coverage limits, claim tracking.

---

## Data Pipeline & SQL Script Organization

```
SQL/Hospital_Analytics_DB/
├── README.md
├── Cleaned/
│   ├── 01.Hospital_Analytics_Table_Database_Setup.sql    # DDL: Database creation & table schema
│   ├── 02.Hospital_Analytics_Data_Cleaning.sql           # DML: Data hygiene, date casts, NULL handling
│   ├── 03.Hospital_Analytics_Data_Validation.sql         # DQL: Integrity constraints & key audits
│   └── 04.Hospital_Analytics_Business_Analysis.sql       # DQL: 25 business intelligence queries
├── CSV/                                               # Cleaned CSV data sources (15 tables)
│   ├── Admissions.csv
│   ├── Appointments.csv
│   ├── Billing.csv
│   ├── Departments.csv
│   ├── Doctors.csv
│   ├── Employees.csv
│   ├── Hospitals.csv
│   ├── Insurance.csv
│   ├── Laboratory.csv
│   ├── Medicines.csv
│   ├── Patients.csv
│   ├── Payments.csv
│   ├── Pharmacy.csv
│   ├── Rooms.csv
│   └── Treatments.csv
├── Images/
└── Raw/
    └── Hospital_Analytics_DB_dataset.xlsx                # Source Excel workbook
```

---

## Key SQL Business Queries & Analytical Insights

The repository contains **25 analytical business intelligence queries** in `04.Hospital_Analytics_Business_Analysis.sql`. Below are key sample queries:

### 1. Inpatient Admissions & Bed Utilization
```sql
SELECT 
    admission_type,
    admission_status,
    COUNT(*) AS total_admissions,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM admissions), 2) AS pct_of_admissions
FROM admissions
GROUP BY admission_type, admission_status
ORDER BY total_admissions DESC;
```
*Business Value:* Monitors patient influx between Emergency vs. Elective procedures to balance ward bed allocations.

### 2. Departmental Revenue & Doctor Workload
```sql
SELECT 
    d.department_name,
    COUNT(DISTINCT doc.doctor_id) AS total_doctors,
    COUNT(a.appointment_id) AS total_appointments,
    ROUND(AVG(doc.consultation_fee), 2) AS avg_consultation_fee
FROM departments d
LEFT JOIN doctors doc ON d.department_id = doc.department_id
LEFT JOIN appointments a ON doc.doctor_id = a.doctor_id
GROUP BY d.department_name
ORDER BY total_appointments DESC;
```
*Business Value:* Evaluates doctor staffing efficiency and patient demand across hospital specialties.

### 3. Comprehensive Billing, Revenue & Cost Distribution
```sql
SELECT 
    COUNT(bill_id) AS total_invoices,
    SUM(total_amount) AS total_gross_revenue,
    AVG(total_amount) AS avg_patient_bill,
    MIN(total_amount) AS min_invoice,
    MAX(total_amount) AS max_invoice
FROM billing;
```
*Business Value:* Provides executive visibility into aggregate healthcare financial performance and inpatient billing averages.

### 4. Diagnostic Laboratory Revenue & Testing Status
```sql
SELECT 
    test_status,
    COUNT(*) AS total_tests,
    SUM(test_cost) AS total_lab_revenue,
    ROUND(AVG(test_cost), 2) AS avg_test_cost
FROM laboratory
GROUP BY test_status;
```
*Business Value:* Tracks turnaround time and revenue contribution from diagnostic pathology and imaging centers.

### 5. Payment Methods & Settlement Integrity
```sql
SELECT 
    payment_mode,
    payment_status,
    COUNT(*) AS total_transactions,
    SUM(payment_amount) AS total_collected
FROM payments
GROUP BY payment_mode, payment_status
ORDER BY total_collected DESC;
```
*Business Value:* Assesses digital vs. insurance direct-billing settlements and identifies outstanding pending receivables.

---

## Technical Competencies in SQL
* **Relational Database Design:** Complete third-normal-form (3NF) design, foreign key cascades, date-time attribute adjustments, and index planning.
* **Data Sanitization & ETL:** Cleaned legacy dates, handled edge-case NULL attributes, standardizing text inputs, and enforcing room capacity constraints.
* **Analytical Querying:** Extensive use of table `JOIN` operations, aggregate calculations (`SUM`, `AVG`, `COUNT`), conditional aggregation, and sorting optimizations.
