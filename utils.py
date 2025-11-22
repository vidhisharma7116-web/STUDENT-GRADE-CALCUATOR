def input_marks():
    marks = {}
    subjects = ["Math", "Science", "English"]
    for s in subjects:
        m = int(input("Enter marks for " + s + ": "))
        marks[s] = m
    return marks
