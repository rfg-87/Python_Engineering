'''
This is an exercice to introduce the Input/Ouput concepts to read and write files.

The idea is the next:

VerticalState object
        ↓
trajectory in RAM
        ↓
save
        ↓
CSV file on disk
        ↓
read
        ↓
strings
        ↓
float conversion
        ↓
NumPy array
        ↓
validation

'''

############################
#           CODE            
############################


# Import external functions
#---------------------------------------
import numpy as np


##################################
# EXERCICE
##################################


# Define Internal Functions
#---------------------------------------
# BLOCK A: Create a class
#--------------------------------------
class VerticalState:

    '''
    Definition of the VerticalState class with the atributes to define an object of that class
    and with the methods that can be applied to that object

    '''

    def __init__(self, h, v, t = 0.0, g = 9.81):

        '''
        Initialization of the VerticalState class with its arguments that will define each object

        '''

        self.h = h
        self.v = v
        self.t = t
        self.g = g


    def state_vector(self):

        state = np.array([self.h, self.v, self.t])

        return state


    def euler_step(self, dt):

        self.h = self.h + self.v * dt
        self.v = self.v - self.g * dt
        self.t = self.t + dt