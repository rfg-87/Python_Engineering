'''
This is a new class in which we are going to use the I/O concept: Input/Ouput.

To read and to write a file with some data calculated

In vertical_state.py we generate the class that defines the objects that we want to create/analyze
and the functions that in this case are called methods that acts over the objects generated modifying
them: they modify their atributes.

In main.py we are going to use the folder where the script lies as reference, not the folder from
where we have open the terminal

# relative path
Path('data/results.csv')

# absolute path example
Path('/home/user/project/data/results.csv')

We separate:
- main.py: for main operations and calls.
- vertical_state.py: where we keep the physics of the problem.
- file_io.py: where we interact with the files generated with the data generated.

'''



############################
#           CODE            
############################

##################################
# EXERCICE
##################################

# Import external functions
#---------------------------------------
import numpy as np
from pathlib import Path



# Import Internal Functions
#---------------------------------------
from vertical_state import VerticalState
from file_io import save_trajectory_csv, load_trajectory_csv, append_run_log



# Define Internal Functions
#---------------------------------------

def main():

    # BLOCK B: Create a robust route with pathlib
    #--------------------------------------
    '''
    - Script directory: 
        + Path(__file__) we are giving the file current working file address as an anchor to a relative Path
        + .resolve()     we are making the route absolute and normalized (i.e for Windows and Linux)
        + .parent        gives the folder that has the script

        For example as absolute path: we can have: c/Windows/Desktop/Python_Engineering/week_04/main.py

        with .parent() we do: c/Windows/Desktop/Python_Engineering/week_04/

        __file__ represents the actual Python file and parent 

    '''

    base_dir = Path(__file__).resolve().parent      # Script directory: absolute folder address

    #data_dir = base_dir + '/data'                   # We use + to concatenate string --> NO DEJA
    data_dir = base_dir / 'data'                    # Alternatively, we can use / to construct addresses without concatenate strings

    data_dir.mkdir(exist_ok = True)                 # We generate that folder if it does not exist or ignore if it exists


    trajectory_file = data_dir / 'vertical_trajectory.csv'   # Trajectory file address
    log_file = data_dir / 'run_log.txt'                     # Data log address




    # BLOCK C: Generate trajectoy in memory
    #--------------------------------------
    '''
    We are going to apply the methods to the object generated to generate the trajectory using
    the methods in vertical_state.py and the class generated there

    '''

    # We define the constants to use
    dt = 0.1
    n_steps = 5

    # We define the object of the class
    earth_state = VerticalState(
        h = 100.0,
        v = 20.0
    )

    # We start the object state with a trajectory in instant 0: A LIST IS MORE EFFICIENT THAN AN ARRAY
    #trajectory_row = [earth_state.state_vector()]
    #trajectory = np.array([earth_state.state_vector()])
    trajectory = earth_state.state_vector()             # As the method state.vetor() returns an array

    for i in range(n_steps):

        earth_state.euler_step(dt)                      # Modifies earth_state object
        # new_trajectory = np.array([earth_state.state_vector()])
        new_trajectory = earth_state.state_vector()     # Makes the state.vector() of the object arguments h, v t in an array return
        trajectory = np.vstack( (trajectory, new_trajectory) )
        #trajectory_row.append(earth_state.state_vector())

    #trajectory = np.array(trajectory_row)




    # BLOCK E: Check visually the file
    #--------------------------------------
    # Save the file to open it
    save_trajectory_csv(trajectory_file, trajectory)

    # Load the file and extract the data: directly an np.array
    loaded_trajectory_from_csv = load_trajectory_csv(trajectory_file)





    # BLOCK G: Validate round trip (data -> file -> reconstructed data)
    #--------------------------------------
    # Check if the shape of the original data and loaded_data are the same
    same_shape = trajectory.shape == loaded_trajectory_from_csv.shape

    # Check if the values are the same using np.allclose()
    same_values = np.allclose(trajectory, loaded_trajectory_from_csv)




    # BLOCK H: Practice mode append 'a' inside with
    #--------------------------------------
    '''
    We are going to use a log file to save a summary of each execution without deleting the previous data

    This log file saves the last state of every run with the command 'a' that writes extra lines instead
    of rewriting all the file as it does with 'w'

    '''

    final_state = trajectory[-1]

    message = (
        f'steps = {n_steps}, dt = {dt}, '
        f'final_h = {final_state[0]:.6f}, '
        f'final_v = {final_state[1]:.6f}, '
        f'final_t = {final_state[2]:.6f}'
    )

    append_run_log(log_file, message)


    # Printing compact summary:
    print(f'\ntrajectory shape: {trajectory.shape}')
    print(f'\n{trajectory}')

    print(f'\n{loaded_trajectory_from_csv}')

    print(f'''
        The data calculated and the loaded data from the CSV file have the same shape?
            {"YES" if same_shape else "NO"}
        The data calculated and the loaded data from the CSV file have the same values (within a tolerance)?
            {"YES" if same_values else "NO"}
    ''')




# BLOCK I: Imports and main.py
#--------------------------------------
if __name__ == '__main__':
    main()





# FINAL VALIDATION
#-------------------------------------------------
'''
Explain:
- What is file I/O?
+ It stands for Input/Output file. Read and write in general terms.

- What is the difference between RAM data and persistent file data?
+ The RAM data is used when running and goes away when the script ends.
+ Persistent data is the one that we can go to search for it after the script has run.

- What does open() return?
+ It opens the file that in the address given with a condition of reading, writing, etc. and optionally
we can define the type of encoding. Access the file.
+ It returns an object that we use to interact with the file.

- What does mode 'w' do if the file already exists?
+ It overwrites the current file.

- What is the difference between 'w', 'r' and 'a'?
+ 'w' writes entirely the file or overwrites if we had a previous one.
+ 'r' reads the file. If it does not exist it gives us an error.
+ 'a' appends new data keeping the data before.

- Why do we use 'with open(...) as file:'?
+ Because we generate a context manager so when we abandon the block, Python closes the file.

- What does file.write() receive?
+ It receives the data in a string type to be writen in the file

- Why do numerical values become text when written to this CSV?
+ Because the CSV file is a text file and write is writing text.

- What does file.readline() do in our loader?
+ It reads the header in this case. readline() is for reading a line.

- Why do we call strip() before split(',')?
+ Because we want to clean the lines of white spaces in the extremes or line jumps before spliting into a list.

- What does split(',') return?
+ It returns a list with the line values separataed with a comma as text (string) in every index of the list

- Why do we use float() after split()?
+ To give a numerical type of data to a returned text (string) data.

- What does Path(__file__).resolve().parent represent?
+ It represents the absolute folder where the script is. It also normalize it to not differenciate
between OS adressing management.

- Why is file_io.py separated from vertical_state.py?
+ Because we separate the physical part of the problem with regards to the persistence layer or 
data management. In this case, the class and its properties is separated from the file management.

- What is a round-trip validation?
+ It consists of comparing data from calculations to the loaded data from files where we have save
that data. Check:
Calculations -> Files -> loaded_data

- Why is np.allclose() more appropriate than exact float equality here?
+ When we write :.6f we have chosen a limited decimal precision and we are also working with floats
that we want to compare inside a tolerance.

'''