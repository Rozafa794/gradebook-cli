import argparse

from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
    list_students,
    list_courses,
    list_enrollments,
    compute_average,
    compute_gpa,
)


def parse_grade(value):
    
    # Parse and validate a grade value.
    
    try:
        grade = float(value)
    except ValueError as error:
        raise ValueError("Grade must be a number.") from error

    if not 0 <= grade <= 100:
        raise ValueError("Grade must be between 0 and 100.")

    return grade


def main():
    parser = argparse.ArgumentParser(
        description="Gradebook CLI - manage students, courses, and grades."
    )

    subparsers = parser.add_subparsers(dest="command")

    add_student_parser = subparsers.add_parser("add-student", help="Add a new student")
    add_student_parser.add_argument("--name", required=True, help="Student name")

    add_course_parser = subparsers.add_parser("add-course", help="Add a new course")
    add_course_parser.add_argument("--code", required=True, help="Course code")
    add_course_parser.add_argument("--title", required=True, help="Course title")

    enroll_parser = subparsers.add_parser("enroll", help="Enroll a student in a course")
    enroll_parser.add_argument("--student-id", required=True, type=int, help="Student ID")
    enroll_parser.add_argument("--course", required=True, help="Course code")

    add_grade_parser = subparsers.add_parser("add-grade", help="Add a grade")
    add_grade_parser.add_argument("--student-id", required=True, type=int, help="Student ID")
    add_grade_parser.add_argument("--course", required=True, help="Course code")
    add_grade_parser.add_argument("--grade", required=True, help="Grade value")

    list_parser = subparsers.add_parser("list", help="List data")
    list_parser.add_argument(
        "target",
        choices=["students", "courses", "enrollments"],
        help="What to list"
    )

    avg_parser = subparsers.add_parser("avg", help="Compute course average")
    avg_parser.add_argument("--student-id", required=True, type=int, help="Student ID")
    avg_parser.add_argument("--course", required=True, help="Course code")

    gpa_parser = subparsers.add_parser("gpa", help="Compute GPA for a student")
    gpa_parser.add_argument("--student-id", required=True, type=int, help="Student ID")

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            student_id = add_student(args.name)
            print(f"Student added successfully with ID {student_id}.")

        elif args.command == "add-course":
            add_course(args.code, args.title)
            print("Course added successfully.")

        elif args.command == "enroll":
            enroll(args.student_id, args.course)
            print("Student enrolled successfully.")

        elif args.command == "add-grade":
            grade = parse_grade(args.grade)
            add_grade(args.student_id, args.course, grade)
            print("Grade added successfully.")

        elif args.command == "list":
            if args.target == "students":
                students = list_students()
                if not students:
                    print("No students found.")
                else:
                    for student in students:
                        print(f"ID: {student['id']}, Name: {student['name']}")

            elif args.target == "courses":
                courses = list_courses()
                if not courses:
                    print("No courses found.")
                else:
                    for course in courses:
                        print(f"Code: {course['code']}, Title: {course['title']}")

            elif args.target == "enrollments":
                enrollments = list_enrollments()
                if not enrollments:
                    print("No enrollments found.")
                else:
                    for enrollment_item in enrollments:
                        print(
                            f"Student ID: {enrollment_item['student_id']}, "
                            f"Course: {enrollment_item['course_code']}, "
                            f"Grades: {enrollment_item['grades']}"
                        )

        elif args.command == "avg":
            average = compute_average(args.student_id, args.course)
            print(f"Average: {average:.2f}")

        elif args.command == "gpa":
            gpa = compute_gpa(args.student_id)
            print(f"GPA: {gpa:.2f}")

        else:
            parser.print_help()

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()