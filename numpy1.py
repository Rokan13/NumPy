import numpy as np

a = np.array([1, 2, 3, 4], dtype='int16')
print("array a",a)
print("dimention",a.ndim) #get dimention
print("type",a.dtype)
print("Shape",a.shape)
print("iteam Size",a.itemsize)
print("total size",a.size) #totalsize
print("byte size",a.nbytes)
b= np.array([[1.2,5.0,6.8],[6.5,8.9,9.0]])
print("array b",b)


print("shape",b.shape) #get shape