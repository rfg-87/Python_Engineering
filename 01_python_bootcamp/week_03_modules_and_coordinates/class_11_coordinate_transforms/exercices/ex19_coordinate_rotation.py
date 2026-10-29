'''
In this exercice we are going to introduce the rotation matrix and some functions inside Numpy
such as np.cos() and np.sin().

Python works with radians for the angles, so, if our angles are given in degrees we have to transform
them into radians with a function in Numpy called np.deg2rad().

We are also going to use the matrix product @. Alternatively, we can use the np.dot product

A 2D rotation matrix has the form of:

[
[cos(theta)  -sin(theta)]
[sin(theta)   cos(theta)]
]

'''



############################
#           CODE            
############################


# Import external functions
#---------------------------------------
import numpy as np


# Define Internal Functions
#---------------------------------------
def rotation_matrix_2d_angle(angle_deg):

    theta = np.deg2rad(angle_deg)

    R = np.array([
        [np.cos(theta), - np.sin(theta)],
        [np.sin(theta),   np.cos(theta)]
    ])

    return R


def rotate_2d_vector(vector, angle_deg):

    R = rotation_matrix_2d_angle(angle_deg)

    rotated_vector = R @ vector

    return rotated_vector


def rotation_matrix_over_Z(angle_deg):

    theta = np.deg2rad(angle_deg)

    R_z = np.array([
        [np.cos(theta), - np.sin(theta), 0.0],
        [np.sin(theta),   np.cos(theta), 0.0],
        [0.0,             0.0,           1.0]
    ])

    return R_z




# Main Calculations
#---------------------------------------
# Reference values
A = np.array([100.0, 0.0])
B = np.array([3.0, 4.0])




##################################
# EXERCICE
##################################



# BLOCK A: Convert degrees to radians
#--------------------------------------
print("\n")
print("BLOCK A: Convert degrees to radians:")
print("------------------------------------")

angle_deg = 90.0

angle_rad = np.deg2rad(angle_deg)

print(f'''
    The angle defined {angle_deg:.2f}º in radians is {angle_rad:.2f} rad
''')




# BLOCK B: Create the rotation matrix
#--------------------------------------
print("\n")
print("BLOCK B: Create the rotation matrix:")
print("------------------------------------")

R = rotation_matrix_2d_angle(angle_deg)

print(f'''
    Checking the shape, ndim and determinant of the rotation matrix:
    - Shape: {R.shape}
    - Number of dimensions: {R.ndim}
    - Determinant: {np.linalg.det(R):.2f}
''')




# BLOCK C: Rotate a vector
#--------------------------------------
print("\n")
print("BLOCK C: Rotate a vector:")
print("-------------------------")

vector = np.array([3, 4])

rotated_vector = rotate_2d_vector(vector, angle_deg)

print(f'''
    The rotated vector of {vector} by {angle_deg}º is {rotated_vector}
''')




# BLOCK D: Reference case A
#--------------------------------------
print("\n")
print("BLOCK D: Reference case A:")
print("--------------------------")

vector_A = np.array([100.0, 0.0])

rotated_vector_A = rotate_2d_vector(vector_A, angle_deg)

np.set_printoptions(formatter = {'float': '{:0.1f}'.format})

print(f'''
    The rotated vector of {vector_A} by {angle_deg}º is {rotated_vector_A}
    Note that the 0.0 value when rotated is not 0 exactly as there is some residual factor
    close to 6E-15.

    We can see it if we do not put the set_printoptions to set the format to the print representation.
''')




# BLOCK E: Norm of a vector
#--------------------------------------
print("\n")
print("BLOCK E: Norm of a vector:")
print("--------------------------")

norm_vector_A = np.linalg.norm(vector_A)
norm_vector_A_rotated =np.linalg.norm(rotated_vector_A)

same_norm = np.allclose(norm_vector_A, norm_vector_A_rotated)

print(f'''
    The difference between the norm of the original vector and the rotated vector have the same norm?
    {"SAME NORM" if same_norm else "DIFFERENT NORM"}
''')




