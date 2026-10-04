import unittest

from models import Student
from services import AcademicService, ValidationService


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        self.student = Student(
            student_id="STU001",
            name="Test Student",
            email="test@example.com",
            phone="9876543210",
            department="Computer Technology",
            attendance=75,
            python_marks=80,
            sql_marks=70,
            excel_marks=90
        )

    # -------------------------
    # Attendance Tests
    # -------------------------

    def test_attendance_75_is_valid(self):
        self.assertEqual(
            ValidationService.validate_attendance(75),
            75
        )

    def test_attendance_0_is_valid(self):
        self.assertEqual(
            ValidationService.validate_attendance(0),
            0
        )

    def test_attendance_100_is_valid(self):
        self.assertEqual(
            ValidationService.validate_attendance(100),
            100
        )

    def test_attendance_negative_is_invalid(self):
        with self.assertRaises(ValueError):
            ValidationService.validate_attendance(-5)

    def test_attendance_above_100_is_invalid(self):
        with self.assertRaises(ValueError):
            ValidationService.validate_attendance(105)

    # -------------------------
    # Marks Tests
    # -------------------------

    def test_marks_negative_is_invalid(self):
        with self.assertRaises(ValueError):
            ValidationService.validate_marks(-10)

    def test_marks_above_100_is_invalid(self):
        with self.assertRaises(ValueError):
            ValidationService.validate_marks(110)

    # -------------------------
    # Academic Calculation Tests
    # -------------------------

    def test_total_marks(self):
        self.assertEqual(
            AcademicService.calculate_total(self.student),
            240
        )

    def test_average_marks(self):
        self.assertAlmostEqual(
            AcademicService.calculate_average(self.student),
            80.0
        )

    def test_pass_result(self):
        self.assertTrue(
            AcademicService.check_pass(self.student)
        )

    def test_attendance_eligibility(self):
        self.assertTrue(
            AcademicService.check_attendance(self.student)
        )

    def test_grade(self):
        self.assertEqual(
            AcademicService.calculate_grade(self.student),
            "A"
        )


if __name__ == "__main__":
    unittest.main()