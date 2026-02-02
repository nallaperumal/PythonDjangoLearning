def validation(func):
    def wrapper(y):
        print(f"validating before the func: {y}")
        func(y)
        print("after validation")
    return wrapper

def myName(func):
    def wrapper(x):
        print(f"before calling the func with param..{x}")
        upperX = x.upper()
        func(upperX)
        print(f"post processing with param..{x}")
    return wrapper

@validation
@myName
def myFunction(nam):
    print(f"Hey {nam}")

myFunction("udit narayan")