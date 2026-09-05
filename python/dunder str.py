class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
      return f"student:Name{self.name}.Age{self.age}"

student1 = Student("Sharu", 25)

print(student1)