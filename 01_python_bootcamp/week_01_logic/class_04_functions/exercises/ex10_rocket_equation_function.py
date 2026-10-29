'''
PROBLEM
---------------------------
Calculate the difference of velocity of a rocket (delta_v) knowing its specific impulse (Isp),
considering constant gravity at sea level (g0) and a relation of initial mass (m0) and a final
mass (mf) between two estates.

But now, defining a function to calculate it and calling it.

INPUTS
---------------------------
Isp
g0 (constant and known) --> Defined inside the definition of the function in this case
m0
mf

OUTPUTS
---------------------------
delta_v

EQUATIONS
---------------------------
delta_v = Isp * g0 * ln(m0 / mf)

SPECIAL CASES
---------------------------
Isp < 0 --> not possible engine used
m0 < mf --> physical not possible
m0 = mf --> analyzing same state

DO I NEED ITERATION?
---------------------------
No

ALGORITHM
---------------------------
1. Define function and its arguments
2. Define Isp
3. Define initial mass m0
4. Define final mass mf
5. Call function
6. Validate Isp
7. Validate m0
8. Validate mf
9. Validate m0 > mf
10. Calculate mass ratio
11. Calculate delta_v
12. Return result from function
13. Display result
14. Other analysis

VALIDATION
---------------------------
Isp >= 0
m0 > 0
mf > 0
m0 > mf

'''


############################
#           CODE            
############################


# Import external functions
#---------------------------------------
import numpy as np


# Define Internal Functions with keywords arguments
#---------------------------------------
def calculate_rocket_delta_v(
        Isp,
        m0,
        mf,
        g0 = 9.80665
        ):

    if Isp < 0:

        print("\nPlease define a valid Isp. Isp < 0 means no physical possible specific impulse.\n")
        return None

    elif m0 <= 0:

        print("\nPlease review initial mass as is either negative or zero.\n")
        return None

    elif mf <= 0:

        print("\nPlease review final mass as is either negative or zero.\n")
        return None

    elif m0 <= mf:

        print(
            "\nPlease review initial and final masses as final mass cannot be equal "
            "or higher than the initial mass.\n"
        )
        return None

    else: 

        mass_ratio = m0 / mf
        delta_v = Isp * g0 * np.log(mass_ratio)

        return delta_v


# Introduce variables
#---------------------------------------
Isp = 250       # [s]
#g0 = 9.81       # [m/s^2]              Is defined as a constant parameter inside the def of the function
m0 = 500000     # [kg]
mf = 250000      # [kg]



# Main Calculations
#---------------------------

delta_v = calculate_rocket_delta_v(Isp, m0, mf)             # We define g0 inside the definition
                                                            # of the function

if delta_v is not None:
    print(f"\nThe ideal rocket delta_v is: {delta_v:.2f} [m/s]\n")

# Function call with keyword arguments
delta_v_keyword = calculate_rocket_delta_v(Isp = 500, m0 = 500000, mf = 250000)

if delta_v_keyword is not None:
    print(f"\nThe ideal rocket delta_v_keyword is: {delta_v_keyword:.2f} [m/s]\n")



# Function reuse: nominal cases & keyword arguments
#------------------------------------------------------
delta_v1 = calculate_rocket_delta_v(0, m0, mf)          # Isp = 0
print(f"\nControl print for Isp = 0: delta_v1 = {delta_v1} [m/s]\n")
delta_v2 = calculate_rocket_delta_v(Isp, 250000, mf)    # m0 = mf
delta_v3 = calculate_rocket_delta_v(Isp, m0, 0)         # mf = 0
delta_v4 = calculate_rocket_delta_v(Isp, 125000, mf)    # m0 < mf
delta_v5 = calculate_rocket_delta_v(-250, m0, mf)       # Isp < 0