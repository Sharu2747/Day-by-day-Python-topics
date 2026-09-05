class Student:


   def __init__(self,name,age):
      self.name=name
      self.age=age

   def display(self):
      print(self.name,self.age)

student1=Student("Sharu",23)
student2=Student("Adhav",25)

student1.display()
student2.display()

