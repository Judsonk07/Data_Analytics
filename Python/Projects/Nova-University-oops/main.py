from models import Student, Faculty
from services import AcademicService, ValidationService


class StudentManagementSystem:
    """Main application class."""

    def __init__(self):
        self.students = []
        self.faculty_members = []

    # -------------------------
    # Input Helper Methods
    # -------------------------

    def get_text_input(self, message):
        while True:
            value = input(message).strip()

            if value:
                return value

            print("Input cannot be empty. Please try again.")

    def get_number_input(self, message, value_type=float):
        while True:
            try:
                return value_type(input(message))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_marks(self, subject):
        while True:
            marks = self.get_number_input(
                f"Enter {subject} marks (0-100): ",
                float
            )

            try:
                ValidationService.validate_marks(marks)
                return marks
            except ValueError as error:
                print(f"Error: {error}")

    def get_attendance(self):
        while True:
            attendance = self.get_number_input(
                "Enter attendance percentage (0-100): ",
                float
            )

            try:
                ValidationService.validate_attendance(attendance)
                return attendance
            except ValueError as error:
                print(f"Error: {error}")

    # -------------------------
    # Student Methods
    # -------------------------

    def add_student(self):
        print("\n========== ADD STUDENT ==========")

        student_id = self.get_text_input("Enter Student ID: ")

        if any(
            student.student_id == student_id
            for student in self.students
        ):
            print("Student ID already exists.")
            return

        name = self.get_text_input("Enter Name: ")
        email = self.get_text_input("Enter Email: ")
        phone = self.get_text_input("Enter Phone: ")
        department = self.get_text_input("Enter Department: ")

        attendance = self.get_attendance()

        python_marks = self.get_marks("Python")
        sql_marks = self.get_marks("SQL")
        excel_marks = self.get_marks("Excel")

        student = Student(
            student_id,
            name,
            email,
            phone,
            department,
            attendance,
            python_marks,
            sql_marks,
            excel_marks
        )

        self.students.append(student)

        print("\nStudent added successfully!")

    def view_students(self):
        print("\n========== STUDENT LIST ==========")

        if not self.students:
            print("No student records available.")
            return

        for student in self.students:
            print(student.display_info())
            print("-" * 40)

    def find_student(self):
        if not self.students:
            print("No student records available.")
            return None

        student_id = self.get_text_input("Enter Student ID: ")

        for student in self.students:
            if student.student_id == student_id:
                return student

        print("Student not found.")
        return None

    def check_attendance(self):
        print("\n========== ATTENDANCE ELIGIBILITY ==========")

        student = self.find_student()

        if student:
            if AcademicService.check_attendance(student):
                print(
                    f"{student.name} is eligible for the examination."
                )
            else:
                print(
                    f"{student.name} is NOT eligible for the examination."
                )

    def view_academic_result(self):
        print("\n========== ACADEMIC RESULT ==========")

        student = self.find_student()

        if student:
            total = AcademicService.calculate_total(student)
            average = AcademicService.calculate_average(student)
            passed = AcademicService.check_pass(student)
            grade = AcademicService.calculate_grade(student)

            print(f"\nStudent: {student.name}")
            print(f"Student ID: {student.student_id}")
            print(f"Python Marks: {student.python_marks}")
            print(f"SQL Marks: {student.sql_marks}")
            print(f"Excel Marks: {student.excel_marks}")
            print(f"Total Marks: {total}")
            print(f"Average Marks: {average:.2f}")
            print(f"Result: {'PASS' if passed else 'FAIL'}")
            print(f"Grade: {grade}")

    # -------------------------
    # Faculty Methods
    # -------------------------

    def add_faculty(self):
        print("\n========== ADD FACULTY ==========")

        faculty_id = self.get_text_input("Enter Faculty ID: ")

        if any(
            faculty.faculty_id == faculty_id
            for faculty in self.faculty_members
        ):
            print("Faculty ID already exists.")
            return

        name = self.get_text_input("Enter Name: ")
        email = self.get_text_input("Enter Email: ")
        phone = self.get_text_input("Enter Phone: ")
        department = self.get_text_input("Enter Department: ")
        designation = self.get_text_input("Enter Designation: ")

        faculty = Faculty(
            faculty_id,
            name,
            email,
            phone,
            department,
            designation
        )

        self.faculty_members.append(faculty)

        print("\nFaculty added successfully!")

    def view_faculty(self):
        print("\n========== FACULTY LIST ==========")

        if not self.faculty_members:
            print("No faculty records available.")
            return

        for faculty in self.faculty_members:
            print(faculty.display_info())
            print("-" * 40)

    # -------------------------
    # Menu
    # -------------------------

    def display_menu(self):
        print("\n")
        print("=" * 45)
        print("       NOVA UNIVERSITY")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Add Student")
        print("2. View Students")
        print("3. Check Attendance Eligibility")
        print("4. View Academic Result")
        print("5. Add Faculty")
        print("6. View Faculty")
        print("7. Exit")

        print("=" * 45)

    def run(self):
        while True:
            self.display_menu()

            choice = input("Enter your choice (1-7): ").strip()

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.check_attendance()

            elif choice == "4":
                self.view_academic_result()

            elif choice == "5":
                self.add_faculty()

            elif choice == "6":
                self.view_faculty()

            elif choice == "7":
                print("\nThank you for using Nova University Student Management System.")
                break

            else:
                print("Invalid choice. Please select a number from 1 to 7.")


if __name__ == "__main__":
    application = StudentManagementSystem()
    application.run()