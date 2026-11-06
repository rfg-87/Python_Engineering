'''
Exercice 25.

We are going to operate with vectors in a simply way in order to understand the algebra and the 
functions in Python that we can apply to them.

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
print("BLOCK A: : Fully solved and task algebra example")
print("-------------------------------------------------")


# SOLVED EXAMPLE
print("\n")
print("SOLVED EXAMPLE:")

# Definition of vectors
u = np.array( [3, -1] )
v = np.array( [-2, 4] )

# Sum of vectors
sum_vectors = u + v

# Linear combination
linear_comb = 2 * u + (-1) * v

# Norms
norm_sum_vectors = np.linalg.norm(sum_vectors)
norm_linear_comb = np.linalg.norm(linear_comb)

# Printing results
print(f"The sum of u and v is: {sum_vectors}")
print(f"The expected result is: [1, 3]\n")

print(f"The linear combination of 2u - v is: {linear_comb}")
print(f"The expected result is: [8, -6]\n")

print(f"The norm of u + v is: {norm_sum_vectors:.4f}")
print(f"The expected result is: 3.1623\n")

print(f"The norm of 2u - v is: {norm_linear_comb}")
print(f"The expected result is: 10.0\n")




# YOUR TASK
print("\n")
print("TASK EXAMPLE:")

# Definition of vectors
a = np.array( [2, -1] )
b = np.array( [-3, 5] )

# Sum of vectors
sum_vectors_task = a + b

# Linear combination
linear_comb_task = 2 * a + (-1) * b

# Norms
norm_sum_vectors_task = np.linalg.norm(sum_vectors_task)
norm_linear_comb_task = np.linalg.norm(linear_comb_task)

# Printing results
print(f"The sum of a and b is: {sum_vectors_task}")
print(f"The expected result is: [-1, 4]\n")

print(f"The linear combination of 2a - b is: {linear_comb_task}")
print(f"The expected result is: [7, -7]\n")

print(f"The norm of a + b is: {norm_sum_vectors_task:.4f}")
print(f"The expected result is: 4.1231\n")

print(f"The norm of 2a - b is: {norm_linear_comb_task:.4f}")
print(f"The expected result is: 9.8995\n")






# BLOCK B: Engineering problem
#--------------------------------------
print("\n")
print("BLOCK B: : Engineering problem: forces in 2D")
print("-------------------------------------------------")


# Definition of forces
F1 = np.array( [3, 4] )     # [N] units in Newtons
F2 = np.array( [-1, 2] )    # [N] units in Newtons

# Magnitude of forces
norm_F1 = np.linalg.norm(F1)
norm_F2 = np.linalg.norm(F2)

# Resultant of forces
R = F1 + F2

# Magnitude of resultant
norm_R = np.linalg.norm(R)


# Printing results
print(f"The magnitude of F1 is: {norm_F1:.3f} N")
print(f"The expected result is: 5.000 N\n")

print(f"The magnitude of F2 is: {norm_F2:.3f} N")
print(f"The expected result is: 2.236 N\n")

print(f"The resultant force R is: {R} N")
print(f"The expected result is: [2, 6] N\n")

print(f"The resultant magnitude force R is: {norm_R:.3f} N")
print(f"The expected result is: 6.325 N\n")