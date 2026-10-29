'''
This is a new class in which we are going to use the I/O concept: Input/Ouput.

To read and to write a file with some data calculated and also corrupting one of the files to 
apply exceptions and error management

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
from file_io import save_trajectory_csv, load_trajectory_csv



# Define Internal Functions
#---------------------------------------

# BLOCK C: enumerate(..., start = 2)
#--------------------------------------
def test_file(file_path):

    '''
    Function to test whether can happen to the file when we try to extract information and show errors:

    - file does not exist
    - values of the file are not proper
    - file and values ok

    We will use the try:

    The else: in the try only is executed if the try block finishes without any exception.

    The finally is for an action that must occur always, with or without exception (i.e: closing the reading file)
    
    '''

    print(f'\nTesting file: {file_path.name}')

    try:

        trajectory = load_trajectory_csv(file_path)

    except FileNotFoundError as error:

        print('FILE ERROR')
        print('----------')
        print(type(error).__name__)
        print(error)

    except ValueError as error:

        print('DATA ERROR')
        print('----------')
        print(type(error).__name__)
        print(error)

    else:

        print('READING OK')
        print('----------')
        print(f'Trajectory shape: {trajectory.shape}')
        print(f'{trajectory}')

    finally:

        print('Test finished')                              # Always executed with or without exception. Usually to close files but the with open(...) already closes it


def main():

    '''
    - Script directory: 
        + Path(__file__) we are giving the file current working file address as an anchor to a relative Path
        + .resolve()     we are making the route absolute and normalized (i.e for Windows and Linux)
        + .parent        gives the folder that has the script

        For example as absolute path: we can have: c/Windows/Desktop/Python_Engineering/week_04/main.py

        with .parent() we do: c/Windows/Desktop/Python_Engineering/week_04/

        __file__ represents the actual Python file and parent 

    '''

    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / 'data'

    data_dir.mkdir(exist_ok = True)

    valid_trajectory_file = data_dir / 'valid_trajectory.csv'        # Valid trajectory file --> Generated through file_io.py
    missing_trajectory_file = data_dir / 'missing_trajectory.csv'    # We will not generate this file
    corrupted_trajectory_file = data_dir / 'corrupted_trajectory.csv'# File with corrupted trajectory --> Generated through file_io.py

    '''
    We are going to apply the methods to the object generated to generate the trajectory using
    the methods in vertical_state.py and the class generated there

    '''

    # We define the constants to use
    dt = 0.1
    n_steps = 2

    # We define the object of the class
    earth_state = VerticalState(
        h = 100.0,
        v = 20.0
    )

    # We start the object state with a trajectory in instant 0: A LIST IS MORE EFFICIENT THAN AN ARRAY FOR DYNAMIC GROWTH: when final rows is unknown
    # In this case, in difference with regards to class 14 we are going to use a list
    trajectory_row = [earth_state.state_vector()]

    for i in  range(n_steps):

        earth_state.euler_step(dt)
        trajectory_row.append(earth_state.state_vector())

    trajectory = np.array(trajectory_row)




    # BLOCK 0: Generate reference values
    #--------------------------------------
    valid_trajectory = trajectory
    corrupted_trajectory = valid_trajectory.copy().astype(dtype=object) # astype change the type of the array
    corrupted_trajectory[1, 1] = 'NOT_A_NUMBER'                         # Alternative form of [1][1] for matrix is [1, 1]

    # Generate the .csv files
    save_trajectory_csv(valid_trajectory_file, valid_trajectory)
    save_trajectory_csv(corrupted_trajectory_file, corrupted_trajectory)

    # Load the file and extract the data:
    files_to_test = [
        valid_trajectory_file,
        missing_trajectory_file,
        corrupted_trajectory_file
    ]

    for file_path in files_to_test:

        test_file(file_path)

if __name__ == '__main__':
    main()




# FINAL VALIDATION
#-------------------------------------------------
'''
Explain:
- What is an exception?
+ An exception is an object that represents a problem or abnormal condition that occurs during program execution and interrupts the normal flow.
+ It is captured by the object except.

- How is an exception different from a syntax error?
+ A syntax error occurs when Python cannot correctly parse or understand the structure of the code before normal execution begins.
+ for example:
    if x > 5
        print('ok')

    It is missing a : (Syntax Error)  

  but float("NOT_A_NUMBER") is syntactically correct but when executed at some operation Python fails.  

- What code should go inside try?
+ The code that we want to protect over an error that we can interpret.

- Why should we catch FileNotFoundError and ValueError separately?
+ Because they mean different problems (an except Exception can capture both).
+ We catch them separately because they represent different problems and may require different responses.

- What does 'as error' give us?
+ It is giving us an object that saves the exception in a variable.

- When does else execute?
+ Only if the block try does not raise any exception.

- When does finally execute?
+ It is executed always, with or without exception.

- What does raise do?
+ It raises deliverately an exception.

- Why do we raise ValueError for an invalid header/column count?
+ It indicates that the value does not make sense or valid for the operation but the operation can be valid.

- Why should we avoid except Exception: in this exercise?
+ We avoid it because it can capture many unexpected errors that we do not actually know how to handle, hiding useful information and possible bugs.
+ Then, with ValueError we know exactly what we are managing.

- What does enumerate(file, start=2) give us?
+ enumerate() returns an iterable object that yields (index, item) pairs during iteration.

- Why is a line number useful in an error message?
+ Because we can go directly to see what is happening in that concrete line in the file.

- What is a traceback?
+ It is a chain of calls that was active when the exception occur.

- Which part of a traceback would you inspect first?
+ The last part of the message, there we have the message and type of error and read upwards .

- Why is silently returning an empty array after corrupted data dangerous?
+ Because we can avoid that error and continue with the operations.

- What is the difference between handling an error and hiding an error?
+ Handling an error means recognizing it and deliberately deciding how the program should respond.
+ Hiding an error means suppressing it without solving, reporting or understanding the problem.

'''