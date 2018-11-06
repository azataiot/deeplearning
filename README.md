---
title: 线性代数|神经网络6周挑战
key: week1mon1
tags: 
 - 中文
 - AI
 - 深度学习
 - 人工智能
 - 机器学习
 - 线性代数
toc: true
mathjax: true
mathjax_autoNumber: true
---

![1200px-Linear_subspaces_with_shading](https://ws2.sinaimg.cn/large/006tNbRwgy1fwx3d4cu05j30rs06t3zq.jpg)

Week 1. Monday.线性代数+概率论与信息论<!--more--> 

# 线性代数

## 整体框架与思维导图

![线性代数](https://ws4.sinaimg.cn/large/006tNbRwgy1fwx3lqumgfj312i0s2427.jpg)

## 标量、向量、矩阵和张量

## ![image-20181105113036844](https://ws2.sinaimg.cn/large/006tNbRwgy1fwx4i6fmokj31kw169k4x.jpg)

### Python 代码

#### transpose

* **Using Nested List Comprehension:**

通过python列表推导的方法，我们也能轻易完成这个任务

``` python
# 矩阵的转置python实现代码
# matrix transpose python implementation
# 1. using nested list comprehension:

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
```

* **Using zip:**

定义：zip([iterable, ...])

zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。利用*号操作符，可以将list unzip（解压），看下面的例子就明白了：

``` python
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)
[(1, 2, 3), (4, 5, 6)]
```

我们的矩阵转换就可以这么来：

``` python 
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
```

* **Using Numpy**

``` python
import numpy as np

m=[[1,2],[3,4],[5,6]]

for row in m:
    print(row)
# You need to install numpy in order to import it 
# Numpy transpose returns similar result when  
# applied on 1D matrix 
matrix=[[1,2,3],[4,5,6]] 
print(matrix) 
print("\n") 
print(np.transpose(matrix)) 
```

#### 矩阵相加

备注，两个list 简单的相加是一个 append 的过程，也就是把两个list 拼接到一起，而不是对应元素相加。

``` python
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
```

* **利用numpy模块求解。**

``` python
print("利用numpy模块求解。\n")

m1=[[1,2],[3,4],[5,6]]
m2=[[3,4],[5,6],[7,8]]

import numpy as np 
array1=np.array(m1)
array2=np.array(m2)

sum_array=array1+array2
print(sum_array)
```

* **利用numpy模块的sum()函数进行求解。**

``` python
print("利用numpy模块的sum()函数进行求解。\n")
m1=[[1,2],[3,4],[5,6]]
m2=[[3,4],[5,6],[7,8]]

import numpy as np 
array1=np.array(m1)
array2=np.array(m2)

new=np.sum([m1,m2],axis=0)

print(new)
```

#### 标量与矩阵相乘

``` python
m1=[[1,2],[3,4],[5,6]]

a=5

for row in m1:
    print(row)
print("*******")

for i in range(len(m1)):
    for j in range(len(m1[0])):
        m1[i][j]=a*m1[i][j]

print("新的矩阵\n")
for row in m1:
    print(row)
print("*******")
```

#### 标量与矩阵相加

``` python
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
```

#### 广播（broadcasting）

``` python
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
```

##  矩阵和向量相乘

![image-20181105151341773](https://ws1.sinaimg.cn/large/006tNbRwgy1fwxay8k8ptj31fi1j2123.jpg)

### Python 实现

#### matrix product

 python 实现:

``` python
# 数学公式在python 中的实现的时候，注意数学公式，按照公式把公式内容写出来就可以了。

# 首先，注意公式中的每一个变量的意义，比如说， C 是我们的product 最后的矩阵，而i 是C 的行，j 是C的列。

# C 总共有 A的行数 个行和 B 的列数个 列。 也就是乘是取第一个矩阵的行，第二个矩阵的列数。
def matrixProduct(mat1,mat2):
    if(shape(mat1)[1]!=shape(mat2)[0]): #首先判断一下这两个矩阵是不是可以相乘的（check whether those two matrices are cable of product.
        print(""" To calculate the matrix product, the first matrix row numbers should be
        equal to the secound matrix column number.""")
    else:
        trans_mat1=matTranspose(mat1)
        matrix=[[0 for i in range(shape(mat1)[0])] for i in range(shape(mat2)[1])]
        row_matrix=len(matrix)
        col_matrix=len(matrix[0])
        for i in range(shape(mat1)[0]):
            for j in range(shape(mat2)[1]):
                for k in range(shape(mat2)[0]):
                    matrix[i][j] +=mat1[i][k]*mat2[k][j]
    return matrix
```

![image-20181106104149716](https://ws2.sinaimg.cn/large/006tNbRwgy1fwy8psptf0j30ag03y3yj.jpg)

数学公式在python 中的实现的时候，注意数学公式，按照公式把公式内容写出来就可以了。

首先，注意公式中的每一个变量的意义，比如说， C 是我们的product 最后的矩阵，而i 是C 的行，j 是C的列。

C 总共有 A的行数 个行和 B 的列数个 列。 也就是成绩是取第一个矩阵的行，第二个矩阵的列数。

#### **Hadamard Product**

![image-20181106121419109](https://ws3.sinaimg.cn/large/006tNbRwgy1fwybdve8awj304401ea9y.jpg)

``` python

def hadamardProduct(mat1,mat2):
    """
    HadamardProduct is the product of two matrix elements that placed in the same index.
    元素对应乘积(element-wise product)或 者 Hadamard 乘积(Hadamard product)
    是两个矩阵对应元素的成绩
    """
    if(shape(mat1)!=shape(mat2)):
        print("""To calculate the Hadamard Product of two matrix, they should have the same shape!
        For example, matrix A with 3 row 3 col and matrix B with 3 row 3 col can be processed for calculating
        the Hadamard Product while A can't with a matrix C have 3 row and 4 col ! """)
    else:
        [row,col]=shape(mat1)
        result_matrix=[[0 for i in range(shape(mat1)[1])] for j in range(shape(mat1)[0])]
        for i in range(shape(mat1)[0]):
            for j in range(shape(mat1)[1]):
                result_matrix[i][j]= mat1[i][j]* mat2[i][j]
        return result_matrix
```

## 单位矩阵和逆矩阵



## 线性相关和生成子空间

## 范数

## 特殊类型的矩阵和向量

## 特征分解

## 奇异之分解

## Moore-Penrose 伪逆

## 迹运算

## 行列式

## 实例：主成分分析

# 概率论与信息论





