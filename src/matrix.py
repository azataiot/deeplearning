# for test purpose:
m1=[[1,2],[3,4],[5,6]]
m2=[[3,4],[5,6],[7,8]]
s=[[1,2,3]]
t=[[3,4,5]]
a=[[1],[2],[3]]

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
        print("You can only calculate the dot product of two vectors which have the same shape.")
    else:
        for i in range(shape(vector1)[0]):
            for j in range(shape(vector2)[1]):
                    dot=vector1[i][j]*vector2[i][j]
    return dot