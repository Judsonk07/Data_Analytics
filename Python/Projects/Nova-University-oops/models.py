class Person:
    """Base class for common person information."""

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display_info(self):
        return (
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}"
        )


class Student(Person):
    """Represents a university student."""

    def __init__(
        self,
        student_id,
        name,
        email,
        phone,
        department,
        attendance,
        python_marks,
        sql_marks,
        excel_marks
    ):
        super().__init__(name, email, phone)

        self.student_id = student_id
        self.department = department
        self.attendance = attendance
        self.python_marks = python_marks
        self.sql_marks = sql_marks
        self.excel_marks = excel_marks

    def total_marks(self):
        return (
            self.python_marks
            + self.sql_marks
            + self.excel_marks
        )

    def average_marks(self):
        return self.total_marks() / 3

    def is_attendance_eligible(self):
        return self.attendance >= 75

    def is_passed(self):
        return self.average_marks() >= 50

    def get_grade(self):
        average = self.average_marks()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def display_info(self):
        return (
            f"\nStudent ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}\n"
            f"Department: {self.department}\n"
            f"Attendance: {self.attendance}%\n"
            f"Python Marks: {self.python_marks}\n"
            f"SQL Marks: {self.sql_marks}\n"
            f"Excel Marks: {self.excel_marks}"
        )


class Faculty(Person):
    """Represents a university faculty member."""

    def __init__(
        self,
        faculty_id,
        name,
        email,
        phone,
        department,
        designation
    ):
        super().__init__(name, email, phone)

        self.faculty_id = faculty_id
        self.department = department
        self.designation = designation

    def display_info(self):
        return (
            f"\nFaculty ID: {self.faculty_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}\n"
            f"Department: {self.department}\n"
            f"Designation: {self.designation}"
        )