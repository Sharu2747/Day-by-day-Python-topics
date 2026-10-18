
import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="student_db",
    user="postgres",
    password="admin"
)

print("Database connected successfully!")

cur = conn.cursor()

# 1. Insert Arun
cur.execute(
    "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)",
    ("Arun", 22, "Python", 88)
)

conn.commit()

# 2. Retrieve all students
cur.execute("SELECT * FROM students")

students = cur.fetchall()

for student in students:
    print(student)

# 3. Close at the end
cur.close()
conn.close()
