class Book:
  def __init__(self,name):
    self.name=name

  def __eq__(self,other):
    return self.name == other.name
  

book1=Book("Python")
book2=Book("Python")

print(book1==book2)

