class Student:
    # Represents a student with an ID and a name.

    def __init__(self, student_id: int, name: str):
        if not isinstance(student_id, int) or student_id <= 0:
            raise ValueError("Student ID must be a positive integer.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty.")

        self.id = student_id
        self.name = name.strip()

    def __str__(self):
        return f"Student(ID: {self.id}, Name: {self.name})"


class Course:
    
    # Represents a course with a code and a title.
    

    def __init__(self, code: str, title: str):
        if not isinstance(code, str) or not code.strip():
            raise ValueError("Course code cannot be empty.")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Course title cannot be empty.")

        self.code = code.strip()
        self.title = title.strip()

    def __str__(self):
        return f"Course(Code: {self.code}, Title: {self.title})"


class Enrollment:
   
    # Represents a student's enrollment in a course, including a list of grades.
   

    def __init__(self, student_id: int, course_code: str, grades=None):
        if not isinstance(student_id, int) or student_id <= 0:
            raise ValueError("Student ID must be a positive integer.")
        if not isinstance(course_code, str) or not course_code.strip():
            raise ValueError("Course code cannot be empty.")

        self.student_id = student_id
        self.course_code = course_code.strip()
        self.grades = grades if grades is not None else []

        for grade in self.grades:
            self._validate_grade(grade)

    def _validate_grade(self, grade):
        if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
            raise ValueError("Grades must be numbers between 0 and 100.")

    def add_grade(self, grade):
        self._validate_grade(grade)
        self.grades.append(grade)

    def __str__(self):
        return (
            f"Enrollment(Student ID: {self.student_id}, "
            f"Course: {self.course_code}, Grades: {self.grades})"
        )