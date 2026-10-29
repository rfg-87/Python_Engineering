'''
PROBLEM
---------------------------
Calculate a sum of the square of a number.

INPUTS
---------------------------
N --> Total numbers

OUTPUTS
---------------------------
sum_squares

EQUATIONS
---------------------------
S = Sigma_i0_N(i**2)

SPECIAL CASES
---------------------------
N --> infinite, particular case not evaluated

DO I NEED ITERATION?
---------------------------
Yes

ALGORITHM
---------------------------
1. Define N
2. Validate N
3. Calculate sum
4. Display result

VALIDATION
---------------------------
N is integer
N >= 1

'''


############################
#           CODE            
############################


# Import external functions
#---------------------------------------
import numpy as np
import sys



# Introduce variables
#---------------------------------------
N = 1000000

# Auxiliar variable for accumulate sum
sum_squares = 0


# Validation: 
#---------------------------------------
#if N is not int or N < 1: # It checks if it is an object or class integer
if not isinstance(N, int) or N < 1:
    print("\nIntroduce a positive integer value equal or above 1")
    sys.exit()


# Calculations
#---------------------------------------
for i in range(1, N + 1):

    sum_squares += i**2
    #print(f"i = {i}  |  total = {sum_squares}")



# Analytical validation
#---------------------------------------
analytical_result = (N * (N + 1) * (2 * N + 1)) // 6   # --> Integer division, if we apply / when the 
                                                       # number raises above a limit and we try to make it
                                                       # integer, it loses the precision as that number
                                                       # has passed to float

print(f"\nIterative result: {sum_squares}")
print(f"Analytical result: {analytical_result}\n")