'''
PROBLEM
---------------------------
Calculate vertical motion with Euler integral approximation: temporal integration.

INPUTS
---------------------------
h0 --> Initial height/altitude
v0 --> Initial velocity
t0 --> Initial time
g  --> Gravity constant
dt --> Delta time or time increase per step

OUTPUTS
---------------------------
time_flight --> Total time above ground or time of flight: t_f
max_altitude --> Maximum altitude reached during flight: max_h
final_vel   --> Final velocity when reaching ground: vel_f

EQUATIONS
---------------------------
dh/dt = v
dv/dt = -g

SPECIAL CASES
---------------------------
Negative height initial value --> not contemplated

DO I NEED ITERATION?
---------------------------
Yes

ALGORITHM
---------------------------
1. Define initial conditions
2. Calculate h
3. Calculate v
4. Calculate t
5. Calculate max_height
6. Iterate
7. Display result
8. Validate approximation against h = h0 + v0 * t - 0.5 * g * t**2
9. Validate approximation against h_max = h0 + v0**2 / (2 * g)
10. Validate approximation against t_f = (v0 + sqrt(v0**2 + 2 * g * h0)) / g
11. Validate approximation against v_f = - sqrt(v0**2 + 2 * g * h0)

VALIDATION
---------------------------
dt > 0
g > 0
h0 >= 0
v0 > 0
t0 >= 0 

'''


############################
#           CODE            
############################


# Import external functions
#---------------------------------------
from math import sqrt

import sys



# Introduce variables
#---------------------------------------
h0 = 0
v0 = 50
t0 = 0
g = 9.81  
dt = 0.01



# Validation: 
#---------------------------------------
if h0 < 0:
    print("\nIntroduce a non-negative initial height\n")
    sys.exit()

elif v0 <= 0:
    print("\nIntroduce a non-negative and above zero initial velocity\n")
    sys.exit()

elif t0 < 0:
    print("\nIntroduce a non-negative initial time\n")
    sys.exit()

elif dt <= 0:
    print("\nIntroduce a non-negative and above zero delta time\n")
    sys.exit()

elif g <= 0:
    print("\nIntroduce a non-negative and above zero gravity constant\n")
    sys.exit()



print()
# Calculation:
#---------------------------------------

# Initial state
t = t0
h = h0
v = v0
t_f = 0
max_h = h0
v_f = v0                # As if the total time is 0, the final velocity is equal to the initial
E = g * h + v**2 / 2

print("Initial state: "
    f"t = {t:5.2f} s | "
    f"h = {h:8.2f} m | "
    f"v = {v:8.2f} m/s | "
    f"E = {E:8.2f} J/kg"
)


#Loop for calculations
i = 0                   # iteration number

while h >= 0:

    h_new = h + v * dt
    v_new = v - g * dt
    t_new = t + dt
    E = g * h_new + v_new**2 / 2

    if h_new > max_h:
        max_h = h_new

    h = h_new
    v = v_new
    t = t_new
    i += 1
    
    print(f"Iteration {i}: "
        f"t = {t:5.2f} s | "
        f"h = {h:8.2f} m | "
        f"v = {v:8.2f} m/s | "
        f"E = {E:8.2f} J/kg"
    )


t_f = t - t0
v_f = v

print("\n"
    f"maximum altitude: {max_h:.2f} m\n"
    f"time of flight: {t_f:.2f} s\n"
    f"end velocity: {v_f:.2f} m/s\n"
)




# Function validation
#---------------------------------------
analytical_h_max = h0 + v0**2 / (2 * g)
analytical_t_f = (v0 + sqrt(v0**2 + 2 * g * h0)) / g
analytical_v_f = - sqrt(v0**2 + 2 * g * h0)
N_steps = t_f / dt

difference_h_max = analytical_h_max - max_h
difference_t_f = analytical_t_f - t_f
difference_v_f = analytical_v_f - v_f
difference_iterations = N_steps - i

error_h_max = abs(difference_h_max) / analytical_h_max * 100
error_t_f = abs(difference_t_f) / analytical_t_f * 100
error_v_f = abs(difference_v_f) / abs(analytical_v_f) * 100     # As the analytical velocity < 0; we need the abs value

print("Validation wrt analytical solution:\n"
    f"+ Difference in the maximum altitude: {difference_h_max:.2f} m (Error of {error_h_max:.2f} %)\n"
    f"+ Difference in time of flight: {difference_t_f:.2f} s (Error of {error_t_f:.2f} %)\n"
    f"+ Difference in the final velocity: {difference_v_f:.2f} m/s (Error of {error_v_f:.2f} %)\n"
    f"+ Expected iterations {N_steps} and iterations made {i}\n"
)