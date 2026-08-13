create table Hospital (
hospital_id varchar(10),
hospital_name varchar(100),
hospital_type varchar(50),
city varchar(50),
state varchar(50),
region varchar(50),
bed_capacity int,
established_year int,
contact_number varchar(20),
email varchar(50),
constraint pk_hospital_id primary key (hospital_id));

create table Departments (
department_id varchar(15),
department_name varchar(50),
hospital_id varchar(10),
floor_number varchar(3),
head_doctor_id varchar(15),
constraint pk_department_id primary key (department_id));

create table Doctors (
doctor_id varchar(15),
first_name varchar(30),
last_name varchar(30),
gender varchar(10),
specialization varchar(50),
department_id varchar(15),
hospital_id varchar(10),
qualification varchar(30),
experience_years int,
consultation_fee decimal(10,2),
phone_number varchar(15),
email varchar(50),
joining_date date,
constraint pk_doctor_id primary key (doctor_id));

create table Patients (
patient_id varchar(20),
first_name varchar(30),
last_name varchar(25),
gender varchar(10),
date_of_birth date,
age int,
city varchar(30),
state varchar(30),
phone_number varchar(20),
email varchar(50),
blood_group varchar(6),
registration_date date,
constraint pk_patient_id primary key (patient_id));


create table Rooms (
room_id varchar(15),
hospital_id varchar(10),
room_number int,
room_type varchar(15),
floor_number int,
daily_charge decimal(10,2),
room_status varchar(15),
constraint pk_room_id primary key (room_id));


create table Appointments (
appointment_id varchar(30),
patient_id varchar(20),
doctor_id varchar(15),
hospital_id varchar(10),
appointment_date date,
appointment_time time,
status varchar(30),
reason_for_visit varchar(50),
created_at timestamp,
constraint pk_appointment_id primary key (appointment_id));

create table Admissions (
admission_id varchar(20),
patient_id varchar(20),
hospital_id varchar(10),
department_id varchar(15),
admitting_doctor_id varchar(15),
room_id varchar(15),
admission_date date,
discharge_date date,
admission_type varchar(30),
admission_status varchar(30),
constraint pk_admission_id primary key (admission_id));


create table Treatments (
treatment_id varchar(20),
admission_id varchar(20),
patient_id varchar(20),
doctor_id varchar(15),
treatment_name varchar(100),
treatment_date date,
treatment_cost decimal(10,2),
treatment_status varchar(30),
constraint pk_treatment_id primary key (treatment_id));


create table Insurance (
insurance_id varchar(20),
patient_id varchar(20),
insurance_provider varchar(100),
policy_number varchar(30),
coverage_amount decimal(12,2),
policy_start_date date,
policy_end_date date,
claim_status varchar(30),
constraint pk_insurance_id primary key (insurance_id));


create table Medicines (
medicine_id varchar(20),
medicine_name varchar(100),
category varchar(50),
manufacturer varchar(100),
unit_price decimal(10,2),
stock_quantity int,
constraint pk_medicine_id primary key (medicine_id));



create table Pharmacy (
pharmacy_sale_id varchar(20),
patient_id varchar(20),
medicine_id varchar(20),
hospital_id varchar(10),
quantity int,
sale_date date,
total_price decimal(10,2),
constraint pk_pharmacy_sale_id primary key (pharmacy_sale_id));



create table Laboratory (
lab_test_id varchar(20),
patient_id varchar(20),
doctor_id varchar(15),
hospital_id varchar(10),
test_name varchar(100),
test_date date,
test_result varchar(50),
test_cost decimal(10,2),
test_status varchar(30),
constraint pk_lab_test_id primary key (lab_test_id));



create table Employees (
employee_id varchar(20),
first_name varchar(30),
last_name varchar(30),
gender varchar(10),
hospital_id varchar(10),
department_id varchar(15),
designation varchar(50),
employment_type varchar(30),
salary decimal(12,2),
joining_date date,
phone_number varchar(15),
email varchar(50),
constraint pk_employee_id primary key (employee_id));



create table Billing (
bill_id varchar(20),
patient_id varchar(20),
admission_id varchar(20),
appointment_id varchar(30),
bill_date date,
room_charges decimal(10,2),
doctor_charges decimal(10,2),
medicine_charges decimal(10,2),
lab_charges decimal(10,2),
other_charges decimal(10,2),
total_amount decimal(12,2),
bill_status varchar(30),
constraint pk_bill_id primary key (bill_id));


create table Payments (
payment_id varchar(20),
bill_id varchar(20),
patient_id varchar(20),
payment_date date,
payment_amount decimal(12,2),
payment_mode varchar(30),
payment_status varchar(30),
constraint pk_payment_id primary key (payment_id));