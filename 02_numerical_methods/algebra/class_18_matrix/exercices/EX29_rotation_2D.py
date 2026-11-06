'''
Exercice 29.

We are going to learn about rotation matrix and how to rotate a vector with its 
peculiarities.

Use of library:
- numpy

Note: Python works with radian angles so we need to transform from degrees to radians 
or to radians to degrees if we want to export them as degrees.

Note2: we have the function np.rad2deg to transform radians to degrees.

Note3: We have the function np.deg2rad to transform degrees to radians.
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

# Definition of angle rotated in degrees and change to radians
theta = 90.0                # [º]
theta = np.deg2rad(theta)   # [rad]

# Definition of matrix and vectors
R = np.array( [
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
] )

v = np.array( [2, 1] )

# Multiplication of Rv
v_R = R @ v

# Norm of the original vector and the rotated
norm_v = np.linalg.norm(v)
norm_v_R = np.linalg.norm(v_R)

# Check that the norms are equal
check_norm = np.isclose(norm_v, norm_v_R)

# Printing results
print(f"The norm of v is: {norm_v:.4f}")
print(f"The norm of rotated v is: {norm_v_R:.4f}")
print(f"Are both normals equal? {check_norm}")




# YOUR TASK A1
print("\n")
print("TASK EXAMPLE:")

###### CODE ######

# Definition of angle
theta_A1 = np.deg2rad(30.0)

# Definition of matrix and vectors
R = np.array( [
    [np.cos(theta_A1), -np.sin(theta_A1)],
    [np.sin(theta_A1), np.cos(theta_A1)]
] )

a = np.array( [4, 0] )

# Calculus of a' = R @ a
a_R = R @ a

# Norms
norm_a = np.linalg.norm(a)
norm_a_R = np.linalg.norm(a_R)

# Check of norms
check_norm_A1 = np.isclose(norm_a, norm_a_R)

# Printing results
print(f"The norm of a is: {norm_a:.4f}")
print(f"The rotated vector a is: {a_R}")
print(f"The norm of rotated a is: {norm_a_R:.4f}")
print(f"Are both normals equal? {check_norm_A1}")




# YOUR TASK A2
print("\n")
print("TASK EXAMPLE:")

###### CODE ######

# Definition of angle
theta_A2 = np.deg2rad(90.0)

# Definition of matrix and vectors
R = np.array( [
    [np.cos(theta_A2), -np.sin(theta_A2)],
    [np.sin(theta_A2), np.cos(theta_A2)]
] )

q = np.array( [3, -2] )

# Calculus of a' = R @ a
q_R = R @ q

# Inverse transformation: q = q_R_RT = R.T @ q_R
q_R_RT = R.T @ q_R

# Check of vectors rotated and come back
check_vectors_A2 = np.allclose(q_R_RT, q)

# Printing results
print(f"The vector q is: {q}")
print(f"The rotated vector q is: {q_R}")
print(f"The vector of rotated q' and rotated by transpose is: {q_R_RT}")
print(f"Are both vectors equal? {check_vectors_A2}")




# YOUR TASK A3
print("\n")
print("TASK EXAMPLE:")

###### CODE ######

# Definition of angle
theta_A3_1 = np.deg2rad(30.0)
theta_A3_2 = np.deg2rad(-60.0)

theta_check = np.deg2rad(-30.0)

# Definition of matrix and vectors
R_1 = np.array( [
    [np.cos(theta_A3_1), -np.sin(theta_A3_1)],
    [np.sin(theta_A3_1), np.cos(theta_A3_1)]
] )

R_2 = np.array( [
    [np.cos(theta_A3_2), -np.sin(theta_A3_2)],
    [np.sin(theta_A3_2), np.cos(theta_A3_2)]
] )

R_check = np.array( [
    [np.cos(theta_check), -np.sin(theta_check)],
    [np.sin(theta_check), np.cos(theta_check)]
] )

p = np.array( [2, 0] )

# Calculus of p_final = R_2 @ R_1 @ p
p_final = R_2 @ R_1 @ p

# Check for rotating -30.0º
p_final_check = R_check @ p

# Norm calculation
norm_p = np.linalg.norm(p)
norm_p_final = np.linalg.norm(p_final)

# Check of vectors rotated and checked angle
check_norm_A3 = np.isclose(norm_p, norm_p_final)
check_vectors_A3 = np.allclose(p_final, p_final_check)

# Printing results
print(f"The vector p_final is: {p_final}")
print(f"The vector p_final rotated directly -30.0º: {p_final_check}")
print(f"Are both vectors equal? {check_vectors_A3}")
print(f"Are the normals of p and p rotated equal? {check_vectors_A3}")






# BLOCK B: Engineering problem
#--------------------------------------
print("\n")
print("BLOCK B: Engineering problem: Rotating a force")
print("-----------------------------------------------")

# Rotating angle
theta_rad = np.deg2rad(30.0)

# Definition of force vector
F = np.array( [10, 0] )

# Definition of rotation matrix
R = np.array( [
    [np.cos(theta_rad), -np.sin(theta_rad)],
    [np.sin(theta_rad), np.cos(theta_rad)]
] )

# Rotated force
F_R = R @ F

# Norm calculation
norm_F = np.linalg.norm(F)
norm_F_R = np.linalg.norm(F_R)

# Check of norms
check_norm_B = np.isclose(norm_F, norm_F_R)

# Printing results
print(f"The norm of F is: {norm_F:.2f} N")
print(f"The norm of rotated F is: {norm_F_R:.2f} N")
print(f"Are both normals equal? {check_norm_B}")
print(f"The rotated F vector is: {F_R} N")






# BLOCK C: Engineering problem
#--------------------------------------
print("\n")
print("BLOCK C: Engineering problem: Reference-frame change")
print("----------------------------------------------------")

'''
Here we are not rotating the vector if not the frame.
'''

# Rotating angle
theta_rad_C = np.deg2rad(90.0)

# Definition of force vector
F_G = np.array( [3, 4] )

# Definition of rotation matrix
R = np.array( [
    [np.cos(theta_rad_C), -np.sin(theta_rad_C)],
    [np.sin(theta_rad_C), np.cos(theta_rad_C)]
] )

# Rotated frame force F_L
F_L = R.T @ F_G

# Recovering original force F_G
F_G_recover = R @ F_L

# Norm definition
norm_F_G = np.linalg.norm(F_G)
norm_F_L = np.linalg.norm(F_L)
norm_F_G_recover = np.linalg.norm(F_G_recover)

# Check of norms and vectors
check_norm_C = np.allclose( [norm_F_L, norm_F_G_recover], norm_F_G)
check_vectors_C = np.allclose(F_G, F_G_recover)

# Printing results
print(f"The norm of F_G is: {norm_F_G:.2f} N")
print(f"The norm of F_L is: {norm_F_L:.2f} N")
print(f"The norm of recovered F_G is: {norm_F_G_recover:.2f} N")
print(f"Are the three normals equal? {check_norm_C}")
print(f"Are the vector F_G and recovered F_G equal? {check_vectors_C}")
print(f"The force components in the local frame are: {F_L}")

'''
3. Compare the norms and explain in one sentence what changed and what did not:
With this rotation:

+ Norm has not changed as the rotation matrix is ortogonal (R.T @ R = I)
+ The vector has switched values between X and Y with negative Y because of the rotation.
To better see it you can do a picture.
'''





'''
Validation checklist

'''
print(f"Shape of rotation matrix: {R.shape}")
print(f"Shape of force vector: {F_G.shape}")

print("An active rotation: the vector is rotating, the frame axis are fixed, change of the physical orientation of the vector.")
print("A passive rotation: the physical vector remains fixed, the reference frame axis change, the vector coordinates used changes.")