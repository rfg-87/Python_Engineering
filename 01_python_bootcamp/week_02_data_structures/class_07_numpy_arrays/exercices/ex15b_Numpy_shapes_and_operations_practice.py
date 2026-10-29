'''
The main goal of this exercice is to get more comfortable with the numpy and np.array matrix
operations and analysis.

It is linked to the PDF:

"Python_Engineering_Class07_NumPy_EX15b_Shapes_Operations_ES.pdf"
"Python_Engineering_Class07_NumPy_EX15b_Shapes_Operations_EN.pdf"

Where we have the instructions

'''

# Import external functions
#--------------------------------------
import numpy as np


# Array creation
#--------------------------------------
vector_a = np.array( [1.0, 2.0, 3.0] )
vector_b = np.array( [4.0, 5.0, 6.0] )

matrix_a = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
])

matrix_b = np.array([
    [10.0, 20.0, 30.0],
    [40.0, 50.0, 60.0]
])


# BLOCK A: GEOMETRY INSPECTION
#--------------------------------------
print("\n")
print("BLOCK A: GEOMETRY INSPECTION:")
print("-----------------------------")

# Shape --> Gives (row, col) shape: for vectors, only (col, )
print(f"vector_a shape: {vector_a.shape}")      # Predicted: (3,)
print(f"vector_b shape: {vector_b.shape}")      # Predicted: (3,)
print(f"matrix_a shape: {matrix_a.shape}")      # Predicted: (2,3)
print(f"matrix_b shape: {matrix_b.shape}")      # Predicted: (2,3)
print("\n")

# Dimension --> Gives the n dimensions of rows
print(f"vector_a dimension: {vector_a.ndim}")   # Predicted: 1
print(f"vector_b dimension: {vector_b.ndim}")   # Predicted: 1
print(f"matrix_a dimension: {matrix_a.ndim}")   # Predicted: 2
print(f"matrix_b dimension: {matrix_b.ndim}")   # Predicted: 2
print("\n")

# Size --> Gives the amount of elements inside
print(f"vector_a size: {vector_a.size}")        # Predicted: 3
print(f"vector_b size: {vector_b.size}")        # Predicted: 3
print(f"matrix_a size: {matrix_a.size}")        # Predicted: 6
print(f"matrix_b size: {matrix_b.size}")        # Predicted: 6
print("\n")

# Type --> Gives the type of the elements inside
print(f"vector_a type: {vector_a.dtype}")       # Predicted: float64
print(f"vector_b type: {vector_b.dtype}")       # Predicted: float64
print(f"matrix_a type: {matrix_a.dtype}")       # Predicted: float64
print(f"matrix_b type: {matrix_b.dtype}")       # Predicted: float64
print("\n")




# BLOCK B: INDEXING & SLICING
#--------------------------------------
print("\n")
print("BLOCK B: INDEXING & SLICING:")
print("----------------------------")

print(f"matrix_a element (0, 0): {matrix_a[0, 0]}   |   Shape: {matrix_a[0, 0].shape}") # Predicted: 1.0 | ( )
print(f"matrix_a element (1, 2): {matrix_a[1, 2]}   |   Shape: {matrix_a[1, 2].shape}") # Predicted: 6.0 | ( )
print("\n")

print(f"matrix_a all col of row 0: {matrix_a[0, :]} |   Shape: {matrix_a[0, :].shape}") # Predicted: [1.0, 2.0, 3.0] | (3, )
print(f"matrix_a all row of col 1: {matrix_a[:, 1]} |   Shape: {matrix_a[:, 1].shape}") # Predicted: [2.0, 5.0] | (2, )
print(f"matrix_a all col last row: {matrix_a[-1, :]}    |   Shape: {matrix_a[-1, :].shape}") # Predicted: [4.0, 5.0, 6.0] | (3, )
print("\n")

print(f"matrix_a all row from first col: {matrix_a[:, 1:]}  |   Shape: {matrix_a[:, 1:].shape}") # Predicted: [[2.0, 3.0], [5.0, 6.0]] | Shape: (2, 2)
print("\n")

