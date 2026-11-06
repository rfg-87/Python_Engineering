'''
Exercice 27.

We are going to operate with the algebraic cross-product. It is also widely used in engineering.
For example, the moments generated in a beam.

Note: We are not going to consider special cases such as norm of a vector
equal to zero. We will do it in the future, thisi is just to understand how
to proceed

Use of library:
- numpy


Final Note: From this exercice on, I will represent and print the results of the operations and check
with the documentation: the expected result will not be writen in the print here.

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

# Define the vectors
a = np.array( [1, 0, 0] )
b = np.array( [0, 1, 0] )

# Cross product
c = np.cross(a, b)
d = np.cross(b, a)

# Norm of cross product vectors
norm_c = np.linalg.norm(c)
norm_d = np.linalg.norm(d)

# Printing results
print(f"Cross product of a over b: {c} with norm: {norm_c}")
print(f"Cross product of b over a: {d} with norm: {norm_d}")
print(f"Comparing cross product with dot product, dot product result: {np.dot(a, b)}")




# YOUR TASK
print("\n")
print("TASK EXAMPLE:")

###### CODE ######

# Define the vectors
u = np.array( [2, -1, 3] )
v = np.array( [1, 4, -2] )

# Cross product
w = np.cross(u, v)
y = np.cross(v, u)

# Norm of the cross product vectors
norm_w = np.linalg.norm(w)
norm_y = np.linalg.norm(y)

# Printing results
print(f"Cross product of u over v: {w} with norm: {norm_w:.4f}")
print(f"Cross product of v over u: {y} with norm: {norm_y:.4f}")
print(f"Comparing cross product with dot product, dot product result: {np.dot(u, v)}")

print(f"The vector u is perpendicular to w: {np.dot(u, w)}")
print(f"The vector v is perpendicular to w: {np.dot(v, w)}")






# BLOCK B: Engineering problem
#--------------------------------------
print("\n")
print("BLOCK B: Engineering problem: Moment of a planar force")
print("------------------------------------------------------")


# Definition of distance and force
r = np.array( [0.40, 0, 0] )
F = np.array( [0, 25, 0] )

# Calculus of moment for a force: M = r x F
M = np.cross(r, F)

# Magnitude of the moment
norm_M = np.linalg.norm(M)

# Value of the z component of the moment
M_z = M[2]

# Printing results
print(f"The moment of the force at a distance is: {M} Nm")
print(f"The magnitude of the moment is: {norm_M} Nm")
print(f'The moment goes in the direction z: {"+z" if M_z > 0 else ("0.0" if M_z == 0 else "-z")}')  # Need of '' and "" because one is inside the other

'The moment is positive as the vector of the direction goes over the F in the shorter path: right-sided'






# BLOCK C: Autonomous 3D case
#--------------------------------------
print("\n")
print("BLOCK C: Autonomous 3D case")
print("------------------------------------------------------")

# Definition of distance and force
r_C = np.array( [0.30, 0.20, 0] )
F_C = np.array( [10, -5, 20] )

# Calculus of moment for a force: M = r x F
M_C = np.cross(r_C, F_C)

# Magnitude of the moment
norm_M_C = np.linalg.norm(M_C)

# Printing results
print(f"The moment of the force at a distance is: {M_C} Nm")
print(f"The magnitude of the moment is: {norm_M_C:.4f} Nm")
print(f'Check of the components \n\
        The moment in x goes in the direction: {"+x" if M_C[0] > 0 else ("0.0" if M_C[0] == 0 else "-x")}\n\
        The moment in y goes in the direction: {"+y" if M_C[1] > 0 else ("0.0" if M_C[1] == 0 else "-y")}\n\
        The moment in z goes in the direction: {"+z" if M_C[2] > 0 else ("0.0" if M_C[2] == 0 else "-z")}')  # Need of '' and "" because one is inside the other






'''
Interpretation questions:
- Why is the cross product a vector instead of a scalar?
+ Because it is defined to give a vector perpendicular to the ones considered.
+ Also, it represents the area of the paralelogram that produce both vectors.

- What changes when we reverse the vector order?
+ It changes the sign (direction) of the cross producted vector

- Why does a planar-force problem produce a z moment?
+ Because the cross product generates a perpendicular product to that planar distance per a force

- Why are moments measured in N·m?
+ Because we are multiplying (cross product) a distance and a force: it represents that factor.
+ Normally, we can better know the contributions of both seeing it that way.
+ Finally, is how it was established.

'''