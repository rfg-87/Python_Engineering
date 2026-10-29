'''
Advanced functions.

We are going to see different alternatives to put parameters and arguments inside a function, so they 
can be more flexible in terms of introducing variable parameters or number of parameters.

Until now, we saw:
- positional arguments:
    --> the position of the arguments are determined in the function:
        euler_step(h, v, t, g, dt)
- keyword arguments:
    --> we can define the names and values inside the def of the function or when we call it:

        euler_step(
        h=h,
        v=v,
        t=t,
        g=g,
        dt=dt

    def calculate_dynamic_pressure(rho, velocity, factor=0.5):
        return factor * rho * velocity**2


    When we call the function, if we do not specify factor=0.5, it will take factor=0.5 for internal 
    calculations inside the functions.

    However, if we put:

    calculate_dynamic_pressure(
        1.225,
        50,
        factor=1.0
    )

    Then, it will substitute factor=0.5 to factor=1.0

Now, we are going to see the:
- *args
- **kwargs

Where:

*args    --> tuple
**kwargs --> fictionary

*args does not know how many arguments we will receive, but Python groups them into a tuple
**kwargs does not know how many keyword arguments we will recieve, but Python groups them into a dictionary
    --> The names of the keys inside the dictionary must match with parameters put in def function()

    def initial_energy(h0, v0, g):
        return g * h0 + 0.5 * v0**2
    
    initial_energy(**config)

    Where config has:
        config["h0"],
        config["v0"],
        config["g"]
    
    We can see that the names in the def must match the key in the dictionary of the config:

    "h0" → h0
    "v0" → v0
    "g"  → g

    

We are not goint fo validate data as this exercice is for learn about advanced functions.

'''



############################
#           CODE            
############################


# Import external functions
#---------------------------------------



# Define Internal Functions
#---------------------------------------
def print_simulation_config(**kwargs):
    print(kwargs)


def initial_energy(h0, v0, g = 9.81):

    energy_0 = h0 * g + 0.5 * v0**2

    return energy_0


def average_measurements(*values):

    average = sum(values) / len(values)
    print(f'For values {values} inside the function their type is {type(values)}')

    return average


def simulation_summary(**kwargs):

    for key, value in kwargs.items():

        print(f'''The simulation summary for the values introduced are:
        "{key}" : {value}     
        ''')

    print(f'Confirming that **kwargs is {type(kwargs)}')
    print(f'{kwargs}')


def add(a, b):

    s = a + b

    return s


def multiply(a, b):

    m = a * b

    return m


def apply_operation(operation, x, y):

    op = operation(x, y)

    return op





# Main Calculations
#---------------------------------------

# First approaxes
# Dictionary definition for variables introduced
config = {
    "h0": 0.0,
    "v0": 50.0,
    "g": 9.81
}

print('\n')


# Dictionaries
#---------------------------------------
# Take a look how we can insert a dictionary inside a function
print_simulation_config(h0 = 0, v0 = 50, g = 9.81, dt = 0.1)
print_simulation_config(**config)

# Calculating energy passing a function with:
# - Normal type of arguments or defined.
# - Variable or dynamic entrance of arguments using kwargs
energy_normal_arguments = initial_energy(config["h0"], config["v0"], config["g"])
energy_kwargs_arguments = initial_energy(**config)

print(f'''
    Energy at time 0 passing the arguments of the function normally: {energy_normal_arguments} [J/kg]
    Energy at time 0 passing the arguments as a **kwargs: {energy_kwargs_arguments} [J/kg]
''')



##################################
# EXERCICE
##################################



# BLOCK A: POSITIONAL, KEYWORD & DEFAULT ARGUMENTS
#--------------------------------------
print("\n")
print("BLOCK A: POSITIONAL, KEYWORD & DEFAULT ARGUMENTS:")
print("-------------------------------------------------")


# Call 1: Positional
h0 = 100.0                # This h0 is different to see the g override value as energy depends on it and if it is 0 we will see no difference
v0 = 50.0
g = 9.81
energy_positional_arguments = initial_energy(h0, v0, g)

# Call 2: Keyword
energy_keyword_arguments = initial_energy(h0 = 1.0, v0 = 50.0, g = 9.81)

# Call 3: use default g
energy_default_g = initial_energy(h0, v0)

# Call 4: override default g
energy_override_g = initial_energy(h0, v0, g = 1.62)


