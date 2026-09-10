def greet_decorator(func):
    def wrapper(*args, **kwargs):
        print("Starting")
        func(*args, **kwargs)
        print("finished")
    return wrapper

@greet_decorator
def hello(name, age):
    print("Hello", name, age)

hello("Sharu", 24)