'''
PROBLEM
---------------------------
Calculate vertical motion with Euler integral approximation: temporal integration.

But this time using functions.

But this time using lists and tuples.

Adding the use of dictionaries for the INPUTS and OUTPUTS

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

trajectory:
    List of states stored as:

    (height, velocity, time)

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
comparison between required initial conditions and introduced

'''


############################
#           CODE            
############################


# Import external functions
#---------------------------------------
from math import sqrt



# Define Internal Functions
#---------------------------------------
def validate_inputs(config):

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
        - True/False:  return False if the initial consditions are not validated.

    '''

    # Compare provided initial variables with required
    required = {
        "h0",
        "v0",
        "t0",
        "g",
        "dt"
    }

    provided = set(config.keys())

    missing = required - provided

    if missing != set():
        print(f"\nThere is/are missing variable/s: {missing}\n")
        return False


    #Required conditions that the initial conditions need
    if config["h0"] < 0:
        print("\nIntroduce a non-negative initial height\n")
        return False

    if config["v0"] <= 0:
        print("\nIntroduce a non-negative and above zero initial velocity\n")
        return False

    if config["t0"] < 0:
        print("\nIntroduce a non-negative initial time\n")
        return False

    if config["dt"] <= 0:
        print("\nIntroduce a non-negative and above zero delta time\n")
        return False

    if config["g"] <= 0:
        print("\nIntroduce a non-negative and above zero gravity constant\n")
        return False

    return True


def simulate_vertical_motion(config):

    '''
    Makes the calculations of the simulaitons.

    In this case using lists and tuples

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
            - i:     number of iterations.
            - trajectory: tuple of the state for each trajectory point analysed.
    '''

    # Initial state
    # Defining lists of elements
    h = []
    v = []
    t = []
    trajectory = []

    h.append(config["h0"])
    v.append(config["v0"])
    t.append(config["t0"])

    # Defining tuple for trajectory
    trajectory.append( (config["h0"], config["v0"], config["t0"]) ) 

    t_f = 0
    max_h = config["h0"]
    v_f = config["v0"]                # As if the total time is 0, the final velocity is equal to the initial

    print("Initial state: "
        f"t = {t[0]:5.2f} s | "
        f"h = {h[0]:8.2f} m | "
        f"v = {v[0]:8.2f} m/s"
        )

    #Loop for calculations
    i = 0                   # iteration number

    while h[i] >= 0:

        h_new, v_new, t_new = euler_step(h[i], v[i], t[i], config["g"], config["dt"])

        h.append(h_new)
        v.append(v_new)
        t.append(t_new)
        trajectory.append( (h_new, v_new, t_new) )

        i += 1
        
        print(f"Iteration {i}: "
            f"t = {t[i]:5.2f} s | "
            f"h = {h[i]:8.2f} m | "
            f"v = {v[i]:8.2f} m/s"
        )

    max_h = max(h)
    t_f = t[i] - config["t0"]
    v_f = v[i]

    results = {
        "max_altitude": max_h,
        "final_velocity": v_f,
        "time_of_flight": t_f,
        "iterations": i
    }

    return results, trajectory


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


def analytical_solution(config):

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

    analytical_h_max = config["h0"] + config["v0"]**2 / (2 * config["g"])
    analytical_v_f = - sqrt(config["v0"]**2 + 2 * config["g"] * config["h0"])
    analytical_t_f = (config["v0"] + sqrt(config["v0"]**2 + 2 * config["g"] * config["h0"])) / config["g"]
    N_steps = analytical_t_f / config["dt"]

    analytical_results = {
        "analytical_max_altitude": analytical_h_max,
        "analytical_final_velocity": analytical_v_f,
        "analytical_time_of_flight": analytical_t_f,
        "analytical_iterations": N_steps
    }

    return analytical_results


# The next definition of function is kept as original in order to check wether the internal variables
# are kept when they have different name in the call
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

    differences_results = {
        "difference_max_altitude": difference_h_max,
        "difference_final_velocity": difference_v_f,
        "difference_time_of_flight": difference_t_f
    }

    errors_results = {
        "error_max_altitude": error_h_max,
        "error_final_velocity": error_v_f,
        "error_time_of_flight": error_t_f
    }

    return differences_results, errors_results
    


# Main Calculations
#---------------------------------------

# Introduce variables
#---------------------------------------
# h0 = 0
# v0 = 50
# t0 = 0
# g = 9.81  
# dt = 0.1


# Dictionary definition for variables introduced
config = {
    "h0": 0.0,
    "v0": 50.0,
    "t0": 0.0,
    "g": 9.81,
    "dt": 0.1
}


# Validation: 
#---------------------------------------
if validate_inputs(config):

    print()
    # Calculation:
    #---------------------------------------
    results, trajectory = simulate_vertical_motion(config)

    print("\n"
        f"maximum altitude: {results['max_altitude']:.2f} m\n"
        f"time of flight: {results['time_of_flight']:.2f} s\n"
        f"end velocity: {results['final_velocity']:.2f} m/s\n"
    )


    #Extraction of maximum height and final velocity and time of flight through tuple listed
    max_h_trajectory = max(state[0] for state in trajectory)
    v_f_trajectory = trajectory[-1][1]
    t_f_trajectory = trajectory[-1][2] - config["t0"]

    print("\n"
            f"maximum altitude from trajectory: {max_h_trajectory:.2f} m\n"
            f"time of flight from trajectory: {t_f_trajectory:.2f} s\n"
            f"end velocity from trajectory {v_f_trajectory:.2f} m/s\n"
        )


    # Analytical result for comparisson & Errors
    #-------------------------------------------
    analytical_results = analytical_solution(config)

    differences_results, errors_results = \
            calculate_errors(analytical_results["analytical_max_altitude"], results["max_altitude"],
                            analytical_results["analytical_final_velocity"], results["final_velocity"],
                            analytical_results["analytical_time_of_flight"], results["time_of_flight"])

    print("Validation wrt analytical solution:\n"
        f"+ Difference in the maximum altitude: {differences_results['difference_max_altitude']:.2f} m (Error of {errors_results['error_max_altitude']:.2f} %)\n"
        f"+ Difference in time of flight: {differences_results['difference_time_of_flight']:.2f} s (Error of {errors_results['error_time_of_flight']:.2f} %)\n"
        f"+ Difference in the final velocity: {differences_results['difference_final_velocity']:.2f} m/s (Error of {errors_results['error_final_velocity']:.2f} %)\n"
        f"+ Expected iterations {round(analytical_results['analytical_iterations'])} and iterations made {results['iterations']}\n"
    )