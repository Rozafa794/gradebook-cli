# Gradebook CLI

A simple command-line application in Python for managing students, courses, enrollments, grades, averages, and GPA.

## Project Structure

```text
Gradebook/
│
├── gradebook/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   └── service.py
│
├── data/
│   └── gradebook.json
│
├── logs/
│   └── .gitkeep
│
├── scripts/
│   └── seed.py
│
├── tests/
│   └── test_service.py
│
├── main.py
└── README.md
Features
Add students
Add courses
Enroll students in courses
Add grades to enrollments
List students, courses, and enrollments
Compute course average
Compute GPA
Store data in JSON
Run unit tests
Seed sample data
Setup
1. Create a virtual environment
python -m venv venv
2. Activate the virtual environment

On Windows:

venv\Scripts\activate
3. Run the seed script
python scripts/seed.py

This will populate the project with sample students, courses, enrollments, and grades.

CLI Commands
Add a student
python main.py add-student --name "Rozafa Hajrizi"
Add a course
python main.py add-course --code CS101 --title "Intro to CS"
Enroll a student in a course
python main.py enroll --student-id 1 --course CS101
Add a grade
python main.py add-grade --student-id 1 --course CS101 --grade 95
List students
python main.py list students
List courses
python main.py list courses
List enrollments
python main.py list enrollments
Compute average for one course
python main.py avg --student-id 1 --course CS101
Compute GPA for one student
python main.py gpa --student-id 1
Example Outputs
List students
ID: 1, Name: Rozafa Hajrizi
ID: 2, Name: Arta Berisha
ID: 3, Name: Dren Kelmendi
List courses
Code: CS101, Title: Introduction to Computer Science
Code: MATH201, Title: Business Mathematics
List enrollments
Student ID: 1, Course: CS101, Grades: [95, 88]
Student ID: 1, Course: MATH201, Grades: [91]
Student ID: 2, Course: CS101, Grades: [78, 84]
Student ID: 3, Course: MATH201, Grades: [89, 93]
Compute average
Average: 91.50
Compute GPA
GPA: 91.25
Run Tests
python -m unittest tests/test_service.py

Expected result:

...
----------------------------------------------------------------------
Ran 3 tests in 0.0xxs

OK
Design Decisions
The project uses a layered structure:
models.py for core classes
storage.py for JSON persistence
service.py for business logic
main.py for the command-line interface
Data is stored in a JSON file instead of a database to keep the project simple and easy to run.
GPA is calculated as the average of course averages.
The CLI is built using argparse for a clean command-line experience.
Limitations
The project does not include update or delete commands.
The project uses one local JSON file instead of a full database system.
Unit tests currently use the same JSON storage file, so sample data may need to be reseeded after running tests.
The CLI is designed for local usage only.
Notes

If the data file is missing, the application starts with empty data.

If the JSON file is invalid, the application handles the error and loads an empty default structure.