m1=[[1,2],[3,4],[5,6]]

a=[1,2,3]

for row in m1:
    print(row)
print("*******")

for item in a:
    print(item)
print("*******")


for i in range(len(a)):
    for j in range(len(m1[0])):
        m1[i][j]=a[i]+m1[i][j]

print("新的矩阵\n")
for row in m1:
    print(row)
print("*******")