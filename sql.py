import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="student_db",
    user="postgres",
    password="admin"

)

print("Database connected successfully")

cur=conn.cursor()

name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
marks = float(input("Enter marks: "))

   
cur.execute(
    "SELECT * FROM students WHERE marks > 80"
)

cur.execute(
    "SELECT * FROM students WHERE course = 'Python'"
)

students = cur.fetchall()

print(students)

cur.close()
conn.close()