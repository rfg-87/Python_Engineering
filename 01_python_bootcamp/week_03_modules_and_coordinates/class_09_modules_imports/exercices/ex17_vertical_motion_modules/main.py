'''
This is the main module where we will define the configuration for the simulation and the 
calls of the necessary function to make the simulation.

INPUTS:


OUTPUTS:


We have split the problem into several modules

'''

############################
#           CODE            
############################


# Import external functions
#---------------------------------------


# Import internal functions
#---------------------------------------
from vertical_motion import validate_inputs, simulate_vertical_motion, analytical_solution, calculate_errors
from data_processing import process_trajectory


# Define Internal Functions
#---------------------------------------
def main():

    # Dictionary definition for variables introduced
    config = {
        "h0": 0.0,
        "v0": 50.0,
        "t0": 0.0,
        "g": 9.81,
        "dt": 0.1
    }

    if validate_inputs(config):

        # Dictionary of results and array of the trajectory h_new, v_new, t_new
        results, trajectory_array = simulate_vertical_motion(config)

        # Dictionary with analytical results from vertical_motion.py
        analytical_results = analytical_solution(config)

        # Dictionaries with the differences between computed and analytical results and the errors
        differences_results, errors_results = \
                    calculate_errors(analytical_results["analytical_max_altitude"], results["max_altitude"],
                                    analytical_results["analytical_final_velocity"], results["final_velocity"],
                                    analytical_results["analytical_time_of_flight"], results["time_of_flight"])

        # Dictionary with masked information (processed_results) and array with all calculations including
        # energy (processed_data)
        processed_results, processed_data = process_trajectory(trajectory_array, config)
        
        # Prints
        #------------------------------------
        
        # Print of results: maximum altitude, time of flight, end velocity
        print("\n"
            f"maximum altitude: {results['max_altitude']:.2f} m\n"
            f"time of flight: {results['time_of_flight']:.2f} s\n"
            f"end velocity: {results['final_velocity']:.2f} m/s\n"
        )

        # Print analytical results
        print("Validation wrt analytical solution:\n"
            f"+ Difference in the maximum altitude: {differences_results['difference_max_altitude']:.2f} m (Error of {errors_results['error_max_altitude']:.2f} %)\n"
            f"+ Difference in time of flight: {differences_results['difference_time_of_flight']:.2f} s (Error of {errors_results['error_time_of_flight']:.2f} %)\n"
            f"+ Difference in the final velocity: {differences_results['difference_final_velocity']:.2f} m/s (Error of {errors_results['error_final_velocity']:.2f} %)\n"
            f"+ Expected iterations {round(analytical_results['analytical_iterations'])} and iterations made {results['iterations']}\n"
        )

        # Print of masked results
        print(f'''
            -> How many states corresponds to ascent and descent?
            + For ascending, it corresponds: {processed_results["n_ascending"]} states.
            + For descending, it corresponds: {processed_results["n_descending"]} states.

            -> Which states are above 100 m?
            + The states above 100 m are: {processed_results["heights_above_100"]} states.

            -> What samples are between 2 and 5 seconds?
            + The samples between 2 and 5 seconds are: {processed_results["states_2_5_seconds"]} states.

            -> What states have h > 50 m and v > 0 m/s?
            + The states above 50 m and ascending are: {processed_results["height_over_50_positive_velocity"]} states.

            -> Mean and Standard Deviation of height and velocity.
            + The height mean and standard deviation are: {processed_results["mean_height"]} m with std dev of {processed_results["std_dev_height"]} m.
            + The velocity mean and standard deviation are: {processed_results["mean_velocity"]} m/s with std dev of {processed_results["std_dev_velocity"]} m.

            -> Indexes where h > 100 m.
            + The number of ascending states is {processed_results["n_ascending"]} with indexes for h > 100 {processed_results["indexes_h_above_100"]}.

            -> New matrix [h, v, t, energy].
            + The new matrix including energy, processed_data [h, v, t, energy] is: {processed_data}.

            -> Check of dt is approximately constant with np.diff() and np.allclose().
            + Using np.diff we have the array of the time differences: {processed_results["dt_samples_difference"]}.
            + That finally leads us to: {"Time Matches" if processed_results["dt_samples_reference"] else "Time DOES NOT Match"}
        ''')

        # Print every energy value during trajectory
        print(f"Total Energy as a function of mass:")

        for energy in processed_data[:, 3]:

            print(f"{energy:.2f} J/kg")

        print("\n")

        

# Main
#---------------------------------------
if __name__ == "__main__":
    main()