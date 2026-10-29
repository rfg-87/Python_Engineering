'''
PROBLEM
---------------------------
Calculate the dynamic pressure (q) in a system with known density (rho) and velocity (vel)

INPUTS
---------------------------
rho
vel

OUTPUTS
---------------------------
q

EQUATIONS
---------------------------
q = 0.5 * rho * vel**2

SPECIAL CASES
---------------------------
rho < 0   --> invalid physical input
speed < 0 --> invalid physical input
rho = 0   --> dynamic_pressure = 0 (vacuum)
speed = 0 --> dynamic_pressure = 0

DO I NEED ITERATION?
---------------------------
No

ALGORITHM
---------------------------
1. Define rho
2. Define speed (magnitude of velocity, therefore non-negative)
3. Validate rho
4. Apply equation
5. Display result

VALIDATION
---------------------------
rho >= 0
speed >= 0

'''


############################
#           CODE            
############################

# Introduce variables
#---------------------------
rho = 1.225                 # [kg/m^3]
speed = 100.0               # [m/s] --> magnitude of velocity without direction

if rho < 0:

    print("\nPlease introduce a physical density (rho >= 0)\n")

elif speed < 0:

    print("\nPlease introduce a physical speed (speed >= 0)\n")

else:

    dynamic_pressure = 0.5 * rho * speed**2
    print(f"\nDynamic pressure of the system: {dynamic_pressure} [Pa]\n") 