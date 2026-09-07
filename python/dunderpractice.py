class Person:
  def __init__(self,name,age):
     self.name=name
     self.age=age

class Student(Person):
   def __init__(self, name, age,marks):
      super().__init__(name, age)
      self.marks=marks

   def __str__(self):
      return f"Student Name:{self.name},Age:{self.age},Marks:{self.marks}"

student1=Student("Sharu",23,78)
print(student1)