print(f"matrix_a[0, 0] type: {type(matrix_a[0, 0])}")
print(f"matrix_a[0, :] type: {type(matrix_a[0, :])}")   # If only rows or cols are sliced it returns a np.array in a vector form
print(f"matrix_a[:, 1:] type: {type(matrix_a[:, 1:])}")
print("\n")




# BLOCK C: ELEMENT BY ELEMENT OPERATIONS
#--------------------------------------
print("\n")
print("BLOCK C: ELEMENT BY ELEMENT OPERATIONS:")
print("---------------------------------------")

print(f"vector_a + vector_b: {vector_a + vector_b}")    # Predicted: [5.0, 7.0, 9.0]
print(f"vector_a - vector_b: {vector_a - vector_b}")    # Predicted: [-3.0, -3.0, -3.0]
print(f"vector_a * vector_b: {vector_a * vector_b}")    # Predicted: [4.0, 10.0, 18.0]
print(f"vector_a / vector_b: {vector_a / vector_b}")    # Predicted: [0.25, 0.40, 0.50]
print(f"vector_a**2: {vector_a**2}")                    # Predicted: [1.0, 4.0, 9.0]
print("\n")

print(f"matrix_a + matrix_b: {matrix_a + matrix_b}")    # Predicted: [[11.0, 22.0, 33.0], [44.0, 55.0, 66.0]]
print(f"matrix_a * matrix_b: {matrix_a * matrix_b}")    # Predicted: [[10.0, 40.0, 90.0], [160.0, 250.0, 360.0]]
print(f"matrix_a * 10: {matrix_a * 10}")                # Predicted: [[10.0, 20.0, 30.0], [40.0, 50.0, 60.0]]
print("\n")




# BLOCK D: BROADCASTING
#--------------------------------------
print("\n")
print("BLOCK D: BROADCASTING:")
print("----------------------")

# Broadcasting: apply a vector shape (3, ) to every row in matrix (2, 3), for example, a sum.
offset = np.array( [100.0, 200.0, 300.0] )  # Shape: (3, )

result = matrix_a + offset                  # Predicted: [[101.0, 202.0, 303.0, 104.0, 205.0, 306.0], [4.0, 5.0, 6.0, 100.0, 200.0, 300.0]]
print(f"Broadcasting of matrix_a with offser: {result}")
print("\n")


bad_offset = np.array([10.0, 20.0])
# print(f"matrix_a + bad_offset not possible: {matrix_a + bad_offset}")
#                               |
#                               |
#                               V
# The reason why we could not operate with shapes (2, 3) and (2,) is because the operand is applied to positions 0 and 1 but not 2
# as there is not number defined so Python does not know what to add/substract/etc.




# BLOCK E: RESHAPE & TRANSPOSE
#--------------------------------------
print("\n")
print("BLOCK E: RESHAPE & TRANSPOSE:")
print("-----------------------------")

row = vector_a.reshape(1, 3)
column = vector_a.reshape(3, 1)

matrix_a_T = matrix_a.T

print(f"vector_a reshaped as a row: {row}   |   Shape: {row.shape}")            # Prediction: [[1.0, 2.0, 3.0]] | (1, 3)
print(f"vector_a reshaped as a column: {column} |   Shape: {column.shape}")     # Prediction: [[1.0], [2.0], [3.0]] | (3, 1)
print("\n")

print(f"matrix_a transposed: {matrix_a_T}   |   Shape: {matrix_a_T.shape}")     # Prediction: [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]] | (3, 2)
print("\n")

# The reshape converts the array 1D into an array 2D and changes its shape (3, ) -> (1, 3).
# The .T transposes a matrix re-arranging rows to colums and vice-versa




# BLOCK F: CONCATENATE
#--------------------------------------
print("\n")
print("BLOCK F: CONCATENATE:")
print("---------------------")

# vstack to concatenate: columns must match
new_row = np.array([ [7.0, 8.0, 9.0] ])
matrix_rows = np.vstack( (matrix_a, new_row) )
print(f"Added row to matrix_a: {matrix_rows}    |   Shape: {matrix_rows.shape}")        # Prediction: [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]] | (3, 3)

