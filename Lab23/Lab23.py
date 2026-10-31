import matops
# a dot product function that takes two vectors as input and returns the dot product as a number
print("The dot product of two vectors: ",matops.dot_product([1, 2, 3], [4, 5, 6]))
print("The dot product of two vectors: ",matops.dot_product([1, 2],[3,4,5]))

#a matrix-vector product that takes a matrix and a vector as input and returns a vector
print(f"\nThe matrix-vector product is: ",matops.matrix_vector([[1, 2], [3, 4]],[5,6]))
print("The matrix-vector product is: ",matops.matrix_vector([[1, 0], [2, 1], [0, 3]],[4, 5]))
print("The matrix-vector product is: ",matops.matrix_vector([[1, 2, 3], [4, 5, 6]],[1, 2]))

#a matrix-matrix product that takes two matrices as input and returns a matrix
print(f"\nThe matrix-matrix product is: ",matops.matrix_matrix([[1, 2], [3, 4]],[[5, 6], [7, 8]]))
print("The matrix-matrix product is: ",matops.matrix_matrix([[1, 2, 3], [4, 5, 6]],[[7, 8], [9, 1], [2, 3]]))
print("The matrix-matrix product is: ",matops.matrix_matrix([[1, 2], [3, 4]],[[1, 2], [3, 4], [5, 6]]))

#a cross product function that takes two vectors and returns the cross product, i.e.,a vector
print(f"\nThe cross product of two vectors: ",matops.cross_product([1, 0, 0],[0,1,0]))
print("The cross product of two vectors: ",matops.cross_product([2, 3, 4],[5, 6, 7]))
print("The cross product of two vectors: ",matops.cross_product([1,2],[3,4]))

from utils import math_utils
#a) 34 and 45
print(f"\nAddition: ",math_utils.add(34,45))
print("Subtraction: ",math_utils.subtract(34,45))
print("Multiplication: ",math_utils.multiply(34,45))
print("Division: ",math_utils.divide(34,45))
print("Remainder: ",math_utils.remainder(34,45))

from utils import string_utils
#b) ’BDBH’ and ’101’
x1="BDBH"
x2="101"
x3="bdbh"
print(f"\nUpper to lower case: ",string_utils.upper_to_lower(x1))
print("Lower to upper case: ",string_utils.lower_to_upper(x3))
print("Concatenated strings: ",string_utils.concatenate(x1,x2))