'''
PROBLEM
---------------------------
Calculate the difference of velocity of a rocket (Delta_V) knowing its specific impulse (Isp),
considering constant gravity at sea level (g0) and a relation of initial mass (m0) and a final
mass (mf) between two estates

INPUTS
---------------------------
Isp
g0 (constant and known)
m0
mf

OUTPUTS
---------------------------
Delta_V

EQUATIONS
---------------------------
Delta_V = Isp * g0 * ln(m0 / mf)

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
1. Define g0
2. Define Isp
3. Define initial mass m0
4. Define final mass mf
5. Validate Isp
6. Validate m0
7. Validate mf
8. Validate m0 > mf
9. Calculate mass ratio
10. Calculate delta_V
11. Display result

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


# Introduce variables
#---------------------------------------
Isp = 250       # [s]
g0 = 9.81       # [m/s^2]
m0 = 500000     # [kg]
mf = 500000      # [kg]


if Isp < 0:

    print("\nPlease define a valid Isp. Isp < 0 means no physical possible specific impulse.")

elif m0 <= 0:

    print("\nPlease review initial mass as is either negative or zero.\n")

elif mf <= 0:

    print("\nPlease review final mass as is either negative or zero.\n")

elif m0 <= mf:

    print(
        "\nPlease review initial and final masses as final mass cannot be equal "
        "or higher than the initial mass.\n"
    )

else: 

    mass_ratio = m0 / mf
    delta_v = Isp * g0 * np.log(mass_ratio)

    print(f"\nThe ideal rocket delta_v is: {delta_v} [m/s]\n")