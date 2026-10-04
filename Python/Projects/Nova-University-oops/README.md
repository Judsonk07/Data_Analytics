# Nova University - Student Management System

## 1. Project Overview

The Nova University Student Management System is a Python-based console application developed using Object-Oriented Programming (OOP).

The application maintains student and faculty information and provides academic features such as attendance eligibility, marks calculation, result status, and grade calculation.

## 2. Business Problem

Nova University requires a simple system to maintain basic student and faculty information and perform basic academic checks.

The application provides a structured and maintainable way to:

- Add and view students
- Add and view faculty members
- Store student academic information
- Check attendance eligibility
- Calculate total marks
- Calculate average marks
- Determine pass/fail status
- Calculate student grades
- Handle invalid inputs

## 3. Technologies Used

- Python 3
- Object-Oriented Programming
- Python unittest
- Git
- GitHub

## 4. Project Structure

```text
nova-university-oop/
│
├── main.py
├── models.py
├── services.py
├── tests.py
└── README.md
```

### main.py

Contains the main application and console menu.

### models.py

Contains the main OOP classes:

- Person
- Student
- Faculty

### services.py

Contains reusable business logic and validation:

- AcademicService
- ValidationService

### tests.py

Contains automated unit tests for validation and academic calculations.

## 5. OOP Design

### Person

`Person` is the base class containing common information:

- Name
- Email
- Phone

### Student

`Student` inherits from `Person` and contains:

- Student ID
- Department
- Attendance
- Python marks
- SQL marks
- Excel marks

It also provides academic behaviours such as:

- Total marks
- Average marks
- Attendance eligibility
- Pass/fail status
- Grade

### Faculty

`Faculty` inherits from `Person` and contains:

- Faculty ID
- Department
- Designation

## 6. OOP Concepts Used

### Encapsulation

Student and faculty information is grouped inside their respective classes along with related behaviours.

### Inheritance

`Student` and `Faculty` inherit common attributes and behaviour from `Person`.

```text
Person
  |
  +-- Student
  |
  +-- Faculty
```

### Polymorphism

Both `Student` and `Faculty` provide their own implementation of `display_info()`.

### Abstraction

Reusable business operations are separated into service classes such as `AcademicService` and `ValidationService`.

## 7. Academic Rules

### Attendance Eligibility

A student with attendance of 75% or above is eligible for the examination.

```text
Attendance >= 75%
        |
        +-- Eligible
```

### Pass Rule

A student with an average mark of 50 or above is considered passed.

```text
Average >= 50
        |
        +-- PASS
```

### Grade Rules

| Average | Grade |
|---:|:---|
| 90 - 100 | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 50 - 59 | D |
| Below 50 | F |

## 8. Validation

Attendance must be between 0 and 100.

Marks must also be between 0 and 100.

The application handles invalid input without terminating unexpectedly.

Examples:

```text
Attendance: -5
Output: Attendance must be between 0 and 100.

Attendance: 105
Output: Attendance must be between 0 and 100.

Marks: 110
Output: Marks must be between 0 and 100.
```

## 9. Application Menu

The application provides the following menu:

```text
1. Add Student
2. View Students
3. Check Attendance Eligibility
4. View Academic Result
5. Add Faculty
6. View Faculty
7. Exit
```

## 10. How to Run

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/nova-university-oop.git
```

### Step 2: Open the project

```bash
cd nova-university-oop
```

### Step 3: Run the application

```bash
python main.py
```

## 11. Run Tests

Run the automated tests using:

```bash
python -m unittest tests.py -v
```

## 12. Sample Academic Calculation

Example:

```text
Python Marks: 80
SQL Marks: 70
Excel Marks: 90

Total Marks: 240
Average Marks: 80.00
Result: PASS
Grade: A

Attendance: 75%
Eligibility: Eligible
```

## 13. Testing Performed

The application was tested with:

| Test Case | Input | Expected Result |
|---|---:|---|
| Attendance boundary | 75 | Valid |
| Minimum attendance | 0 | Valid |
| Maximum attendance | 100 | Valid |
| Invalid attendance | -5 | Rejected |
| Invalid attendance | 105 | Rejected |
| Valid marks | 80 | Accepted |
| Invalid marks | -10 | Rejected |
| Invalid marks | 110 | Rejected |
| Academic calculation | Valid marks | Correct result |
| Invalid menu input | Non-numeric/invalid choice | Handled gracefully |

## 14. Conclusion

The Nova University Student Management System demonstrates how business requirements can be translated into a maintainable Python OOP application.

The application supports multiple student and faculty records, reusable academic rules, validation, academic calculations, and graceful invalid-input handling.