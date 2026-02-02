def validation(func):
    def wrapper():
        print("validating before the func")
        func()
        print("after validation")
    return wrapper

def myName(func):
    def wrapper():
        print("before calling the func")
        func()
        print("post processing")
    return wrapper

@validation
@myName
def myFunction():
    print("Hey Jack Sally")

myFunction()