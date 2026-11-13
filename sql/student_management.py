
import psycopg

try:
    conn = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="student_db",
        user="postgres",
        password="admin"
    )

    print("Database connected successfully!")

    cur = conn.cursor()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        # 1. Add Student
        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter age: "))
            course = input("Enter course: ")
            marks = float(input("Enter marks: "))

            cur.execute(
                "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)",
                (name, age, course, marks)
            )
            conn.commit()

            print("Student added successfully!")

        # 2. View All Students
        elif choice == "2":
            cur.execute("SELECT * FROM students")
            students = cur.fetchall()

            if students:
                for student in students:
                    print(student)
            else:
                print("No students found.")

        # 3. Search Student
        elif choice == "3":
            student_id = int(input("Enter student ID: "))

            cur.execute(
                "SELECT * FROM students WHERE id = %s",
                (student_id,)
            )
            student = cur.fetchone()

            if student:
                print(student)
            else:
                print("Student not found.")

        # 4. Update Student
        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            course = input("Enter new course: ")
            marks = float(input("Enter new marks: "))

            cur.execute(
                """UPDATE students
                   SET name = %s, age = %s, course = %s, marks = %s
                   WHERE id = %s""",
                (name, age, course, marks, student_id)
            )
            conn.commit()

            if cur.rowcount > 0:
                print("Student updated successfully!")
            else:
                print("Student not found.")

        # 5. Delete Student
        elif choice == "5":
            student_id = int(input("Enter student ID: "))

            cur.execute(
                "DELETE FROM students WHERE id = %s",
                (student_id,)
            )
            conn.commit()

            if cur.rowcount > 0:
                print("Student deleted successfully!")
            else:
                print("Student not found.")

        # 6. Exit
        elif choice == "6":
            print("Exiting Student Management System...")
            break

        else:
            print("Invalid choice. Please try again.")

except Exception as e:
    print("Error:", e)

finally:
    if "cur" in locals():
        cur.close()

    if "conn" in locals():
        conn.close()

    print("Database connection closed.")
