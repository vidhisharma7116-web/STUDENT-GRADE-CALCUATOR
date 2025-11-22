students = {}     # key = roll, value = Student object


def add_student(student):
    students[student.roll] = student


def get_student(roll):
    return students.get(roll)


def update_student(roll, new_student):
    students[roll] = new_student


def delete_student(roll):
    if roll in students:
        del students[roll]


def get_all_students():
    return students.values()