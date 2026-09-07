class Book:
  def __init__(self,title,author):
    self.title=title
    self.author=author

  def __str__(self):
    return f"title:{self.title},author{self.author}"

book1 = Book("python Basics","Sharu")
print(book1)