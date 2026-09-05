class Person:
 
  def __init__(self,name):
    self.name=name

class Student(Person):
  def __init__(self, name,marks):
    super().__init__(name)
    self.marks=marks


student1=Student("Sharu",78)



print(student1.name)
print(student1.marks)