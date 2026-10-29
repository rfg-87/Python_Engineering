'''
PROBLEM
---------------------------
Calculate Taylor exponential approximation.

But this time using a function.

INPUTS
---------------------------
N --> highest polynomial order included in the approximation
xp --> Point of the function to evaluate

OUTPUTS
---------------------------
ex_numeric --> Numerical Taylor approximation evaluated at xp.

expression_to_show --> Symbolic representation of the Taylor polynomial.

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
1. Define function
2. Define N
3. Call function
4. Validate N
5. Calculate power x**n
6. Calculate factorial n!
7. Iterate
8. Return value
9. Display result
10. Validate approximation against math.exp() function

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



# Define Internal Functions
#---------------------------------------
def taylor_exp(x, N, xp):

    # Auxiliar variable for accumulations
    ex = sp.Integer(0)      # We start sum from 0
    fact = 1
    terms = []              # empty list for reorganize the terms with the symbols


    # Validation: 
    #---------------------------------------
    if not isinstance(N, int) or N < 0:
        print("\nIntroduce a non-negative integer value\n")
        return None, None


    print()
    # Calculation modified to reorder the symbolic terms and start range from 0:
    #---------------------------------------
    for n in range(0, N + 1):

        term = x**n / fact

        ex += term

        terms.append(term)
        expression_to_show = " + ".join(str(term) for term in terms)

        #print(f"n = {n}  | ex = {expression_to_show}")  --> It was for control

        fact *= n + 1


    ex_symbolic = ex
    ex_numeric = ex_symbolic.subs(x, xp)

    return ex_numeric, expression_to_show



# Introduce variables
#---------------------------------------
N = 5
x = sp.symbols("x")
xp = 0.5            # x under evaluation



# Main Calculations
#---------------------------------------
approximation, expression_to_show = taylor_exp(x, N, xp)

if approximation is not None:
    print(f"\nThe McLaurin approximation of e^x for N = {N} and xp = {xp} is: {approximation}")
    print(f"{expression_to_show}\n")


# Function validation
#---------------------------------------
analytical_result = exp(xp)

print(f"\nFor N = {N}")
print(f"Symbolic result for N = {N}     :    exp(x) = {expression_to_show}")
print(f"Iterative result for N = {N}    :    exp({xp}) = {approximation}")
print(f"Analytical result             :    exp({xp}) = {analytical_result}\n")



# Other cases to look for: Defined cases
#---------------------------------------
approximation1, expression_to_show1 = taylor_exp(x, N = 0, xp = 0.5)        # Positional argument cannot appear after keyword parameters
                                                                            # That is why x is at first position
print(f"\nFor N = 0")
print(f"Symbolic result for N = 0     :    exp(x) = {expression_to_show1}")
print(f"Iterative result for N = 0    :    exp({xp}) = {approximation1}")
print(f"Analytical result             :    exp({xp}) = {analytical_result}\n")

approximation2, expression_to_show2 = taylor_exp(x, N = 5, xp = 0.5)        
print(f"\nFor N = 5")
print(f"Symbolic result for N = 5     :    exp(x) = {expression_to_show2}")
print(f"Iterative result for N = 5    :    exp({xp}) = {approximation2}")
print(f"Analytical result             :    exp({xp}) = {analytical_result}\n")

approximation3, expression_to_show3 = taylor_exp(x, N = 10, xp = 0.5)        
print(f"\nFor N = 10")
print(f"Symbolic result for N = 10    :    exp(x) = {expression_to_show3}")
print(f"Iterative result for N = 10   :    exp({xp}) = {approximation3}")
print(f"Analytical result             :    exp({xp}) = {analytical_result}\n")

approximation4, expression_to_show4 = taylor_exp(x, N = 10, xp = 2)
xp2 = 2
analytical_result4 = exp(xp2)        
print(f"\nFor N = 10")
print(f"Symbolic result for N = 10    :    exp(x) = {expression_to_show4}")
print(f"Iterative result for N = 10   :    exp(2) = {float(approximation4)}")  # Has to define as a float because if not the result is showed as a fraction
print(f"Analytical result             :    exp(2) = {analytical_result4}\n")

approximation5, expression_to_show5 = taylor_exp(x, N = -1, xp = 0.5)
approximation5, expression_to_show5 = taylor_exp(x, N = 3.5, xp = 0.5)