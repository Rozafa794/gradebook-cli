import unittest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from gradebook.storage import save_data
from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
    compute_average,
)


class TestService(unittest.TestCase):
    def setUp(self):
        save_data({
            "students": [],
            "courses": [],
            "enrollments": []
        })

    def test_add_student(self):
        student_id = add_student("Rozafa")
        self.assertEqual(student_id, 1)

    def test_add_grade_and_compute_average(self):
        student_id = add_student("Rozafa")
        add_course("CS101", "Intro to CS")
        enroll(student_id, "CS101")
        add_grade(student_id, "CS101", 90)
        add_grade(student_id, "CS101", 80)

        average = compute_average(student_id, "CS101")
        self.assertEqual(average, 85.0)

    def test_add_invalid_grade(self):
        student_id = add_student("Rozafa")
        add_course("CS101", "Intro to CS")
        enroll(student_id, "CS101")

        with self.assertRaises(ValueError):
            add_grade(student_id, "CS101", 150)


if __name__ == "__main__":
    unittest.main()