class Mobile:
  category="Electronics"



  def __init__(self,brand,price):
    self.brand=brand
    self.__price= price

  def get_price(self):
    return self.__price

  def set_price(self,price):
     self.__price=price


mobile1=Mobile("Samsung",60000)
mobile2=Mobile("Apple",79999)

mobile1.set_price(65000)

print(mobile1.get_price())