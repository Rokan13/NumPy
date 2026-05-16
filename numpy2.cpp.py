import numpy as n
a = n.array([[1,2,3],[4,5,6],[7,8,9]])
print("array a",a)

print(a[1,2]) #specific element[r,c]
print(a[2,2])

print(a[0,:]) #row
print(a[:,2]) #col

a[1,2]=10
print(a)

b = n.array([[1,2,3],[4,5,6],[7,8,9]])
print("array b",b)
print(b[1,2])
print(b[2,2])
print(b[0,:])
print(b[:,2])

print("any other number")
print(n.full_like(a,4))
print(n.full_like(a,5))
print(n.full_like(a,6))

print("Decimal Number")
print(n.random.rand(4,2))

print("Integer value")
print(n.random.randint(-4,8,size=(3,4)))

print("identity matrix")
print(n.identity(5))

print("repeat a array")
arr = n.array([[1,2,3]])
r1 = n.repeat(arr,3,axis=0)
print(r1)

