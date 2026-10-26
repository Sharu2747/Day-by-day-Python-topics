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
#cur.execute(
 #   "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)",
#    ("Arun", 22, "Python", 88)
#)

conn.commit()

# 2. Retrieve all students
cur.execute("SELECT * FROM students WHERE marks<90")

students = cur.fetchall()
print(students)

cur.execute("SELECT * FROM students WHERE name='Sharu'")

students=cur.fetchall()
print(students)

cur.execute("SELECT * FROM students WHERE course='Python' AND marks > 90")

students=cur.fetchall()
print(students)

cur.execute("SELECT * FROM students WHERE marks>90 OR name = 'Arun'")


students=cur.fetchall()
print(students)


cur.execute("SELECT * FROM students ORDER BY marks DESC")


students=cur.fetchall()
print(students)

cur.execute("SELECT * FROM students ORDER BY marks ASC")


students=cur.fetchall()
print(students)

cur.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 2")

students = cur.fetchall()
print(students)

cur.execute("SELECT * FROM students WHERE marks BETWEEN 80 AND 90")

students = cur.fetchall()
print(students)


cur.execute(
    "INSERT INTO students(name,age,course,marks) VALUES (%s, %s, %s, %s) ",
     ("Priya",23,"Python",85)
    )
conn.commit()
print("Inserted Successfully")

cur.execute("SELECT * FROM students WHERE name='Priya'")
students=cur.fetchall()
print(students)

cur.execute("SELECT * FROM students ORDER BY id")


students=cur.fetchall()
print(students)





# 3. Close at the end
cur.close()
conn.close()



