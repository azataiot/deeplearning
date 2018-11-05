# 矩阵的转置python实现代码
# matrix transpose python implementation
# 1. using nested list comprehension:

# 通过python列表推导的方法，我们也能轻易完成这个任务
m=[[1,2],[3,4],[5,6]]
for row in m:
    print(row) # print the proginal matrix.
print(m[0][0]) # 这是矩阵的第一个元素。
rowNum=len(m)
print("这个矩阵的行数是"+str(rowNum)) #这是一个三行矩阵

colNum=len(m[0])
print("这个矩阵的列数是"+str(colNum)) # 这是一个两列的矩阵。

rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print(rez)

for row in rez:
    print(row)