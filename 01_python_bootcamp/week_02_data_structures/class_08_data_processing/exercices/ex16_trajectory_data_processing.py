'''
PROBLEM
---------------------------
Calculate vertical motion with Euler integral approximation: temporal integration.

But this time using functions.

But this time using lists and tuples.

Adding the use of dictionaries for the INPUTS and OUTPUTS.

Defining trajectory as an array too.

BOOLEAN MASKS
DATA PROCESSING: Answer the next quesitons:

-> How many states corresponds to ascent and descent?
-> Which states are above 100m?
-> What samples are between 2 and 5 seconds?
-> What states have h > 50 m and v > 0 m/s?
-> Mean and Standard Deviation of height and velocity.
-> Indexes where h > 100 m.
-> New matrix [h, v, t, energy].
-> Check of dt is approximately constant with np.diff() and np.allclose().

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

trajectory_array:
    Array of the states stored:
    
                h          v          t
    row 0   [  0.0      50.000      0.0 ]
    row 1   [  5.0      49.019      0.1 ]
    row 2   [  9.902    48.038      0.2 ]
    ...

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
import numpy as np



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

    #Defining array for trajectory
    trajectory_array = np.empty( (0, 3) )

    h.append(config["h0"])
    v.append(config["v0"])
    t.append(config["t0"])

    # Defining tuple for trajectory
    trajectory.append( (config["h0"], config["v0"], config["t0"]) ) 

    #Defining first row of the nparray of trajectory
    state_0 = np.array([ [config["h0"], config["v0"], config["t0"]] ])  # Define an np.array for the initial state
    trajectory_array = np.append(trajectory_array, state_0, axis = 0)   # Add the initial state to the trajectory_array
    print(trajectory_array.shape)

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

        new_state = np.array([ [h_new, v_new, t_new] ])
        trajectory_array = np.append(trajectory_array, new_state, axis = 0)

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

    return results, trajectory, trajectory_array


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
    results, trajectory, trajectory_array = simulate_vertical_motion(config)

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
            f"end velocity from trajectory: {v_f_trajectory:.2f} m/s\n"
        )


    #Extraction of maximum height and final velocity and time of flight through np.array
    max_h_trajectory_array = np.max(trajectory_array[:, 0])
    v_f_trajectory_array = trajectory_array[-1][1]
    t_f_trajectory_array = trajectory_array[-1][2] - config["t0"]

    print("\n"
            f"maximum altitude from trajectory_array: {max_h_trajectory_array:.2f} m\n"
            f"time of flight from trajectory_array: {t_f_trajectory_array:.2f} s\n"
            f"end velocity from trajectory_array: {v_f_trajectory_array:.2f} m/s\n"
        )

    energy = config["g"] * trajectory_array[:, 0] + 0.5 * trajectory_array[:, 1]**2

    # energy = energy.round(2) --> Rounds to 2 decimals the result
    # np.set_printoptions(formatter = {'float': '{:0.2f}'.format}) # If we print the array with 2 decimals
    print(f"Total Energy as a function of mass:")

    for en in energy:

        print(f"{en:.2f} J/kg")

    print("\n")

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




# BOOLEAN Masks
#---------------------------------------
'''
We use a boolean mask to filter the information that we want from the array obtained
in the calculations as we know that:

- heights column is     trajectory_array[:, 0]
- velocities column is  trajectory_array[:, 1]
- times column is       trajectory_array[:, 2]

We filter out the data and the states (at the end, the array) by the conditions that
we want to check or filter

'''

# Ascending/Descending masks
ascending_mask = trajectory_array[:, 1] > 0
ascending_states = trajectory_array[ascending_mask]

descending_mask = trajectory_array[:, 1] < 0
descending_states = trajectory_array[descending_mask]

# Check states: above 100 m
h_above_100 = trajectory_array[:, 0] > 100
height_over_100 = trajectory_array[h_above_100]

# Check states: time window between 2 and 5 seconds
time_1 = trajectory_array[:, 2]
time_2 = trajectory_array[:, 2]
time_window = ( (time_1 >= 2) & (time_2 <= 5) )
windows_state = trajectory_array[time_window]

# Alternatively
# times = trajectory_array[:, 2]

# time_window = (
#     (times >= 2)
#     & (times <= 5)
# )

# Check states: height above 50 m and velocity above 0 m/s
h_above_50 = ascending_states[:, 0] > 50
height_over_positive_velocity = ascending_states[h_above_50]

# Mean and Standar deviation
mean_height = np.mean(trajectory_array[:, 0])
std_height = np.std(trajectory_array[:, 0])

mean_velocity = np.mean(trajectory_array[:, 1])
std_velocity = np.std(trajectory_array[:, 1])

# Indexes: total samples ascending and indexes of h > 100 m
# The sum of a mask is giving us the number of samples that fulfill that condition
n_samples_ascending = np.sum(trajectory_array[:, 1] > 0)

indexes_h_above_100 = np.where(h_above_100)[0]

# Matrix adding the energy: Creating a new dataset
processed_data = np.column_stack((
    # trajectory_array[:, 0],
    # trajectory_array[:, 1],
    # trajectory_array[:, 2],
    trajectory_array,
    energy
))

# Check dt with np.diff() and np.allclose()
dt_samples_diff = np.diff(trajectory_array[:, 2])

dt_samples_allclose = np.allclose(dt_samples_diff, config["dt"])

print(f'''
    -> How many states corresponds to ascent and descent?
    + For ascending, it corresponds: {np.sum(ascending_mask)} states.
    + For descending, it corresponds: {np.sum(descending_mask)} states.

    -> Which states are above 100 m?
    + The states above 100 m are: {height_over_100} states.

    -> What samples are between 2 and 5 seconds?
    + The samples between 2 and 5 seconds are: {windows_state} states.

    -> What states have h > 50 m and v > 0 m/s?
    + The states above 50 m and ascending are: {height_over_positive_velocity} states.

    -> Mean and Standard Deviation of height and velocity.
    + The height mean and standard deviation are: {mean_height} m with std dev of {std_height} m.
    + The velocity mean and standard deviation are: {mean_velocity} m/s with std dev of {std_velocity} m.

    -> Indexes where h > 100 m.
    + The number of ascending states is {n_samples_ascending} with indexes for h > 100 {indexes_h_above_100}.

    -> New matrix [h, v, t, energy].
    + The new matrix including energy, processed_data [h, v, t, energy] is: {processed_data}.

    -> Check of dt is approximately constant with np.diff() and np.allclose().
    + Using np.diff we have the array of the time differences: {dt_samples_diff}.
    + That finally leads us to: {"Time Matches" if dt_samples_allclose else "Time DOES NOT Match"}
''')

# The calculation of rows for a filtered state can be also done as:
# n_ascending = ascending_states.shape[0]
# n_descending = descending_states.shape[0]