'''
Exercice 28.

We are going to operate with matrix and see some of its properties.

Use of library:
- numpy

'''

############################
#           CODE            
############################


# Import external functions
#---------------------------------------
import numpy as np


# Define Internal Functions
#---------------------------------------





# Main Calculations
#---------------------------------------





##################################
# EXERCICE
##################################



# BLOCK A: Fully solved algebra example
#--------------------------------------
print("\n")
print("BLOCK A: Fully solved and task algebra example")
print("-------------------------------------------------")


# SOLVED EXAMPLE A0
print("\n")
print("SOLVED EXAMPLE:")

###### CODE ######

# Definition of matrix and vector
A = np.array( [
    [1, 2],
    [3, 4]
] )

x = np.array( [2, -1] )

# Transpose of the matrix A
A_T = A.T

# Multiply the vector by the matrix using @
Ax = A @ x

# Printing results
print(f"""The transpose of the matrix is:  
{A_T} """)
print(f"The result of the multiplication Ax is: {Ax}")
print(f"The shape of the matrix A is: {A.shape}")
print(f"The shape of the vector x is: {x.shape}")
print(f"The shape of the multiplied result is: {Ax.shape}")




# YOUR TASK A1
print("\n")
print("TASK EXAMPLE:")

###### CODE ######

# Definition of matrix and vector
C = np.array( [
    [2, -1],
    [0, 3]
] )

D = np.array( [
    [1, 4],
    [-2, 2]
] )

x = np.array( [3, 2] )

# Calculate C+D and Transpose of the matrix C
C_plus_D = C + D
C_T = C.T

# Calculate Cx using @
Cx = C @ x

# Calculate CD and DC comparing results
CD = C @ D
DC = D @ C

# Calculate component by component multiplication
component_CD = C * D

# Printing results
print(f"""The sum of the matrix C and D is:  
{C_plus_D} """)
print(f"""The transpose of the matrix C is:  
{C_T} """)
print(f"The result of the multiplication Cx is: {Cx}")
print(f"""The multiplication of the matrix C and D is:  
{CD} """)
print(f"""The multiplication of the matrix D and C is:  
{DC} """)
print(f"""The multiplication component by component of the matrix C and D is:  
{component_CD} """)







# BLOCK B: Engineering problem
#--------------------------------------
print("\n")
print("BLOCK B: Engineering problem: Resultant of known forces")
print("--------------------------------------------------------")

# Definition of the unitary vectors of the actuators
e1 = np.array( [0.6, 0.8] )
e2 = np.array( [-0.8, 0.6] )

# Definition of the actuators matrix A
A = np.column_stack( [e1, e2] )             # column_stack() to put the arrays as 

# Definition of the magnitude vectors for actuator 1 10N and actuator 2 5N
u = np.array( [10, 5] )

# Calculate the resultant R: R = Au
R = A @ u

# Calculation of 10e_1 + 5e_2 and compare with A @ u
check_R = 10 * e1 + 5 * e2

comparison = np.allclose(R, check_R)         # For comparing all the elements at once

# Norm of the Resultant
norm_R = np.linalg.norm(R)

# Printing results
print(f"The resultant vector R is: {R} N")
print(f"Are the two operations equivalent? {comparison}")
print(f"The norm of the resultant is: {norm_R}")

'''
Interpret the rows, columns and physical units of A, u and R:

+ units of A: no units.
+ units of u: [N].
+ units of R: [N].

+ columns of A are each of the actuators.
+ rows of u are the magnitudes for each actuator.
+ rows of R are the magnitudes in each direction of the resultant: Rx and Ry.
'''
