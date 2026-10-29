'''
This is a new class in which we are going to use test files to make a project verified.

This is the test for the file_io.py

We build the basic mechanism to understand:

    Arrange -> Act -> Assert

This is intended to be an automated check.

Reference values

- initial state:
h = 100.0 m
v = 20.0 m/s
t = 0.0 s
g = 9.81 m/s^2
dt = 0.1 s

- after one Euler step:
h = 102.0
v = 19.019
t = 0.1

And now we generate an auxiliar file with those values for the initial state and the state after 0.1 seconds.

With this, we can compare both files.

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
from file_io import save_trajectory_csv, load_trajectory_csv



# Define Internal Functions
#---------------------------------------

# BLOCK D: Round test for File I/O
#--------------------------------------
def test_csv_round_trip():

    '''
    Test function in which we generate a reference file from kwnon values (expected)
    and then compare to the generated

    '''

    # Path definition for different files
    base_dir = Path(__file__).resolve().parent.parent

    data_dir = base_dir / 'data'
    data_dir.mkdir(exist_ok = True)

    test_file = data_dir / 'test_round_trip.csv'

    # Generate the test_file with the original (reference) values
    reference = np.array( [ 
        [100.0, 20.0, 0.0],
        [102.0, 19.019, 0.1]
    ] )

    save_trajectory_csv(test_file, reference)

    loaded_reference_result = load_trajectory_csv(test_file)

    # Assert of the shape between reference value and loaded_reference_result
    assert reference.shape == loaded_reference_result.shape
    assert np.allclose(reference, loaded_reference_result)

    # Delete the .csv file generated for test
    test_file.unlink(missing_ok = True)                # missing_ok = True avoids giving an error if the file does not exist. We use it for cleaning temporary test files.


# BLOCK E: Test of an expected exception
#--------------------------------------
def test_missing_file_raises():

    base_dir = Path(__file__).resolve().parent.parent

    missing_file = base_dir / 'data' / 'does_not_exist.csv'

    try:

        load_trajectory_csv(missing_file)

    except FileNotFoundError:
        
        pass

    else:

        assert False, 'Expected FileNotFoundError, but no exception was raised'