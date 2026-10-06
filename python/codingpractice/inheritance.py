class Animal:
  def sound(self):
    print("Animal makes sound")

class Dog(Animal):
  def sound(self):
    print("Dog barks")


dog1 = Dog()
dog1.sound()