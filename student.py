class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks  # dictionary: {"Math": 90, "Science": 85}

    def display(self):
        print("Roll Number:", self.roll)
        print("Name:", self.name)
        print("Marks:", self.marks)