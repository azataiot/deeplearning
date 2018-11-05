# for test purpose:
m1=[[1,2],[3,4],[5,6]]
m2=[[3,4],[5,6],[7,8]]
s=[1,2,3]
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
    :param list vector:
    :param list mat:
    :return list:
    """
    for i in range(len(vector)):
        for j in range(shape(mat)[1]):
            mat[i][j]=vector[i]+mat[i][j]
    return mat


def matrixProduct(mat1,mat2):
    """
    Calculates the product of two matrix.
    """
    # check that either the mat1 and mat2 are productable.
    if()