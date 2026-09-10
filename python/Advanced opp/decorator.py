def greet_decorator(func):
    def wrapper():
        print("Starting")
        func()
        print("Finished")
    return wrapper

@greet_decorator
def hello():
    print("Hello")


hello()