import numpy as np
class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

ans = np.ones((5,5)) # 5 row 5 col
ans[2,1] = 5 #row,col,number
print(ans)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

ans[1:-1,1:-1] = z
print(ans)