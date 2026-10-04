class AcademicService:
    """Reusable academic rules and calculations."""

    PASS_MARK = 50
    ATTENDANCE_REQUIRED = 75

    @staticmethod
    def calculate_total(student):
        return student.total_marks()

    @staticmethod
    def calculate_average(student):
        return student.average_marks()

    @staticmethod
    def check_pass(student):
        return student.average_marks() >= AcademicService.PASS_MARK

    @staticmethod
    def check_attendance(student):
        return student.attendance >= AcademicService.ATTENDANCE_REQUIRED

    @staticmethod
    def calculate_grade(student):
        return student.get_grade()


class ValidationService:
    """Handles validation rules."""

    @staticmethod
    def validate_attendance(attendance):
        if attendance < 0 or attendance > 100:
            raise ValueError(
                "Attendance must be between 0 and 100."
            )

        return attendance

    @staticmethod
    def validate_marks(marks):
        if marks < 0 or marks > 100:
            raise ValueError(
                "Marks must be between 0 and 100."
            )

        return marks