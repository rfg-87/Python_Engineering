'''
PROBLEM
---------------------------
Calculate vertical motion with Euler integral approximation: temporal integration.

But this time using functions.

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
1. Define functions
2. Define initial conditions
3. Calculate h
4. Calculate v
5. Calculate t
6. Calculate max_height
7. Iterate
8. Return results
9. Display result
10. Validate approximation against h = h0 + v0 * t - 0.5 * g * t**2
11. Validate approximation against h_max = h0 + v0**2 / (2 * g)
12. Validate approximation against t_f = (v0 + sqrt(v0**2 + 2 * g * h0)) / g
13. Validate approximation against v_f = - sqrt(v0**2 + 2 * g * h0)

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



# Define Internal Functions
#---------------------------------------
def validate_inputs(h0, v0, t0, g, dt):

    '''
    Validates the input values if they are consistent.

    INPUTS:
        - h0: initial height introduced.
        - v0: initial velocity introduced.
        - t0: initial time introduced.
        - g:  gravity constant introduced.
        - dt: delta time introduced.

    OUTPUTS:
        - Print: message giving information about no-validated value.
        - None:  return None if the initial consditions are not validated.

    '''

    if h0 < 0:
        print("\nIntroduce a non-negative initial height\n")
        return False

    if v0 <= 0:
        print("\nIntroduce a non-negative and above zero initial velocity\n")
        return False

    if t0 < 0:
        print("\nIntroduce a non-negative initial time\n")
        return False

    if dt <= 0:
        print("\nIntroduce a non-negative and above zero delta time\n")
        return False

    if g <= 0:
        print("\nIntroduce a non-negative and above zero gravity constant\n")
        return False

    return True


def simulate_vertical_motion(h0, v0, t0, g, dt):

    '''
    Makes the calculations of the simulaitons.

    INPUTS:
        - h0: initial height introduced & validated.
        - v0: initial velocity introduced & validated.
        - t0: initial time introduced & validated.
        - g:  gravity constant introduced & validated.
        - dt: delta time introduced & validated.

    OUTPUTS:
            - max_h: maximum height achieved in the simulation.
            - v_f:   final velocity when reaching ground.
            - t_f:   total time of flight of the simulation.
    '''

    # Initial state
    t = t0
    h = h0
    v = v0
    t_f = 0
    max_h = h0
    v_f = v0                # As if the total time is 0, the final velocity is equal to the initial

    print("Initial state: "
        f"t = {t:5.2f} s | "
        f"h = {h:8.2f} m | "
        f"v = {v:8.2f} m/s"
        )

    #Loop for calculations
    i = 0                   # iteration number

    while h >= 0:

        h, v, t = euler_step(h, v, t, g, dt)

        if h > max_h:
            max_h = h

        # h = h_new
        # v = v_new
        # t = t_new
        i += 1
        
        print(f"Iteration {i}: "
            f"t = {t:5.2f} s | "
            f"h = {h:8.2f} m | "
            f"v = {v:8.2f} m/s"
        )


    t_f = t - t0
    v_f = v

    return max_h, v_f, t_f, i


def euler_step(h, v, t, g, dt):

    '''
    Makes the calculations of the simulaitons.

    INPUTS:
        - h: state k of the height.
        - v: state k of the velocity.
        - t: state k of the time.
        - g: gravity constant introduced & validated.
        - dt: delta time introduced & validated.

    OUTPUTS:
            - h_new: state k + 1 of the height.
            - v_new: state k + 1 of the velocity.
            - t_new: state k + 1 of the time.
    '''

    h_new = h + v * dt
    v_new = v - g * dt
    t_new = t + dt

    return h_new, v_new, t_new


def analytical_solution(h0, v0, t_f, g, dt):

    '''
    Makes the calculations of the analytical solution.

    INPUTS:
        - h0: initial height introduced & validated.
        - v0: initial velocity introduced & validated.
        - t_f: total time of flight of the simulation.
        - g:  gravity constant introduced & validated.
        - dt: delta time introduced & validated.

    OUTPUTS:
            - analytical_h_max: analytical solution for maximum height.
            - analytical_v_f:   analytical solution for final velocity.
            - analytical_t_f:   analytical solution for time of flight.
            - N_steps:          Number of expected total iterations (just for double check).
    '''

    analytical_h_max = h0 + v0**2 / (2 * g)
    analytical_v_f = - sqrt(v0**2 + 2 * g * h0)
    analytical_t_f = (v0 + sqrt(v0**2 + 2 * g * h0)) / g
    N_steps = t_f / dt

    return analytical_h_max, analytical_v_f, analytical_t_f, N_steps


def calculate_errors(analytical_h_max, max_h, analytical_v_f, v_f, analytical_t_f, t_f):

    '''
    Makes the calculations of errors from simulation to analytical solution.

    INPUTS:
        - analytical_h_max: analytical solution for maximum height.
        - max_h: maximum height achieved in the simulation.          
        - analytical_v_f:   analytical solution for final velocity.
        - v_f:   final velocity when reaching ground.
        - analytical_t_f:   analytical solution for time of flight.
        - t_f:   total time of flight of the simulation.

    OUTPUTS:
        - difference_h_max: absolute difference between maximum height from simulation to analytical solution. 
        - difference_v_f:   absolute difference between final velocity from simulation to analytical solution.
        - difference_t_f:   absolute difference between time of flight from simulation to analytical solution.
        - error_h_max: error in the maximum height from the simulation to the analytical solution.
        - error_v_f:   error in the final velocity from the simulation to the analytical solution.
        - error_t_f:   error in the time of flight from the simulation to the analytical solution.
    '''

    difference_h_max = analytical_h_max - max_h
    difference_v_f = analytical_v_f - v_f
    difference_t_f = analytical_t_f - t_f
    
    error_h_max = abs(difference_h_max) / analytical_h_max * 100
    error_v_f = abs(difference_v_f) / abs(analytical_v_f) * 100
    error_t_f = abs(difference_t_f) / analytical_t_f * 100

    return difference_h_max, difference_v_f, difference_t_f, error_h_max, error_v_f, error_t_f
    


# Main Calculations
#---------------------------------------

# Introduce variables
#---------------------------------------
h0 = 0
v0 = 50
t0 = 0
g = 9.81  
dt = 0.1


# Validation: 
#---------------------------------------
if validate_inputs(h0, v0, t0, g, dt):

    print()
    # Calculation:
    #---------------------------------------
    max_h, v_f, t_f, i = simulate_vertical_motion(h0, v0, t0, g, dt)

    print("\n"
        f"maximum altitude: {max_h:.2f} m\n"
        f"time of flight: {t_f:.2f} s\n"
        f"end velocity: {v_f:.2f} m/s\n"
    )


    # Analytical result for comparisson & Errors
    #-------------------------------------------
    analytical_h_max, analytical_v_f, analytical_t_f, N_steps = analytical_solution(h0, v0, t_f, g, dt)

    difference_h_max, difference_v_f, difference_t_f, error_h_max, error_v_f, error_t_f = \
            calculate_errors(analytical_h_max, max_h, analytical_v_f, v_f, analytical_t_f, t_f)

    print("Validation wrt analytical solution:\n"
        f"+ Difference in the maximum altitude: {difference_h_max:.2f} m (Error of {error_h_max:.2f} %)\n"
        f"+ Difference in time of flight: {difference_t_f:.2f} s (Error of {error_t_f:.2f} %)\n"
        f"+ Difference in the final velocity: {difference_v_f:.2f} m/s (Error of {error_v_f:.2f} %)\n"
        f"+ Expected iterations {N_steps} and iterations made {i}\n"
    )