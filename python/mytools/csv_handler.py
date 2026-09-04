import csv


def export_to_csv(student_list):
    with open("students.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "age", "course", "marks"]
        )

        writer.writeheader()

        for student in student_list:
            writer.writerow(student)

    print("Students exported successfully!")


def import_from_csv(student_list):
    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = {
                    "name": row["name"],
                    "age": int(row["age"]),
                    "course": row["course"],
                    "marks": int(row["marks"])
                }

                student_list.append(student)

        print("Students imported successfully!")

    except FileNotFoundError:
        print("File not found")

    except ValueError:
        print("Invalid data in CSV file")