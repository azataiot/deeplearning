# 1. the direct way
m1=[[1,2],[3,4],[5,6]]
m2=[[3,4],[5,6],[7,8]]
for row in m1:
    print(row)
print("*******")

for row in m2:
    print(row)
print("*******")
row1=len(m1)
row2=len(m2)
colN1=len(m1[0])
colN2=len(m2[0])

for i in range(row1):
    for j in range(colN1):
        m1[i][j]=m1[i][j]+m2[i][j]
for row in m1:
    print(row)

print("利用numpy模块求解。\n")

m1=[[1,2],[3,4],[5,6]]
m2=[[3,4],[5,6],[7,8]]

import numpy as np 
array1=np.array(m1)
array2=np.array(m2)

sum_array=array1+array2
print(sum_array)

print("利用numpy模块的sum()函数进行求解。\n")
m1=[[1,2],[3,4],[5,6]]
m2=[[3,4],[5,6],[7,8]]

import numpy as np 
array1=np.array(m1)
array2=np.array(m2)

new=np.sum([m1,m2],axis=0)

print(new)