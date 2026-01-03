class Test:
    # @staticmethod without this decorater 
    # Test.hello() takes 0 positional arguments but 1 was given error arises
    # t.hello()  →  Test.hello(t)
    # But your function expects 0 arguments, so it crashes.
    def hello():
        print("Hi")
t=Test()
t.hello()