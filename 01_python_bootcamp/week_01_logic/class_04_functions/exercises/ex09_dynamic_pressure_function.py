'''
PROBLEM
---------------------------
Calculate the dynamic pressure (q) in a system with known density (rho) and velocity (vel)
but using functions to calculate it

INPUTS
---------------------------
For the calculate_dynamic_pressure() function:
    rho
    speed

OUTPUTS
---------------------------
Of the calculate_dynamic_pressure() function:
    q

EQUATIONS
---------------------------
Inside the calculate_dynamic_pressure() function:
    q = 0.5 * rho * speed**2

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
3. Call function
4. Validate rho
5. Validate speed
6. Apply equation
7. Return value of function
8. Display result

VALIDATION
---------------------------
rho >= 0
speed >= 0

'''


############################
#           CODE            
############################


# Import external functions
#---------------------------------------


# Define internal Function
#---------------------------

def calculate_dynamic_pressure(rho, speed):


    if rho < 0:

        print("\nPlease introduce a physical density (rho >= 0)\n")
        return None

    elif speed < 0:

        print("\nPlease introduce a physical speed (speed >= 0)\n")
        return None

    else:

        q = 0.5 * rho * speed**2

        return q



# Introduce variables
#---------------------------
rho = 1.225                 # [kg/m^3]
speed = 100.0               # [m/s] --> magnitude of velocity without direction


# Main Calculations
#---------------------------
dynamic_pressure = calculate_dynamic_pressure(rho, speed)

if dynamic_pressure is not None:
    print(f"\nDynamic pressure of the system: {dynamic_pressure} [Pa]\n") 


# Function reuse: examples for other values (no checks)
#------------------------------------------------------
q1 = calculate_dynamic_pressure(1.225, 100)
q2 = calculate_dynamic_pressure(1.225, 200)
q3 = calculate_dynamic_pressure(0.4, 500)

print(f"{q1} [Pa]")
print(f"{q2} [Pa]")
print(f"{q3} [Pa]\n")
