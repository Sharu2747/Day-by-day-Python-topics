def search_student(student_list):
    name = input("Enter student name to search: ")

    found = False

    for student in student_list:
        if name == student["name"]:
            found = True

            print("\nStudent Found")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])

    if not found:
        print("Student not found")

def view_students(student_list):
    if not student_list:
        print("No students found")
    else:
        for index, student in enumerate(student_list, start=1):
            print("\nStudent", index)
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])

def add_student(student_list):
    name = input("Enter student name: ")

    if not name:
        print("Please enter a valid name")
        return

    try:
        age = int(input("Enter student age: "))

        if age < 0 or age > 100:
            raise ValueError

    except ValueError:
        print("Please enter a valid age")
        return

    course = input("Enter course: ")

    try:
        marks = int(input("Enter marks: "))

        if marks < 0 or marks > 100:
            raise ValueError

    except ValueError:
        print("Please enter valid marks")
        return

    student = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    student_list.append(student)

    print("Student added successfully!")

def update_student(student_list):
    name = input("Enter name to update: ")

    found = False

    for student in student_list:
        if name == student["name"]:
            found = True

            new_course = input("Enter new course: ")

            try:
                new_marks = int(input("Enter new marks: "))

                if new_marks < 0 or new_marks > 100:
                    raise ValueError

            except ValueError:
                print("Please enter valid marks")
                return

            student["course"] = new_course
            student["marks"] = new_marks

            print("Updated successfully!")
            return

    if not found:
        print("Student not found")

def update_student(student_list):
    name = input("Enter name to update: ")

    found = False

    for student in student_list:
        if name == student["name"]:
            found = True

            new_course = input("Enter new course: ")

            try:
                new_marks = int(input("Enter new marks: "))

                if new_marks < 0 or new_marks > 100:
                    raise ValueError

            except ValueError:
                print("Please enter valid marks")
                return

            student["course"] = new_course
            student["marks"] = new_marks

            print("Updated successfully!")
            return

    if not found:
        print("Student not found")


def delete_student(student_list):
    name = input("Enter name to delete: ")

    found = False

    for student in student_list:
        if name == student["name"]:
            found = True

            student_list.remove(student)

            print("Student deleted successfully!")
            return

    if not found:
        print("Student not found")