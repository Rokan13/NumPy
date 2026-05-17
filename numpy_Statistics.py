import numpy as s
st = s.array([[1,2,3,4],[5,6,7,8]])
print(st)
print(s.sum(st))
print(s.sum(st,axis=0))
print(s.sum(st,axis=1))
print(s.min(st,axis=1))
print(s.max(st,axis=1))