# hstack to concatenate: rows must match
new_column = np.array([ [10.0], [20.0] ])
matrix_columns = np.hstack( (matrix_a, new_column) )
print(f"Added column to matrix_a: {matrix_columns}  |   Shape: {matrix_columns.shape}") # Prediction: [[1.0, 2.0, 3.0, 10.0], [4.0, 5.0, 6.0, 20.0]] | (2, 4)
print("\n")




# BLOCK G: MAX PER AXIS
#--------------------------------------
print("\n")
print("BLOCK G: MAX PER AXIS:")
print("----------------------")

# Maximum values
print(f"The maximum value on matrix_b is: {np.max(matrix_b)}")                      # Prediction: 60.0
print(f"The maximum value on matrix_b on colums, columns values: {np.max(matrix_b, axis = 0)}")  # Prediction: [40.0, 50.0, 60.0]
print(f"The maximum value on matrix_b on rows, rows values: {np.max(matrix_b, axis = 1)}")  # Prediction: [30.0, 60.0]
print("\n")

# Argument (Position) of the maximum
print(f"The position of the maximum in matrix_b is: {np.argmax(matrix_b)}")                     # Prediction: 5
print(f"The position of the maximum in matrix_b on colums with fixed row, row number for each number: {np.argmax(matrix_b, axis = 0)}")  # Prediction: 2
print(f"The position of the maximum in matrix_b on rows with fixed colums, column number for each number: {np.argmax(matrix_b, axis = 1)}")  # Prediciton: 2
print("\n")

# The np.max with axis = 0 is giving a list of the maximum values of all columns.
# The np.max with axis = 1 is giving a list of the maximum values of all rows.

# The np.argmax with axis = 0 is giving a list of the position where the maximums are for all columns.
# The np.argmax with axis = 1 is giving a list of the position where the maximums are for all rows.




# BONUS: DOT/CROSS PRODUCT AND MATRIX-VECTOR PRODUCT
#---------------------------------------------------
print("\n")
print("BONUS: DOT/CROSS PRODUCT AND MATRIX-VECTOR PRODUCT:")
print("---------------------------------------------------")

# Dot Product
dot_product = vector_a @ vector_b
dot_product_2 = np.dot(vector_a, vector_b)

# Cross Product
cross_product = np.cross(vector_a, vector_b)

# Matrix-Vector product
matrix_vector = matrix_a @ vector_b
matrix_vector_2 = np.dot(matrix_a, vector_b)


print(f"The dot product of vector_a and vector_b is: {dot_product} and using np.dot: {dot_product_2}")
print(f"the cross product of vector_a and vector_b using np.cross is: {cross_product}")
print(f"The dot product of matrix_a and vector_b is: {matrix_vector} and using np.dot: {matrix_vector_2}")
print("\n")




# FINAL VALIDATION
#-------------------------------------------------
'''
Check and explain:
- Why (3, ) is not the same as (1, 3)?
+ (3, ) is a 1D array with 3 elements and (1, 3) is a 2D array (1 row and 3 columns)

- Why (2, 3) + (3, ) works?
+ Because we are doing an offset or broadcasting and the quantity of elements match (3 and 3).
+ Broadcasting compares from right to left and they match as there is no other dimension in (3, )
+ Two dimensions are compatible if they are equal or one of them is equal to 1 (-)

- Why (2, 3) + (2, ) fails?
+ Because when doing an offset or broadcasting we are not sum the same number of elements (1 missing and unknown)

- Why vstack needs the same number of columns?
+ Because if not there will be missing elements to add (unknown for system) or too much for an unknown dimension

- Why hstack needs the same number of rows?
+ Because if not there will be missing elements to add (unknown for system) or too much for an unknown dimension

- Difference between * and @
+ The * is a multiplication element by element and @ is the dot product

- Difference between axis = 0 and axis = 1
+ axis indicates the dimension of Numpy deletes/runs to make the operation.
    + When axis = 0: eliminates the dimension of rows (2, 3) -> (3, ) that is why is a by column result.
    + When axis = 1: eliminates the dimension of columns (2, 3) -> (2, ) that is why is a by row result.
+ axis = 0 is meant to give the value of the columns
+ axis = 1 is meant to give the value of the rows

'''
