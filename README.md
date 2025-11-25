Student Grade Management System

A simple, menu-driven Python project designed to store student details, calculate grades, and perform basic CRUD operations — all in a clean and modular way.

Overview of the Project

The Student Grade Management System is a small console-based application created to help teachers or students manage marks in a quick and organized way.
Instead of writing marks manually or calculating grades again and again, this system does everything automatically.

The program can:
	•	Store student details (name, roll number, marks)
	•	Calculate grades instantly
	•	Display records in a neat format
	•	Allow editing or deleting entries

The entire project is written in Python, without using any external database or file system. All data is stored temporarily inside lists while the program is running.
The main intention behind this project is to understand how CRUD operations, modular programming, and basic system design work in real applications.

Why This Project? 

I chose this project because grading and record-keeping are common tasks in every school, and they often take unnecessary time when done manually.
Creating a small system that does this automatically not only makes the process faster but also avoids mistakes in calculations.

Building this project also helped me learn:
	•	How different modules of a program communicate
	•	How to design a simple workflow
	•	How to structure code cleanly
	•	How CRUD operations work in real projects

Features

The system provides the following core features:

1) Add Student

Enter name, roll number, and marks. The system immediately computes the grade.

2) View All Students

Shows all saved students in a clean table-like output.

3) Search Student

Find a student quickly using their roll number.

4) Update Student

Modify marks or correct the spelling of a name.

5) Delete Student

Remove a student permanently from the list.

6) Automatic Grade Calculation

Grades are assigned based on the student’s average marks.

7) Menu-Driven Interface

Easy navigation — no need for technical knowledge.

8) Completely Modular Code

At least 5+ Python files are used to keep the project clean and readable.

Technologies & Tools Used
	•	Python 3.x
	•	Modular Programming
	•	Functions & OOP Concepts
	•	VS Code / IDLE / PyCharm (any editor works)
	•	Terminal/Command Prompt for execution
No database, no file handling — everything runs in memory.
 
    Project structure
    •	main.py → starting point of the program
	•	student_info.py → Student class
	•	grade_calculator.py → grading logic
	•	operations.py → CRUD operations
	•	data_store.py → in-memory list to store students
	•	menu.py → menu display and user interaction

Steps to Install & Run the Project

1. Download or Clone the Repository

You can also download the ZIP and extract it.

2. Open the Folder in VS Code

Just right-click the folder → Open with VS Code.

3. Run the Program

Make sure Python is installed.
Then open the terminal inside VS Code and type:
You will see the menu appear on the screen.

Instructions for Testing

Step 1: Add a few students

Enter marks and check if grades are calculated correctly.

Step 2: View the entire list

Confirm that the students you added are visible.

Step 3: Search for a roll number

Try both valid and invalid roll numbers.

Step 4: Update marks

See whether the updated details appear properly.

Step 5: Delete a student

Check that the record is removed from the list.

Step 6: Restart the program

Notice that data resets (as expected — no file storage).

Why This Project Is Useful
	•	Teachers can manage student marks easily
	•	Students can track their own academic performance
	•	It removes manual calculation mistakes
	•	It’s perfect for learning CRUD, lists, and modular programming

Who Can Use This Project?
	•	School teachers
	•	Students
	•	Coaching centers
	•	Beginners learning Python
	•	Anyone needing a small marking tool

 Future Improvements 
	•	Adding a graphical interface (Tkinter or PyQt)
	•	Generating PDF grade reports
	•	Adding file or database storage
	•	Exporting data to Excel
	•	Adding attendance or multiple subjects