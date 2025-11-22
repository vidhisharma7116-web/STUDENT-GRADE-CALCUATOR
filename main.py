from student import Student
import grade_calc
import storage
from menu import show_menu
import utils


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = utils.input_marks()

        s = Student(roll, name, marks)
        storage.add_student(s)
        print("Student added successfully.")

    elif choice == "2":
        roll = input("Enter roll number: ")
        s = storage.get_student(roll)
        if s:
            s.display()
            total = grade_calc.calculate_total(s.marks)
            percentage = grade_calc.calculate_percentage(s.marks)
            grade = grade_calc.calculate_grade(percentage)

            print("Total Marks:", total)
            print("Percentage:", percentage)
            print("Grade:", grade)
        else:
            print("Student not found.")

    elif choice == "3":
        roll = input("Enter roll number to update: ")
        s = storage.get_student(roll)
        if s:
            name = input("Enter new name: ")
            marks = utils.input_marks()

            updated = Student(roll, name, marks)
            storage.update_student(roll, updated)
            print("Student updated successfully.")
        else:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter roll number to delete: ")
        storage.delete_student(roll)
        print("Student deleted.")

    elif choice == "5":
        print(" All Students ")
        all_students = storage.get_all_students()
        for stu in all_students:
            stu.display()

    elif choice == "6":
        print("Exiting program!")
        break

    else:
        print("Invalid choice.")