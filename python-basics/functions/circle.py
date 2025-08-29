import math
def foo(radius):
    area = math.pi * radius**2
    circumference = math.pi * 2 * radius
    return area, circumference

a,c = foo(2)
print(math.trunc(a), math.trunc(c))