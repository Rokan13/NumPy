import numpy as l
a = l.ones((3,4))
print("A",a)
b = l.full((4,3), 2)
print("B",b)
print("Matmul",l.matmul(a,b))

c = l.identity(4)
print("Determine",l.linalg.det(c))