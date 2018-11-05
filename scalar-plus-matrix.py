m1=[[1,2],[3,4],[5,6]]

a=5

for row in m1:
    print(row)
print("*******")

for i in range(len(m1)):
    for j in range(len(m1[0])):
        m1[i][j]=a+m1[i][j]

print("新的矩阵\n")
for row in m1:
    print(row)
print("*******")