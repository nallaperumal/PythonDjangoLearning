import sys
x = 123456789
y = 123456789
z = 123456789
print(sys.getrefcount(x))
z = None
print(sys.getrefcount(x))
y = None
print(sys.getrefcount(x))