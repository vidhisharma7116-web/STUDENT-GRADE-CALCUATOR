def calculate_total(marks):
    total = 0
    for m in marks.values():
        total += m
    return total


def calculate_percentage(marks):
    total = calculate_total(marks)
    percentage = (total / (len(marks) * 100)) * 100
    return percentage


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    if percentage >= 75:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 40:
        return "D"
    return "F"