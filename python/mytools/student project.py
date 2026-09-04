from file_handler import save_students, load_students
from csv_handler import export_to_csv, import_from_csv
from student import (
    search_student,
    view_students,
    add_student,
    update_student,
    delete_student
)


def main():
    student_list = load_students()

    while True:

        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("7. Export to CSV")
        print("8. Import from CSV")

        choice = input("Enter your choice: ")

        # ADD STUDENT
        if choice == "1":
            add_student(student_list)
            save_students(student_list)

        # VIEW STUDENTS
        elif choice == "2":
            view_students(student_list)

        # SEARCH STUDENT
        elif choice == "3":
            search_student(student_list)

        # UPDATE STUDENT
        elif choice == "4":
            update_student(student_list)
            save_students(student_list)

        # DELETE STUDENT
        elif choice == "5":
            delete_student(student_list)
            save_students(student_list)

        # EXIT
        elif choice == "6":
            print("Goodbye!")
            break

        # EXPORT CSV
        elif choice == "7":
            export_to_csv(student_list)

        # IMPORT CSV
        elif choice == "8":
            import_from_csv(student_list)

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()