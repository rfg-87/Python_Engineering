'''
Exercice 26.

We are going to operate with the dot product and the angle between vectors
applying what we have seen in EX25.

Note: We are not going to consider special cases such as norm of a vector
equal to zero. We will do it in the future, thisi is just to understand how
to proceed

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


# SOLVED EXAMPLE
print("\n")
print("SOLVED EXAMPLE:")

# Definition of vectors
u = np.array( [2, 1] )
v = np.array( [1, 3] )

# Dot product
uv = np.dot(u, v)

# Norm of vectors
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

# Angle between vectors
numerator = uv
denominator = norm_u * norm_v

cos_theta = ( numerator / denominator )
safe_cos_theta = np.clip(cos_theta, -1.0, 1.0)

theta_rad = np.arccos(safe_cos_theta)               # [rad] Angle in radians
theta_deg = np.rad2deg(theta_rad)                   # [º] Angle in degrees 


# Printing results
print(f"The dot product of u and v is: {uv}")
print(f"The expected result is: 5\n")

print(f"The module of u is: {norm_u:.3f}")
print(f"The expected result is: {np.sqrt(5):.3f}\n")

print(f"The module of v is: {norm_v:.3f}")
print(f"The expected result is: {np.sqrt(10):.3f}\n")

print(f"The angle between u and v is: {theta_deg:.2f}º")
print(f"The expected result is: 45.00º\n")




# YOUR TASK
print("\n")
print("TASK EXAMPLE:")

# Definition of vectors
a = np.array( [3, -1] )
b = np.array( [2, 2] )

# Dot product
ab = np.dot(a, b)

# Norm of vectors
norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)

# Angle between vectors
numerator = ab
denominator = norm_a * norm_b

cos_theta_ab = ( numerator / denominator )
safe_cos_theta_ab = np.clip(cos_theta_ab, -1.0, 1.0)

theta_ab_rad = np.arccos(safe_cos_theta_ab)               # [rad] Angle in radians
theta_ab_deg = np.rad2deg(theta_ab_rad)                   # [º] Angle in degrees 

# Printing results
print(f"The dot product of a and b is: {ab}")
print(f"The expected result is: 4\n")

print(f"The module of a is: {norm_a:.3f}")
print(f"The expected result is: {np.sqrt(10):.3f}\n")

print(f"The module of b is: {norm_b:.3f}")
print(f"The expected result is: {np.sqrt(8):.3f}\n")

print(f"The angle between a and b is: {theta_ab_deg:.2f}º")
print(f"The expected result is: 63.43º\n")




# YOUR TASK B
print("\n")
print("TASK EXAMPLE B:")

# Definition of vectors
p = np.array( [2, 1] )
q = np.array( [1, -2] )

# Dot product
pq = np.dot(p, q)

# Norm of vectors
norm_p = np.linalg.norm(p)
norm_q = np.linalg.norm(q)

# Angle between vectors
numerator = pq
denominator = norm_p * norm_q

cos_theta_pq = ( numerator / denominator )
safe_cos_theta_pq = np.clip(cos_theta_pq, -1.0, 1.0)

theta_pq_rad = np.arccos(safe_cos_theta_pq)               # [rad] Angle in radians
theta_pq_deg = np.rad2deg(theta_pq_rad)                   # [º] Angle in degrees 


# Printing results
print(f"The dot product of p and q is: {pq}")
print(f"The expected result is: 0\n")

print(f"The module of p is: {norm_p:.3f}")
print(f"The expected result is: {np.sqrt(5):.3f}\n")

print(f"The module of q is: {norm_q:.3f}")
print(f"The expected result is: {np.sqrt(5):.3f}\n")

print(f"The angle between p and q is: {theta_pq_deg:.2f}º")
print(f"The expected result is: 90.00º\n")

'''
p and q are perpendicular as its numerator is 0. When calculating the angle is 90º.
The dot rpoduct is not a vector because it multiplies each component of the vectors and sum its products.

'''





# BLOCK B: Engineering problem
#--------------------------------------
print("\n")
print("BLOCK B: Engineering problem: work in 2D")
print("-----------------------------------------")


# Definition of force and distance
F = np.array( [8, 6] )
s = np.array( [3, 4] )

# Calculus of work: W = F·s
W = np.dot(F, s)

# Magnitude of force and distance
norm_F = np.linalg.norm(F)
norm_s = np.linalg.norm(s)

# Calculus of angle between force and displacement
numerator = W
denominator = ( norm_F * norm_s )

cos_theta_Fs = numerator / denominator
theta_Fs_deg = np.rad2deg( np.arccos( np.clip(cos_theta_Fs, -1.0, 1.0) ) )

# Prints
print(f"The work is: {W} J")
print(f"The magnitude of the force is: {norm_F} N and the magnitude of displacement: {norm_s} m")
print(f"The cosinus of the angle between vectors is: {cos_theta_Fs} and the angle is of: {theta_Fs_deg:.2f}º\n")




# EXTRA CASE B2
F_2 = np.array( [10, 0] )
s_2 = np.array( [0, 2] )

W_2 = np.dot(F_2, s_2)

print("\n")
print(f"The work in this case B2 is: {W_2} J")




# EXTRA CASE B3
F_3 = np.array( [-5, 0] )
s_3 = np.array( [4, 0] )

W_3 = np.dot(F_3, s_3)

print("\n")
print(f"The work in this case B3 is: {W_3} J")




'''
Interpretation questions:
- Why does the dot product return a number rather than a vector?
+ Because it is the sum of the multiplication of the vector components

- What is the physical meaning of W > 0, W = 0 and W < 0?
+ W > 0 the force is produced in the direction of the displacement.
+ W = 0 the force is perpendicular to the direction.
+ W < 0 the force/displacement is applied in the opposite direction of the displacement/force.

- What fails when calculating the angle of a zero vector?
+ It fails the denominator as the cosinus of the angle is divided then by 0.

- Why does force in N multiplied by displacement in m give J?
+ Because the Joule [J] is the multiplication of a Newton [N] and a meter [m]

'''