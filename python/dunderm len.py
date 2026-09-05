class Book:
  def __init__(self,name):
    self.name=[1,2,3,4,]

  def __len__(self):
    return len(self.pages)

book1=Book()

print(len(book1))