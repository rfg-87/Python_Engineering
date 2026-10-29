'''
PROBLEM
---------------------------
Calculate the solution of a quadratic equation considering its multiple cases through the discriminant
and the constants a, b, c.

INPUTS
---------------------------
a
b
c

OUTPUTS
---------------------------
x

EQUATIONS
---------------------------
a*x**2 + b*x + c = 0

SPECIAL CASES
---------------------------
discriminant = 0 --> one solution
discriminant < 0 --> no real roots
a = 0            --> not quadratic: first order
b = 0            --> direct quadratic
c = 0            --> particular quadratic
a, b, c = 0      --> combinations of constants that may do the solution to explode

DO I NEED ITERATION?
---------------------------
No

ALGORITHM
---------------------------
1. Define a
2. Define b
3. Define b
4. Validate a = 0 
5. Validate b = 0 
6. Validate c = 0 
7. Calculate when a = 0 and subcases
8. Calculate when b = 0 and subcases
9. Calculate when c = 0 and subcases
10. Calculate x
11. Display result

VALIDATION
---------------------------
a, b, c are real numbers

'''


############################
#           CODE            
############################


# Import external functions
#---------------------------------------
import numpy as np
import numbers


# Introduce variables
#---------------------------------------
# Case 1 of 2 roots
# a = 1 
# b = -3
# c = 2

# Case 2 of double root
# a = 1 
# b = 2
# c = 1

# Case 3 of without roots: imaginary
# a = 1 
# b = 0
# c = 1

# Case 4 not quadratic
a = 0 
b = 2
c = 1


# Validation that variables are real
#---------------------------------------
if isinstance(a, numbers.Real) == False:
    print("\nPlease introduce 'a' as a real number")

if isinstance(b, numbers.Real) == False:
    print("\nPlease introduce 'b' as a real number")

if isinstance(c, numbers.Real) == False:
    print("\nPlease introduce 'c' as a real number")

#Alternatively we can use: n.imag != 0


# Special cases
#---------------------------------------
if a == 0:

    if b == 0:

        if c == 0:
            print("\nEquation is already 0 = 0. Infinitely many solutions\n")
        else:
            print("\nNo solution for x, as a = 0 and b = 0 and c != 0. Only solution c = 0.\n")

    else:

        x = - (c / b)

        print(f"\nThe solution of the equation is of first order: x = {x}\n")

        check = b * x + c

        print(f"Check of the solution 'b * x + c' of first order: {check}\n")

elif b == 0:

    if a == 0: #Dead code: ecloding case contemplated above for the combination a = 0 and b = 0
    
            if c == 0:
                print("\nEquation is already 0 = 0. Infinitely many solutions\n")
            else:
                print("\nNo solution for x, as a = 0 and b = 0 and c != 0. Only solution c = 0.\n")

    elif c == 0:

        x = 0

        print(f"\nThe solution of the equation is: x = {x}\n")



    if (c / a) < 0:

        x1 = np.sqrt(- (c / a))
        x2 = -x1

        print(f"\nThe solution of the equation is: x1 = {x1} and x2 = {x2}\n")

        check_1 = a * x1**2 + c
        check_2 = a * x2**2 + c
        
        print(f"Check of the solution 'a * x1**2 + c' for x1: {check_1}")
        print(f"Check of the solution 'a * x2**2 + c' for x2: {check_2}\n")

    else:

        x1 = complex(0, np.sqrt(abs(- (c / a))))
        x2 = - x1

        print(f"The solution of the equation is complex: x1 = {x1} and x2 = {x2}\n")

        check_1 = a * x1**2 + c
        check_2 = a * x2**2 + c
        
        print(f"Check of the imaginary solution 'a * x1**2 + c' for x1: {check_1}")
        print(f"Check of the imaginary solution 'a * x2**2 + c' for x2: {check_2}\n")

elif c == 0:

    if a == 0:

        x = 0

        print(f"\nThe solution of the equation is: x = {x}\n")

    if b == 0:

        x = 0
        
        print(f"\nThe solution of the equation is: x = {x}\n")

    x1 = 0
    x2 = - (b / a)

    print(f"\nThe solution of the equation is: x1 = {x1} and x2 = {x2}\n")

    check_1 = a * x1**2 + b * x1
    check_2 = a * x2**2 + b * x2
    
    print(f"Check of the solution 'a * x1**2 + b * x1' for x1: {check_1}")
    print(f"Check of the solution 'a * x2**2 + b * x2' for x2: {check_2}\n")

else:
    # Standard solution: a*x**2 + b*x + c = 0
    #---------------------------------------
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:

        x1 = complex(- (b), np.sqrt(abs(discriminant))) / (2*a)
        x2 = x1.conjugate()

        print(f"\nThe solution of the equation is complex: x1 = {x1} and x2 = {x2}\n")

        check_1 = a * x1**2 + b * x1 + c
        check_2 = a * x2**2 + b * x2 + c
        
        print(f"Check of the solution 'a * x1**2 + b * x1 + c' for x1: {check_1}")
        print(f"Check of the solution 'a * x2**2 + b * x2 + c' for x2: {check_2}\n")

    elif discriminant == 0:

        x = - (b / (2*a))

        print(f"\nThe solution of the equation is: x = {x}\n")

        check = a * x**2 + b * x + c
        
        print(f"Check of the solution 'a * x**2 + b * x + c' is: {check}\n")

    else:

        x1 = (- (b) + np.sqrt(discriminant)) / (2*a)
        x2 = (- (b) - np.sqrt(discriminant)) / (2*a)

        print(f"\nThe solution of the equation is: x1 = {x1} and x2 = {x2}\n")

        check_1 = a * x1**2 + b * x1 + c
        check_2 = a * x2**2 + b * x2 + c
        
        print(f"Check of the solution 'a * x1**2 + b * x1 + c' for x1: {check_1}")
        print(f"Check of the solution 'a * x2**2 + b * x2 + c' for x2: {check_2}\n")