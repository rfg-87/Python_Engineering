'''
This is a new class in which we are going to introduce the oop concept: object oriented programming.

In vertical_state.py we generate the class that defines the objects that we want to create/analyze
and the functions that in this case are called methods that acts over the objects generated modifying
them: they modify their atributes.

'''



############################
#           CODE            
############################


# Import external functions
#---------------------------------------



# Import Internal Functions
#---------------------------------------
from vertical_state import VerticalState




# Define Internal Functions
#---------------------------------------
def main():

    # Main Calculations
    #---------------------------------------





    ##################################
    # EXERCICE
    ##################################




    # BLOCK F: Create 2 independent objects
    #--------------------------------------
    print("\n")
    print("BLOCK F: Create 2 independent objects:")
    print("--------------------------------------")

    '''
    Both objects are of the same class but they keep independent atributes. They are defined by
    h, v, t, g but with different atributes

    '''

    earth_state = VerticalState(
        h = 100.0,
        v = 20.0
    )

    # The moon_state will override the value of gravity
    moon_state = VerticalState(
        h = 100.0,
        v = 20.0,
        g = 1.62
    )




    # BLOCK G: Using methods
    #--------------------------------------
    print("\n")
    print("BLOCK G: Using methods:")
    print("-----------------------")

    '''
    We are going to use the methods defined in vertical_state.py to calculate some parameters of the
    object such as specific energy or to use the euler integration method to update the state of the
    object: we will have the earth_before and earth_after as variables that are updated before applying
    the euler method and after applying it with the atributes of the object h, v, t updated

    '''

    # Specific energy calculation
    earth_energy = earth_state.specific_energy()
    moon_energy = moon_state.specific_energy()

    # State vector before applying euler method
    earth_state_before_euler = earth_state.state_vector()
    moon_state_before_euler = moon_state.state_vector()

    # State vector after applying euler method: First update of the state, then, assign variable
    # to the updated state
    earth_state.euler_step(0.1)
    moon_state.euler_step(0.1)

    earth_state_after_euler = earth_state.state_vector()
    moon_state_after_euler = moon_state.state_vector()


    print(f'''
        The energy of the Earth object at initial position is: {earth_energy} [J/kg]
        The energy of the Moon object at initial position is: {moon_energy} [J/kg]

        The initial state vector of the Earth object (h, v, t) is: {earth_state_before_euler}
        The initial state vector of the Moon object (h, v, t) is: {moon_state_before_euler}

        The state vector of the Earth object (h, v, t) after applying Euler is: {earth_state_after_euler}
        The state vector of the Moon object (h, v, t) after applying Euler is: {moon_state_after_euler}
    ''')



# BLOCK H: main.py
#--------------------------------------
print("\n")
print("BLOCK H: main.py:")
print("-----------------")

'''
main.py module and calling function

'''

if __name__ == "__main__":
    main()






# FINAL VALIDATION
#-------------------------------------------------
'''
Explain:
- What is a class?
+ It is a general definition of several objects that shares same attributes but not same values of them
and the operations that can be made over those objects.
+ A class is a general definition or blueprint that describes the attributes and methods that its objects can have.

- What is an object or instance?
+ An object is a defined class defined but its concrete atributes.
+ An object is a concrete instance of a class with its own attribute values

- What does __init__ do?
+ It initializes the object with its atributes.

- What does self refer to?
+ It is referred to the object atributes when used into a method.

- What is the difference between parameter h and self.h?
+ h is a received parameter meanwhile the self.h is an atribute saved in the obejct.
+ self is a reference to the current object (instance) on which the method is being executed and
self.h access to the current object atribute h

- What is an attribute?
+ They are variables or data associated to the object.

- What is a method?
+ It is a function defined into a class but it works with the objects created inside that class.

- Why can earth_state and moon_state have different g values?
+ Because they are different objects defined under the same class: same atributes but with different values.

- What changes inside the object when euler_step() is called?
+ It is changing the atributes of the object h, v, t.

- Why is earth_state.specific_energy() different from VerticalState.specific_energy?
+ Because it is a method applied to a concrete object and VerticalState.specific_energy() is a function
in which we have to pass the parameters.
+ In VerticalState.specific_energy(earth_state) we have to pass the earth_state inside the specific_energy.
As the method is defined we can used earth_state_specific_energy().

- What advantages does this representation have over passing h, v, t and g to every function?
+ Because we can reuse the methods for several defined objects instead of calling them one by one to 
different functions.

'''