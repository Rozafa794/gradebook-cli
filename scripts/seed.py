from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from gradebook.service import add_student, add_course, enroll, add_grade
from gradebook.storage import save_data


def seed_data():
    
    # Seed the gradebook with sample data.
    
    empty_data = {
        "students": [],
        "courses": [],
        "enrollments": []
    }
    save_data(empty_data)

    student_id_1 = add_student("Rozafa Hajrizi")
    student_id_2 = add_student("Arta Berisha")
    student_id_3 = add_student("Dren Kelmendi")

    add_course("CS101", "Introduction to Computer Science")
    add_course("MATH201", "Business Mathematics")

    enroll(student_id_1, "CS101")
    enroll(student_id_1, "MATH201")
    enroll(student_id_2, "CS101")
    enroll(student_id_3, "MATH201")

    add_grade(student_id_1, "CS101", 95)
    add_grade(student_id_1, "CS101", 88)
    add_grade(student_id_1, "MATH201", 91)

    add_grade(student_id_2, "CS101", 78)
    add_grade(student_id_2, "CS101", 84)

    add_grade(student_id_3, "MATH201", 89)
    add_grade(student_id_3, "MATH201", 93)

    print("Sample data seeded successfully.")


if __name__ == "__main__":
    seed_data()