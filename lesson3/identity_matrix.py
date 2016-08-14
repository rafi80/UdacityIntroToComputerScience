# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)

def is_identity_matrix(matrix):
    if not is_sqaure_matrix(matrix):
        return False
    else:
        i = 0
        fault = 0
        while i < len(matrix):
            if is_a_line_of_identity_matrix(matrix[i],i):
                fault += 0
            else:
                fault += 1
            i+=1

    if fault == 0:
        return True
    else:
        return False


def is_sqaure_matrix(matrix):

   number_of_rows = len(matrix)
   lengths_of_elements = []

   for element in matrix:
        lengths_of_elements.append(element)
   for columns_length in lengths_of_elements:
        if len(columns_length) != number_of_rows:
            return False
            break
   return True

def is_a_line_of_identity_matrix(list,index_in_identity):
    i = 0
    fault = 0
    while i<len(list):
        if i < index_in_identity and list[i] != 0:
            fault =1
        elif i > index_in_identity and list[i] != 0:
            fault = 1
        elif i == index_in_identity and list[i]!= 1:
            fault = 1
        i+=1
    if fault == 0:
        return True
    else:
        return False



# Write your code here



# Test Cases:

matrix1 = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]
print is_identity_matrix(matrix1)
# >>>True

matrix2 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]

print is_identity_matrix(matrix2)
# >>>False

matrix3 = [[2, 0, 0],
           [0, 2, 0],
           [0, 0, 2]]

print is_identity_matrix(matrix3)
# >>>False

matrix4 = [[1, 0, 0, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 1]]

print is_identity_matrix(matrix4)
# >>>False

matrix5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

print is_identity_matrix(matrix5)
# >>>False

matrix6 = [[1, 0, 0, 0],
           [0, 1, 0, 1],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]

print is_identity_matrix(matrix6)
# >>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
# >>>False

# print is_sqaure_matrix(matrix1)
# print is_sqaure_matrix(matrix2)
# print is_sqaure_matrix(matrix3)
# print is_sqaure_matrix(matrix4)
# print is_sqaure_matrix(matrix5)
# print is_sqaure_matrix(matrix6)
# print is_sqaure_matrix(matrix7)

list1 = [1,0,0]
list2 = [0,1,0]
list3 = [0,0,0,0,0,1]
list100 = [0,0,0,0,0,0,0,1,-1]
list101 = [0,2,0,0,0,0,0,1,0]
listC = [1, -1, 1]

# print is_a_line_of_identity_matrix(list1,0)
# # >>> True
# print is_a_line_of_identity_matrix(list2,1)
# # >>> True
# print is_a_line_of_identity_matrix(list3,5)
# # >>> True
# print is_a_line_of_identity_matrix(list100,7)
# # >>> False
# print is_a_line_of_identity_matrix(list101,7)
# # >>> False

