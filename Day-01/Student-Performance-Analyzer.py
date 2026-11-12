raw_students = [
    {"name": "Ali",   "marks": [80, 90, 70]},
    {"name": "Sara",  "marks": [95, 85, 90]},
    {"name": "Hamza", "marks": [40, 35, 50]},
    {"name": "Ali",   "marks": [80, 90, 70]},   # duplicate
]
PASS_MARK = 50

# Returns a student dict with name, marks list, plus extras like age
def create_student(name, *marks, **extra):
    student = {"name":name,"marks":marks}
    student.update(extra)
    return student

# Drops repeated records
def remove_duplicates(students):
    return 0
# Returns (total, average)
def calculate_stats(student):
    total = 0
    for k,v in student.items():
        total += student["marks"]
        n = len(student)
        if n==0:
            return 0, 0 
        average = total/n

# Returns the student with the highest average
def find_top_student(students):

# Returns two lists: passed, failed	
def split_pass_fail(students):

# Prints the report
def print_report(students):