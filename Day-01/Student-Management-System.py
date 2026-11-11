"""
Day 1 - Step 1 Practical Task: Student Management System

Question:
Create a student management program using a dictionary.
The program should:
    1. Store multiple students.
    2. Store each student's name, age, and marks.
    3. Add a new student.
    4. Update an existing student's marks.
    5. Find the student with the highest marks.
    6. Display all students.

Concepts used: nested dictionaries, .items(), functions, return values,
tuple unpacking.
"""


def add_student(students, student_id, name, age, marks):
    """Add a new student to the dictionary."""
    students[student_id] = {"name": name, "age": age, "marks": marks}


def update_marks(students, student_id, new_marks):
    """Update marks of an existing student."""
    students[student_id]["marks"] = new_marks


def find_top_student(students):
    """Return (name, marks) of the highest scorer, or None if empty.
    On a tie, the first student to reach the top score wins."""
    top_marks = 0
    top_id = None
    for student_id, info in students.items():
        if info["marks"] > top_marks:
            top_marks = info["marks"]
            top_id = student_id
    if top_id is None:
        return None
    return students[top_id]["name"], top_marks


def display_students(students):
    """Print every student."""
    for student_id, info in students.items():
        print(student_id, info)


def main():
    students = {
        "student-1": {"name": "Ali", "age": 21, "marks": 99},
        "student-2": {"name": "Haider", "age": 22, "marks": 100},
    }

    add_student(students, "student-3", "Mutwassim", 22, 100)
    update_marks(students, "student-1", 98)

    result = find_top_student(students)
    if result:
        name, marks = result
        print(f"Top student: {name} with {marks} marks")

    print("\nAll students:")
    display_students(students)


if __name__ == "__main__":
    main()