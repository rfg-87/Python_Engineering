'''
PROBLEM
---------------------------
Calculate the factorial of a number.

INPUTS
---------------------------
n --> Factorial number

OUTPUTS
---------------------------
fact -- > Factorial product

EQUATIONS
---------------------------
n! = n * (n-1) * (n-2) * (n-3) *...* 1

SPECIAL CASES
---------------------------
n = 0 --> fact = 1

DO I NEED ITERATION?
---------------------------
Yes

ALGORITHM
---------------------------
1. Define n
2. Validate n
3. Calculate factorial
4. Display result
5. Validate results math.factorial function

VALIDATION
---------------------------
n is integer
n >= 0

'''


############################
#           CODE            
############################


# Import external functions
#---------------------------------------
from math import factorial
import sys



# Introduce variables
#---------------------------------------
n = 5

# Auxiliar variable for accumulations
fact = 1
fact_reverse = 1


# Validation: 
#---------------------------------------
if not isinstance(n, int) or n < 0:
    print("\nIntroduce a non-negative integer value\n")
    sys.exit()


# Calculations
#---------------------------------------
for i in range(1, n + 1):

    fact *= i
    print(f"i = {i}  |  fact = {fact}")

# Alternative version
print("\n")
for i in range(n, 0, -1):

    fact_reverse *= i
    print(f"i = {i}  |  fact = {fact_reverse}")



# Function validation
#---------------------------------------
analytical_result = factorial(n)

print(f"\nIterative result: {fact}")
print(f"\nIterative inverse result: {fact_reverse}")
print(f"Analytical result: {analytical_result}\n")