'''
This is an exercice to introduce the Object Oriented Programming OOP, in order to introduce
the class object, how to configure it with __init__ the generation of specific objects
associated to that class and the methods applied to that object.

Inside the class definition, we have to define the methods that can be applied to the object
created under that class. The identation is important and the methods must be inside the 
class definition.

'''

############################
#           CODE            
############################


# Import external functions
#---------------------------------------
import numpy as np



# Define Internal Functions
#---------------------------------------





# Main Calculations
#---------------------------------------





##################################
# EXERCICE
##################################



# BLOCK A: Create a class
#--------------------------------------
print("\n")
print("BLOCK A: Create a class:")
print("------------------------")

class VerticalState:

    '''
    Definition of the VerticalState class with the atributes to define an object of that class
    and with the methods that can be applied to that object (functions below: def...energy_state(),
    euler_step(), etc.)

    '''

    def __init__(self, h, v, t = 0.0, g = 9.81):

        self.h = h
        self.v = v
        self.t = t
        self.g = g




    # BLOCK B: Method specific_energy()
    #--------------------------------------
    print("\n")
    print("BLOCK B: Method specific_energy():")
    print("----------------------------------")

    def specific_energy(self):

        '''
        This function calculates and return the specific energy. It is converted to a method applied
        later to the object.

        INPUTS:
        - No need of inputs as with "self" it will be using the attributes of the object to calculate
        the energy

        OUTPUTS:
        - e: specific energy

        '''

        e = self.g * self.h + 0.5 * self.v**2

        return e




    # BLOCK C: Method state_vector
    #--------------------------------------
    print("\n")
    print("BLOCK C: Method state_vector:")
    print("-----------------------------")

    def state_vector(self):

        '''
        This function calculates and return the state vector. It is converted to a method applied
        later to the object.

        INPUTS:
        - No need of inputs as with "self" it will be using the attributes of the object to calculate
        the state vector of it

        OUTPUTS:
        - state: state vector of the object
            
        '''

        state = np.array([self.h, self.v, self.t])

        return state




    # BLOCK D: Method is_ascending()
    #--------------------------------------
    print("\n")
    print("BLOCK D: Method is_ascending():")
    print("-------------------------------")

    def is_ascending(self):

        '''
        This function calculates and return the states that are ascending with v > 0. It is converted to a method applied
        later to the object.

        INPUTS:
        - No need of inputsas with "self" it will be using the attributes of the object to know if it is
        ascending or not

        OUTPUTS:
        - ascending: the mask to know if the object is ascending considering v > 0.0

        '''

        ascending = self.v > 0.0

        return ascending




    # BLOCK E: Method euler_step()
    #--------------------------------------
    print("\n")
    print("BLOCK E: Method euler_step():")
    print("-----------------------------")

    def euler_step(self, dt):

        '''
        This function modifies the object: before calling, it has some h, v and t but after
        using the method over the object, this one has a new state

        INPUTS:
        - dt: differential of time or increased time between steps to update
        - No need of other inputs as with "self" it will be using the attributes of the object to update
        the state of the object when moving in vertical motion

        OUTPUTS:
        - No outputs per se: this function or method is updating/modifying the h, v, t of the object
        
        '''

        self.h = self.h + self.v * dt

        self.v = self.v - self.g * dt

        self.t = self.t + dt