'''
A module where we extract the results wanted and organize them.

INPUTS:


OUTPUTS:

'''

# Import external functions
#---------------------------------------
import numpy as np



# Define Internal Functions
#---------------------------------------
def process_trajectory(trajectory_array, config):

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

    heights = trajectory_array[:, 0]
    velocities = trajectory_array[:, 1]
    times = trajectory_array[:, 2]


    # Checking states
    #------------------------------------

    # Ascending/Descending masks
    ascending_mask = velocities > 0
    ascending_states = trajectory_array[ascending_mask]

    descending_mask = velocities < 0
    descending_states = trajectory_array[descending_mask]

    # Check states: above 100 m
    h_above_100 = heights > 100
    height_over_100 = trajectory_array[h_above_100]

    # Check states: time window between 2 and 5 seconds
    time_window = ( (times >= 2) & (times <= 5) )
    windows_state = trajectory_array[time_window]

    # Check states: height above 50 m and velocity above 0 m/s
    h_above_50 = ascending_states[:, 0] > 50
    height_over_positive_velocity = ascending_states[h_above_50]

    # Mean and Standar deviation
    mean_height = np.mean(heights)
    std_height = np.std(heights)

    mean_velocity = np.mean(velocities)
    std_velocity = np.std(velocities)

    # Indexes: total samples ascending and indexes of h > 100 m
    # The sum of a mask is giving us the number of samples that fulfill that condition
    indexes_h_above_100 = np.where(h_above_100)[0]

    # Check dt with np.diff() and np.allclose()
    dt_samples_diff = np.diff(times)

    dt_samples_allclose = np.allclose(dt_samples_diff, config["dt"])



    # Analyzing energy
    #----------------------------------------------
    energy = config["g"] * heights + 0.5 * velocities**2



    # Processed data: np.array including energy

    processed_data = np.column_stack((
        trajectory_array,
        energy
    ))

    # Results to return
    processed_results = {
        "n_ascending": np.sum(ascending_mask),
        "n_descending": np.sum(descending_mask),
        "heights_above_100": height_over_100,
        "states_2_5_seconds": windows_state,
        "height_over_50_positive_velocity": height_over_positive_velocity,
        "mean_height": mean_height,
        "std_dev_height": std_height,
        "mean_velocity": mean_velocity,
        "std_dev_velocity": std_velocity,
        "indexes_h_above_100": indexes_h_above_100,
        "dt_samples_difference": dt_samples_diff,
        "dt_samples_reference": dt_samples_allclose
    }


    return processed_results, processed_data