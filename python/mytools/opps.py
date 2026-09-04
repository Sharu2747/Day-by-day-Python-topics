from abc import ABC, abstractmethod

class Animal(ABC):
  @ abstractmethod
  def sound(self):
    pass

class Dog(Animal):
    def sound(self):
      print("Barks")

dog1 = Dog()
dog1.sound()
