# a dot product function that takes two vectors as input and returns the dot product as a number
def dot_product(v1,v2):
    if len(v1)!=len(v2):
        print("Error: Vectors has to be of equal length")
        return None
    result=0
    for i in range(len(v1)):
        result=result+v1[i]*v2[i]
    return result

#a matrix-vector product that takes a matrix and a vector as input and returns a vector
def matrix_vector (matrix,vector):
    if len(matrix[0])!=len(vector):
        print("Error: Matrix column count must match vector length.")
        return None
    result=[]
    for row in matrix:
        row_sum=0
        for i in range(len(vector)):
            row_sum=row_sum+row[i]*vector[i]
        result.append(row_sum)
    return result

#a matrix-matrix product that takes two matrices as input and returns a matrix
def matrix_matrix (matrix_1,matrix_2):
    if  len(matrix_1[0])!=len(matrix_2): #columns in matrix1 must be equal to rows in matrix2
        print("Error: Number of columns in Matrix 1 must equal number of rows in Matrix 2.")
        return None
    result=[[0]*len(matrix_2[0]) for _ in range(len(matrix_1))] #initialize a zero matrix
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_2)):
                result[i][j]+=matrix_1[i][k]*matrix_2[k][j]
    return result

#a cross product function that takes two vectors and returns the cross product, i.e.,a vector
def cross_product(v1,v2):
    if len(v1)!=3 or len(v2)!=3:
        print("Error: Cross product is only defined for 3-dimensional vectors.")
        return None
    result=[]
    for i in range(3):
        next_index=(i+1)%3
        last_index=(i+2)%3
        value=(v1[next_index]*v2[last_index]-v1[last_index]*v2[next_index])
        result.append(value)
    return result