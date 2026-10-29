'''
This is a new class in which we are going to use test files to make a project verified.

This is the test for the vertical_state.py

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



# Import Internal Functions
#---------------------------------------
from vertical_state import VerticalState



# Define Internal Functions
#---------------------------------------

# BLOCK A: Create tests as functions
#--------------------------------------
def test_initial_state():

    '''
    A test is a code that executes part of the script and compares the real result with an expected result

    '''

    # ARRANGE
    state = VerticalState(h = 100.0, v = 20.0)

    # ACT
    result = state.state_vector()

    # ASSERT
    expected = np.array( [100.0, 20.0, 0.0] )
    
    assert np.allclose(result, expected), f'Expected values: {expected}, got: {result}'     


# BLOCK B: Test of Euler method
#--------------------------------------
def test_euler_step():

    '''
    We are checking a known physical/numerical behavior. If in the future euler_step() is modified and the 
    result is broken, the test will pop up an advice.

    '''

    # ARRANGE
    state = VerticalState(h = 100.0, v = 20.0)
    dt = 0.1

    # ACT
    state.euler_step(dt)
    result = state.state_vector()

    # ASSERT
    expected = np.array( [102.0, 19.019, 0.1] )

    assert np.allclose(result, expected), f'Expected Euler: {expected}, got: {result}'


# BLOCK C: Why np.allclose()
#--------------------------------------
# We use np.allclose() instead of == because we are comparing floating numbers and we need to have little tolerance.