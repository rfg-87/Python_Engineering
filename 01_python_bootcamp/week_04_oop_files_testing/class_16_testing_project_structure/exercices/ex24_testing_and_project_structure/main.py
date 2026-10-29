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

In this case, we added the run_tests.py and the tests/ folder as we are going to test that the functions and modules
for the main.py are working properly

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
- What is a test?
+ It is a code which purpose is to check automatically that other code is behaving as expected.

- What is the difference between production/application code and test code?
+ Application code is the code that implements the actual behavior and functionality of the program.
+ Test code verifies that the application code behaves as expected.

- Explain Arrange, Act and Assert.
+ Arrange: objects, data and conditions that I prepare.
+ Act: function or method to execute.
+ Assert: the result expected and how I check it.

- What does assert do?
+ It checks a boolean expression.

- What happens when an assertion is False?
+ It raises an AssertionError: the result did not match the expected.

- Why do we use np.allclose for floating-point arrays?
+ Because floating-point calculations may introduce small numerical representation differences.

- Why should each test check one clear behavior?
+ Because if the test fails, we can identify more easily which specific behavior is broken.

- What is a regression?
+ It happens when a modification of the code breaks the nominal behavior.

- Why should tests be repeatable?
+ Because in that case it can be trustworthy creating its own inputs and cleans them afterwards.
+ Not depending on edited files.

- What is the difference between PASS, FAIL and ERROR?
+ PASS: The test passed without any raise of assert or error. The assert happens but with True.
+ FAIL: It gives an assert error: not matching results from expected.
+ ERROR: For unexpected exceptions.

- Why do we intentionally test FileNotFoundError?
+ Because raising FileNotFoundError for a missing file is part of the expected behavior of the application, and
expected failure behavior should also be tested.

- Why is except Exception acceptable in our test runner but not a good default everywhere?
+ Because the test runner must report unexpected exceptions without allowing one test to stop the execution of the remaining tests.

- What is tests/__init__.py doing in this exercise?
+ It is generating the tests/ folder as a package so we can import its modules and functions.

- Why do tests live in a separate folder?
+ Because it is better for separating the production code to the test code.

- Why should main.py not contain the test logic?
+ Because it is the production or final code.

- What advantage does this structure give us before uploading to GitHub?
+ It is giving us a checked and validated code.

'''