# BLOCK F: Inverse transformation
#--------------------------------------
print("\n")
print("BLOCK F: Inverse transformation:")
print("--------------------------------")

R = rotation_matrix_2d_angle(30.0)
vector_B = np.array([3.0, 4.0])

rotated_vector_B = R @ vector_B

# Using the transpose to recover the original vector_B
recover_vector_B = R.T @ rotated_vector_B

np.set_printoptions(formatter = {'float': '{:0.1f}'.format})
print(f'''
    The inverse of a ortogonal rotation matrix matches the transpose of it:
        vector_B = {vector_B}
        rotated_vector_B = {rotated_vector_B}
    If we use the transpose to revert the rotations:
        vector_B = {vector_B}
        recover_vector_B = {recover_vector_B}
    And we can study the difference between the original and recovered vector through np.allclose():
        The difference between vector_B and the recovered vector B is of {"0" if np.allclose(recover_vector_B, vector_B) else np.linalg.norm(recover_vector_B - vector_B)}
''')




# BLOCK G: Consecutive rotations
#--------------------------------------
print("\n")
print("BLOCK G: Consecutive rotations:")
print("-------------------------------")

v1 = rotate_2d_vector(vector_B, 20.0)
v2 = rotate_2d_vector(v1, 40.0)

v3 = rotate_2d_vector(vector_B, 60.0)

print(f'''
    For 2D rotations with the same sign, a first rotation of 20.0º with a second rotation of 40.0º
    is equivalent to a direct rotation of 60.0.
    If we use np.allclose() to have the True/False difference between vectors we obtain that:
    The vectors v2 and v3 are the same?
    {np.allclose(v2, v3)}
''')





# BONUS: 3D rotation over Z axis
#--------------------------------------
print("\n")
print("BONUS: 3D rotation over Z axis:")
print("-------------------------------")

vector_3D = np.array([10.0, 0.0, 5.0])

rotated_vector_3D_over_z = rotation_matrix_over_Z(90.0) @ vector_3D

print(f'''
    The expected output for the vector [10.0, 0.0, 5.0] rotated 90.0 over Z axis is [0.0, 10.0, 5.0]
    and our solution is:
    {rotated_vector_3D_over_z}
    So, the solution matches?
    {np.allclose(rotated_vector_3D_over_z, np.array([0.0, 10.0, 5.0]))}
''')



# FINAL VALIDATION
#-------------------------------------------------
'''
Explain:
- What does np.deg2rad( receive and return?
+ It receives an angle in degrees and transforms it into radians.

- What are the shape and meaning of R in 2D?
+ The shape of 2D rotation matrix is (2, 2). R is the rotation matrix: rotates a vector in the plane.

- Why do we use @ instead of * for R and vector?
+ @ is the matrix-vector product, matrix-matrix product and dot product vector-vector.
+ * is the product element by element between. In this case, matrix element per vector element.

- Why should vector norm remain unchanged after a rotation?
+ Because a rotation matrix is an ortonormal matrix: its norm is equal to 1 so when multiplying, it
does not change the norm of the vector ||v2|| = ||R||·||v1|| = 1·||v1|| = ||v1||.

- What does R.T mean?
+ It is the transposed of the rotation matrix.

- Why can R.T recover the original vector?
+ Because for an ortonormal matrix or ortogonal rotation matrix the inverse of the matrix
is equal to the transposed matrix: R^-1 = R^T.

- Why can a theoretical zero appear as a tiny non-zero float?
+ Because of the internal rounding of floats, there can be slight differences in very far decimals.

- What is the difference between rotating a vector and changing the coordinate frame?
+ In the change of a coordinate frame, we can also suffer translations plus rotationsdifferent
centers of the systems, or even to go from an inertial system to a non-inertial one. When rotating,
we are only applying that change.

+ ACTIVE ROTATION: we rotate the vector, for example, velocity
--> vector physically rotates
--> axes remain fixed

                    v' = R @ v

+ ACTIVE ROTATION / CHANGE OF FRAME
--> physicial vector stays the same
--> coordinate axes change
--> its coordinates therefore change

                    v_new_frame = R^-1 @ v = R^T @ v

'''