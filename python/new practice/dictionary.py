students = {
    "Arun": 85,
    "Priya": 92,
    "Kumar": 78,
    "Sharu": 95
}


def display_students():
    for student, marks in students.items():
        print(student, ":", marks)


def calculating_average():
    total = 0

    for student, marks in students.items():
        total += marks

    average = total / len(students)
    print("Average marks:", average)


display_students()
calculating_average()