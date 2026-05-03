def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

def say_hello():
    print("Hello")
# say_hello()
@decorator
def say_hello():
    print("Hello")
say_hello()