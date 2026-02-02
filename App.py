import inspect
class Vehicle:
    def __init__(self, wheels, color = "white"):
        self.wheels = wheels
        self.color = color
    def recolor(self, color):
        self.color = color
v = Vehicle("4", "red")
# print(v.color)
# print(dir(v))
# print(callable(v.recolor))
print(inspect.signature(v.recolor))
print(v.__dict__)
