import numpy as r
before = r.array([[1.,2,3,4],[5,6,7,8]])
print(before.shape)
print(before)

after = before.reshape((2,2,2)) #2,3 now work
print(after)


