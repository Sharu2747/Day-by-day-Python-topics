def greet_decorator(func):
    def wrapper(**kwargs):
        print("Started")
        func(**kwargs)
        print("finished")
    return wrapper

@ greet_decorator
def hello(name,age):
    print("hello",name,age)

hello(name="sharu",age=24)