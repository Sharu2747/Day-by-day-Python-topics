student = {
    "name": "Sharu",
    "age": 24,
    "course": "Python"
}

student["marks"]=85
student["age"]=25
del student["marks"]

if "age" in student:
    print("Age exists")

print(student)
print("age" in student)