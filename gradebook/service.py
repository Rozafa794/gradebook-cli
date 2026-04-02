from .models import Student, Course, Enrollment
from .storage import load_data, save_data


def add_student(name):
    
    # Add a new student and return the new student ID.
    
    data = load_data()

    existing_ids = [student["id"] for student in data["students"]]
    new_id = max(existing_ids, default=0) + 1

    student = Student(new_id, name)

    data["students"].append({
        "id": student.id,
        "name": student.name
    })

    save_data(data)
    return student.id


def add_course(code, title):
    
    # Add a new course.
    
    data = load_data()

    for existing_course in data["courses"]:
        if existing_course["code"].lower() == code.strip().lower():
            raise ValueError("Course code already exists.")

    course = Course(code, title)

    data["courses"].append({
        "code": course.code,
        "title": course.title
    })

    save_data(data)


def enroll(student_id, course_code):
    
    # Enroll a student in a course.
    
    data = load_data()

    student_exists = any(student["id"] == student_id for student in data["students"])
    if not student_exists:
        raise ValueError("Student not found.")

    course_exists = any(
        course["code"].lower() == course_code.strip().lower()
        for course in data["courses"]
    )
    if not course_exists:
        raise ValueError("Course not found.")

    already_enrolled = any(
        enrollment["student_id"] == student_id
        and enrollment["course_code"].lower() == course_code.strip().lower()
        for enrollment in data["enrollments"]
    )
    if already_enrolled:
        raise ValueError("Student is already enrolled in this course.")

    enrollment = Enrollment(student_id, course_code, [])

    data["enrollments"].append({
        "student_id": enrollment.student_id,
        "course_code": enrollment.course_code,
        "grades": enrollment.grades
    })

    save_data(data)


def add_grade(student_id, course_code, grade):
    
    # Add a grade to a student's enrollment in a course.
    
    data = load_data()

    for enrollment in data["enrollments"]:
        if (
            enrollment["student_id"] == student_id
            and enrollment["course_code"].lower() == course_code.strip().lower()
        ):
            temp_enrollment = Enrollment(
                enrollment["student_id"],
                enrollment["course_code"],
                enrollment["grades"]
            )
            temp_enrollment.add_grade(grade)
            enrollment["grades"] = temp_enrollment.grades
            save_data(data)
            return

    raise ValueError("Enrollment not found.")


def list_students():
    
    # Return all students sorted by ID.
    
    data = load_data()

    return sorted(
        data["students"],
        key=lambda student: student["id"]
    )


def list_courses():
    
    # Return all courses sorted by code.
    
    data = load_data()

    return sorted(
        data["courses"],
        key=lambda course: course["code"].lower()
    )


def list_enrollments():
    
    # Return all enrollments sorted by student ID and course code.
    
    data = load_data()

    return sorted(
        data["enrollments"],
        key=lambda enrollment: (
            enrollment["student_id"],
            enrollment["course_code"].lower()
        )
    )


def compute_average(student_id, course_code):
    
    # Compute the average grade for a student's course enrollment.
    
    data = load_data()

    for enrollment in data["enrollments"]:
        if (
            enrollment["student_id"] == student_id
            and enrollment["course_code"].lower() == course_code.strip().lower()
        ):
            grades = enrollment["grades"]
            if not grades:
                return 0.0
            return sum(grades) / len(grades)

    raise ValueError("Enrollment not found.")


def compute_gpa(student_id):
    
    # Compute the GPA for a student as the average of course averages.
    
    data = load_data()

    student_exists = any(student["id"] == student_id for student in data["students"])
    if not student_exists:
        raise ValueError("Student not found.")

    student_enrollments = [
        enrollment for enrollment in data["enrollments"]
        if enrollment["student_id"] == student_id
    ]

    if not student_enrollments:
        return 0.0

    course_averages = [
        (sum(enrollment["grades"]) / len(enrollment["grades"]))
        for enrollment in student_enrollments
        if enrollment["grades"]
    ]

    if not course_averages:
        return 0.0

    return sum(course_averages) / len(course_averages)