'''
PROBLEM
---------------------------
Calculate a mathematical function defined by 3 conditions.

INPUTS
---------------------------
speed
T as temperature

OUTPUTS
---------------------------
C_D

EQUATIONS
---------------------------
C_D = 0.3 for M < 0.8
C_D = 0.5 for 0.8 <= M < 1.2
C_D = 0.25 for M >= 1.2

SPECIAL CASES
---------------------------
M < 0 --> no physical meaning

DO I NEED ITERATION?
---------------------------
No

ALGORITHM
---------------------------
1. Define speed
2. Define speed_of_sound
3. Validate speed
4. Calculate when M < 0.8
5. Calculate when 0.8 <= M < 1.2
6. Calculate when M >= 1.2
7. Display result

VALIDATION
---------------------------
M >= 0
T > 0 in Kelvin

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
speed = 500     # [m/s]
T = 20          # [º]



# Validation
#---------------------------------------
if speed < 0:
    print("\nNo physical meaning for v < 0\n")
    sys.exit()

if T <= -273:
    print("\nNo physical meaning for T < -273 [º] or T < 0 [K]\n")
    sys.exit()



# Calculation of speed of sound
#--------------------------------------
# Constants for calculating speed of sound: Air
gamma = 1.4
R = 287                 # [J/kg·K]
T = T + 273             # [K]

# Speed of sound
speed_of_sound = np.sqrt(gamma * R * T)    # [m/s]



# Mach Number
#---------------------------------------
M = speed / speed_of_sound



# Calculation of C_D
#---------------------------------------
if M < 0.8:

    C_D = 0.3

    print(f"\nC_D = {C_D} for Mach {M:.2f}: M < 0.8\n")

elif M < 1.2:

    C_D = 0.5
    
    print(f"\nC_D = {C_D} for Mach {M:.2f}: 0.8 <= M < 1.2\n")

else:

    C_D = 0.25

    print(f"\nC_D = {C_D} for Mach {M:.2f}: M >= 1.2\n")