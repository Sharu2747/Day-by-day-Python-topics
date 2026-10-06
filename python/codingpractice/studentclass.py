class Student:

  def __init__(self,name,marks):
   self.name=name
   self.marks=marks

  def display(self):
    print("Name:",self.name,"Marks:",self.marks)

student1 = Student("Sharu", 85)
student1.display()