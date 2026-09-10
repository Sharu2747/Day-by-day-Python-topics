def greet_decorator(func):
   def wrapper(*args):
      print("Starting")
      func(*args)
      print("Finished")
   return wrapper


@ greet_decorator
def hello(name):
  print("Hello",name)

hello("Sharu")