# Results
print(f'''
    Call 1: positional arguments --> Result: {energy_positional_arguments} [J/kg]
    Call 2: keyword arguments --> Result: {energy_keyword_arguments} [J/kg]
    Call 3: use default g --> Result: {energy_default_g} [J/kg]
    Call 4: override g with 10 m/s^2 value --> Result: {energy_override_g} [J/kg]
''')




# BLOCK B: *args
#--------------------------------------
print("\n")
print("BLOCK B: *args:")
print("---------------")


# Call 1:
average_1 = average_measurements(10, 20)

# Call 2:
average_2 = average_measurements(10, 20, 30)

# Call 3:
average_3 = average_measurements(10, 20, 30, 40, 50)


# Results
print(f'''\n
    Call 1: values 10, 20 --> Result: {average_1}
    Call 2: values 10, 20, 30 --> Result: {average_2}
    Call 3: values 10, 20, 30, 40, 50 --> Result: {average_3}
''')




# BLOCK C: **kwargs
#--------------------------------------
print("\n")
print("BLOCK C: **kwargs:")
print("------------------")

print('''The simulation summary of:
    maximum altitude of 129.9 m
    flight time of 10.3 s
    final velocity of -51.0 m/s
''')

simulation_summary(
    max_altitude = 129.9,
    flight_time = 10.3,
    final_velocity = -51.0
)




# BLOCK D: Unpacking with *
#--------------------------------------
print("\n")
print("BLOCK D: Unpacking with *:")
print("--------------------------")

measurements = [10.2, 10.5, 9.9, 10.1]

average_of_measurement_list_unpacked = average_measurements(*measurements)

print(f'''
    The measurements introduced:
        {measurements}
    Are unpacked and extracted as a sequences so they are given as positional arguments to obtain:
        {average_of_measurement_list_unpacked}

    In other words, measurements {measurements} are introduced as:
        average_measurements(measurements[0], measurements[1], measurements[2], measurements[3])
    
    In this case, the values inside the tuple can be repeated as it is a sequence of arguments but
    in the form of a tuple
''')




# BLOCK E: Unpacking with **
#--------------------------------------
print("\n")
print("BLOCK E: Unpacking with **:")
print("---------------------------")

config = {
    "h0": 0.0,
    "v0": 50.0,
    "g": 9.81
}

energy_0 = initial_energy(**config)

print(f'''The keys of the dictionary must match the names of the parameters of the function. 
Result: {energy_0} [J/kg]
''')




# BLOCK F: Function as argument
#--------------------------------------
print("\n")
print("BLOCK F: Function as argument:")
print("------------------------------")

print('''We have 2 possible operations to do: adding or multiplying; depending on our interest we will be
applying one or another operation.\n''')

adding_values = apply_operation(add, 5, 3)
multiplying_values = apply_operation(multiply, 5, 3)

print(f'''We do not put the () inside the call of the function as we are only passing it, not executing it:
apply_opertaion(add, x, y)
Because the execution of it will be with x and y

Adding result: {adding_values}
Multiplying result: {multiplying_values}
''')




# FINAL VALIDATION
#-------------------------------------------------
'''
Explain:
- Difference between positional and keyword arguments?
+ The positional arguments are passed as they are defined previously by variable/s: assigned by order.
+ The keyword arguments are passed inside the function call and assigned and they can override
the default values.
+ If mixed, positional arguments must be first.

- What a default argument does?
+ It is not needed to pass when calling the function as it is used internally in it when called.

- What *args receives and its type?
+ It receives multiple values and they are collected as a tuple

- What **kwargs receives and its type?
+ It receives a dictionary which keys must match the funtion definition arguments, it is a dict type

- Difference between * when defining and * when calling?
+ When we define, with * we are telling the function that it will receive multiple values with
variable size: it can be 2 values, 3 values or 100 values. The arguments are grouped inside the
function as a tuple.
+ When calling, we are telling the function that effectively it will receive multiple values that
can be as a sequence or as a list. It has to unpack those values as positional arguments and make
the tuple when we are inside the def function.

- Difference between ** when defining and ** when calling?
+ When we define, with ** we are telling the function that it will receive variables in the form of
key : value
+ When calling, with ** we are telling the function that the pairs that it will receive will be 
defining the dictionary generated and the names of the keys and internal variables must match. It has
to unpack those values as a dictionary

- Why apply_operation(add, 5, 3) passes add without ()
+ Because we are passing the function and not executing it

'''