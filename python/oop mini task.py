class Vehicle:
   def start(self):
      print("Vehicle starts")

class Car(Vehicle):
   def start(self):
      print("Car starts with key")

car1=Car()
car1.start()
   