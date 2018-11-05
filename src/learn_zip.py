a=[1,2]
b=[3,4]
c=[5,6]
# zip
# 它接受一系列可迭代的对象作为参数，
# 将对象中对应的元素打包成一个个tuple（元组），
# 然后返回由这些tuples组成的list（列表）
# 若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。

# zip 是把对象中的对应元素打包成一个个的tuple 然后返回这些tuple 的list。

m=[[1,2],[3,4],[5,6]]

for row in m:
    print(row)
transposed_m=list(zip(*m))

for row in transposed_m:
    print(row)