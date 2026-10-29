'''
PROBLEM
---------------------------
Calculate Taylor exponential approximation.

INPUTS
---------------------------
N --> highest polynomial order included in the approximation
xp --> Point of the function to evaluate

OUTPUTS
---------------------------
ex -- > Taylor approximation for e^x in a = 0

EQUATIONS
---------------------------
e**x = sum_n_N (x**n / n!)

SPECIAL CASES
---------------------------
n = 0 --> ex_Taylor = 1

DO I NEED ITERATION?
---------------------------
Yes

ALGORITHM
---------------------------
1. Define N
2. Validate N
3. Calculate power x**n
4. Calculate factorial n!
5. Iterate
6. Display result
7. Validate approximation against math.exp() function

VALIDATION
---------------------------
N is integer
N >= 0

'''


############################
#           CODE            
############################


# Import external functions
#---------------------------------------
from math import exp

import sympy as sp
import sys



# Introduce variables
#---------------------------------------
N = 5
x = sp.symbols("x")
xp = 0.5            # x under evaluation

# Auxiliar variable for accumulations
ex = sp.Integer(0)      # We start sum from 0
fact = 1
terms = []              # empty list for reorganize the terms with the symbols


# Validation: 
#---------------------------------------
if not isinstance(N, int) or N < 0:
    print("\nIntroduce a non-negative integer value\n")
    sys.exit()



print()
# Calculation modified to reorder the symbolic terms and start range from 0:
#---------------------------------------
for n in range(0, N + 1):

    term = x**n / fact

    ex += term

    terms.append(term)
    expression_to_show = " + ".join(str(term) for term in terms)

    print(f"n = {n}  | ex = {expression_to_show}")

    fact *= n + 1


ex_symbolic = ex
ex_numeric = ex_symbolic.subs(x, xp)



# Function validation
#---------------------------------------
analytical_result = exp(xp)

print(f"\nFor N = {N}")
print(f"Symbolic result for N = {N}     :    exp(x) = {expression_to_show}")
print(f"Iterative result for N = {N}    :    exp({xp}) = {ex_numeric}")
print(f"Analytical result             :    exp({xp}) = {analytical_result}\n")


# Old calculations
# # Calculations
# #---------------------------------------
# for n in range(1, N + 1):

#     fact *= n

#     ex += (x**n) / fact

#     print(f"n = {n}  |  ex = {ex}")


# if N > 0:
#     ex = ex.subs(x, xp)



