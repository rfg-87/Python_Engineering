'''
Exercice 30.

We are going to see the 3D rotations and their characteristics.


Use of library:
- numpy

We are introducing new functions such as:
np.eye()
np.linalg.det()

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


# SOLVED EXAMPLE
print("\n")
print("SOLVED EXAMPLE:")

###### CODE ######

# Angle to rotate
theta_deg = 90.0
theta_rad = np.deg2rad(theta_deg)

# Definition of rotation matrix
c = np.cos(theta_rad)
s = np.sin(theta_rad)

Rx = np.array( [
    [1, 0, 0],
    [0, c, -s],
    [0, s, c]
] )

Ry = np.array( [
    [c, 0, s],
    [0, 1, 0],
    [-s, 0, c]
] )

Rz = np.array( [
    [c, -s, 0],
    [s, c, 0],
    [0, 0, 1]
] )

# Definition of vector
a = np.array( [2, 0, 1] )

# Multiply Rz @ a
a_R = Rz @ a

# Recover original vector
a_R_RT = Rz.T @ a_R

# Norm definition
norm_a = np.linalg.norm(a)
norm_a_R = np.linalg.norm(a_R)

# Check norm and vectors
check_norm_A0 = np.isclose(norm_a, norm_a_R)
check_vectors_A0 = np.allclose(a, a_R_RT)

# Printing results
print(f"The norm of v is: {norm_a:.4f}")
print(f"The norm of rotated v is: {norm_a_R:.4f}")
print(f"Are both normals equal? {check_norm_A0}")
print(f"Are both vectors a and a recovered equal? {check_vectors_A0}")



# YOUR TASK
print("\n")
print("TASK EXAMPLE:")

###### CODE ######

# Printing results
print(f"")
print(f"The expected result is: \n")

print(f"")
print(f"The expected result is: \n")

print(f"")
print(f"The expected result is: \n")

print(f"")
print(f"The expected result is: \n")






# BLOCK B: Engineering problem
#--------------------------------------
print("\n")
print("BLOCK B: Engineering problem:")
print("---------------")

# Printing results
print(f"")
print(f"The expected result is: \n")

print(f"")
print(f"The expected result is: \n")

print(f"")
print(f"The expected result is: \n")

print(f"")
print(f"The expected result is: \n")