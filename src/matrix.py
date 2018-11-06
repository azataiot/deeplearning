# for test purpose:
m1=[[1,2],[3,4],[5,6]]
m2=[[3,4],[5,6],[7,8]]
s=[[1,2,3]]
t=[[3,4,5]]
a=[[1],[2],[3]]
b=[[3],[4],[5]]

## vectors and scales above works just for a test purpose.


def indentifyVector(vector):
    """
    Differ vector beetween a row vector and a coloumn vector. 
    Returns 1 if the vector is a row vector and returns 0 if the cvector is a coloumn vector.
    """
    if(len(vector)==1):
        return 1
    else:
        return 0


def shape(matrix):
    """
    returns a list containing two value, first value of the list is
    the number of rows of the matrix, and the second one if the columns of 
    the matrix.
    :param list matrix: input is a matrix orginazed as a python list.
    :retuen list:
    """
    rowNO=len(matrix)
    colNO=len(matrix[0])
    return rowNO,colNO


def matsum(mat1,mat2):
    """
    Adds two matrix and returns the sum. the shape of the two matrix should be the same.
    :param list mat1:
    :param list mat2:
    return list:
    """
    shape1=shape(mat1)
    shape2=shape(mat2)
    for i in range(shape1[0]):
        for j in range(shape2[1]):
            mat1[i][j]=mat1[i][j]+mat2[i][j]
    return mat1


def scaMatPro(scale,mat):
    """
    calculates the result of scale and mat product.
    :param int scale:
    :param list mat:
    :return list:
    """
    for i in range(shape(mat)[0]):
        for j in range(shape(mat)[1]):
            mat[i][j]=scale*mat[i][j]
            return mat



def scaMatSum(scale,mat):
    """
    calculates the result of scale plus mat.
    :param int scale:
    :param list mat:
    :return list:
    """
    for i in range(shape(mat)[0]):
        for j in range(shape(mat)[1]):
            mat[i][j]=scale+mat[i][j]
            return mat 


def broadcast(vector,mat):
    """
    Calculates the Broadcasting operation of one vector and one matrix.
    :param list vector: You should enter a vector transpose.
    :param list mat:
    :return list:
    """
    if(indentifyVector(vector)==1):
        print("You should enter a column vector to do the broadcasting operation.")
    else:
        for i in range(len(vector)):
            for j in range(shape(mat)[1]):
                mat[i][j]=vector[i][0]+mat[i][j]
    return mat

def matTranspose(mat):
    """
    Calculate the transpose of a matrix.
    """
    for row in mat:
        transposed_m=list(zip(*mat))
        return transposed_m

def vectorTranspose(vector):
    """
    Calculate the transpose of a vector.
    """
    m=vector
    # if(indentifyVector(m)==0):
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return rez


def vectorDotPro(vector1,vector2):
    """
    Calculate the dot product of two vectors.
    """
    dot=0
    if(shape(vector1)!=shape(vector2)):
        vector1=vectorTranspose(vector1)
        for i in range(shape(vector1)[0]):
            for j in range(shape(vector2)[1]):
                    dot=vector1[i][j]*vector2[i][j]
    else:
        for i in range(shape(vector1)[0]):
            for j in range(shape(vector2)[1]):
                    dot=vector1[i][j]*vector2[i][j]
    return dot



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
