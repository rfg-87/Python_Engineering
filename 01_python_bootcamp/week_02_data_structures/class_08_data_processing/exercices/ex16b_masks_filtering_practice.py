'''
The main goal of this exercice is to get more comfortable with the numpy and np.array matrix
boolean masks and filter of the arrays.

It is linked to the PDFs:

"Python_Engineering_Class08_Data_Processing_EX16b_ES.pdf"
"Python_Engineering_Class08_Data_Processing_EX16b_EN.pdf"

Where we have the instructions

'''

# Import external functions
#--------------------------------------
import numpy as np


# Array creation
#--------------------------------------
# columns:
# time, altitude, velocity, temperature]
sensor_data = np.array([
    [0.0,  20.0,  30.0, 18.0],
    [1.0,  55.0,  25.0, 17.0],
    [2.0,  90.0,  18.0, 15.0],
    [3.0, 120.0,  10.0, 13.0],
    [4.0, 140.0,   2.0, 11.0],
    [5.0, 138.0,  -6.0, 10.0],
    [6.0, 115.0, -15.0, 12.0],
    [7.0,  80.0, -22.0, 14.0],
    [8.0,  40.0, -28.0, 16.0]
])




# BLOCK A: EXTRACT COLUMNS
#--------------------------------------
'''
Extract columns of the sensor data and print the shape of every extracted vector.

'''

print("\n")
print("BLOCK A: EXTRACT COLUMNS:")
print("-------------------------")

times = sensor_data[:, 0]
altitudes = sensor_data[:, 1]
velocities = sensor_data[:, 2]
temperatures = sensor_data[:, 3]

print(f'''
    The shape of the time is: {times.shape}.
    The shape of the altitude is: {altitudes.shape}.
    The shape of the velocity is: {velocities.shape}.
    The shape of the temperature is: {temperatures.shape}.
    \n''')

# Predictions:
# - time shape: (9, )
# - altitude shape: (9, )
# - velocity shape: (9, )
# - Temperature shape: (9, )




# BLOCK B: SIMPLE MASKS
#--------------------------------------
'''
Create masks for:
- altitude >= 100 m
- velocity > 0 m/s
- velocity < 0 m/s
- temperature < 15 ºC

For each mask print:
- Number of True
- Indexes

'''

print("\n")
print("BLOCK B: SIMPLE MASKS:")
print("----------------------")

# Mask creation and definition
altitude_equal_above_100 = altitudes >= 100
velocity_positive = velocities > 0
velocity_negative = velocities < 0
temperature_below_15 = temperatures < 15

print(f'''
    The number of times sensor altitude is above 100 m is: {np.sum(altitude_equal_above_100)} which indexes are:
    {np.where(altitude_equal_above_100)[0]}.
    The number of times sensor velocity is above 0 m/s is: {np.sum(velocity_positive)} which indexes are:
    {np.where(velocity_positive)[0]}.
    The number of times sensor velocity is below 0 m/s is: {np.sum(velocity_negative)} which indexes are:
    {np.where(velocity_negative)[0]}.
    The number of times sensor temperature is below 15 ºC is: {np.sum(temperature_below_15)} which indexes are:
    {np.where(temperature_below_15)[0]}.
    \n''')

# Predictions:
# - altitude >= 100 m   :   4   :   [3, 4, 5, 6]  
# - velocity > 0 m/s    :   5   :   [0, 1, 2, 3, 4]
# - velocity < 0 m/s    :   4   :   [5, 6, 7, 8]
# - temperature < 15 ºC :   5   :   [3, 4, 5, 6, 7]




# BLOCK C: FILTER VALUES VS ROWS
#--------------------------------------
'''
Using the altitude mask, filter:
- Altitude values.
- Altitude states.

To filter values above 100 m.

'''

print("\n")
print("BLOCK C: FILTER VALUES VS ROWS:")
print("-------------------------------")

# The altitude values are filtered through the altitudes and its mask: altitudes[mask].
# The altitude states are filtered thorugh the data and masked: sensor_data[mask].
high_altitude_values = altitudes[altitude_equal_above_100]
high_altitude_states = sensor_data[altitude_equal_above_100]

print(f'''
    The altitudes above 100 m are: {high_altitude_values}.
    The states for altitudes above 100 m are:
    {high_altitude_states}.
''')

# Predictions
# - altitudes: [120.0, 140.0, 138.0, 115.0]
# - states:    [[3.0, 120.0, 10.0, 13.0],
#              [4.0, 140.0, 2.0, 11.0],
#              [5.0, 138.0, -6.0, 10.0],
#              [6.0, 115.0, -15.0, 12.0]]




# BLOCK D: COMBINING CONDITIONS
#--------------------------------------
'''
Create and filter:
- Altitude >= 100 AND velocity > 0.
- Altitude >= 100 OR temperature < 12.
- NOT asceding.
- Time between 2 and 6 seconds inclusive.

'''

print("\n")
print("BLOCK D: COMBINING CONDITIONS:")
print("------------------------------")

# Creating filters/masks
altitude_velocity_window = ( (altitudes >= 100) & (velocities > 0) )
altitude_temperature_window = ( (altitudes >= 100) | (temperatures < 12) )
not_ascending = ~(velocities > 0)
time_window = ( (times >= 2) & (times <= 6) )

altitude_velocity_data = sensor_data[altitude_velocity_window]
altitude_temperature_data = sensor_data[altitude_temperature_window]
not_ascending_data = sensor_data[not_ascending]
time_filtered_data = sensor_data[time_window]

print(f'''
    For altitude >= 100 AND velocity > 0 the states are:
    {altitude_velocity_data}
    For altitude >= 100 OR temperature < 12 the states are:
    {altitude_temperature_data}
    For the condition of NOT ascending, the states are:
    {not_ascending_data}
    For the time between 2 seconds and 6 seconds (included), the states are:
    {time_filtered_data}
''')




# BLOCK E: STATISTIC FILTERED SUMMARY
#--------------------------------------
'''
For states with altitude >= 100 m:
- mean altitude
- std altitude
- mean velocity
- minimum temperature

'''

print("\n")
print("BLOCK E: STATISTIC FILTERED SUMMARY:")
print("------------------------------------")

mean_altitude_altitude_above_100 = np.mean(high_altitude_values)
std_dev_altitude_altitude_above_100 = np.std(high_altitude_values)

mean_velocity_altitude_above_100 = np.mean(high_altitude_states[:, 2])

minimum_temperature = np.min(high_altitude_states[:, 3])
# Alternatively:
# minimum_temperature = np.min(high_altitude_states, axis=0)[3]


print(f'''
    The mean altitude above 100 m is: {mean_altitude_altitude_above_100:.2f} m
    The standard deviation above 100 m is: {std_dev_altitude_altitude_above_100:.2f} m
    The mean velocity above 100 m is: {mean_velocity_altitude_above_100:.2f} m/s
    The minimum temperature above 100 m is: {minimum_temperature:.2f} ºC
''')




# BLOCK F: DERIVED VARIABLE ADDED COLUMN
#--------------------------------------
'''
Add a column with the speed (absolute value of velocity). Call the new dataset (ds)
as processed_data.

np.abs() returns the absolute value of a number/array element by element

'''

print("\n")
print("BLOCK F: DERIVED VARIABLE ADDED COLUMN:")
print("---------------------------------------")

# We have to let the new df as [time, altitude, velocity, temperature, speed]
speed = np.abs(velocities)

processed_data = np.column_stack((
    sensor_data,
    speed
))

print(f'''
    The new dataset (ds) called processed_data has the speed column added:
    {processed_data}
''')




# BLOCK G: SAMPLING TIME
#--------------------------------------
'''
Compare the time of the samples with regards 1.0 of general sampling time.

np.diff() returns the difference between each sample in the sensor_data dataset.
np.allclose() returns True/False sentence compared to a reference value with some tolerance.

'''

print("\n")
print("BLOCK G: SAMPLING TIME:")
print("-----------------------")

dt_samples_diff = np.diff(times)

reference_dt = 1.0
dt_samples_allclose = np.allclose(dt_samples_diff, reference_dt)

print(f'''
    The difference of times between samples is of (list):
    {dt_samples_diff}
    Are the samples taken around 1.0 second?
    {"YES" if dt_samples_allclose else "NO"}
''')




# BLOCK H: BONUS: np.any() and np.all()
#--------------------------------------
'''
Using these new functions, return the value for:
- If any altitude is above 130 m
- If all the values of the temperature are above 0.0 ºC


'''

print("\n")
print("BLOCK H: BONUS: np.any() and np.all():")
print("--------------------------------------")

altitude_above_130 = altitudes > 130
any_altitude_above_130 = np.any(altitude_above_130)

temperatures_above_zero = temperatures > 0
all_temperatures_above_zero = np.all(temperatures_above_zero)

print(f'''
    Is there any altitude above 130 m?
    {"YES" if any_altitude_above_130 else "NO"}
    Are all the temperatures above 0.0 ºC?
    {"YES" if all_temperatures_above_zero else "NO"}
''')




# FINAL VALIDATION
#-------------------------------------------------
'''
Explain:
- Difference between x[mask] and A[mask]?
+ x[mask] returns the filtered values of a 1D array as the mask contains the True/False.
+ A[mask] returns the filtered rows of a 2D (or more) array.

- Difference between np.sum(mask) and np.where(mask)[0]?
+ np.sum(mask) gives us the total number of times that the mask is fulfilled in the data (some of total True)
+ np.where(mask)[0] gives us the position where the mask is fulfilled in the data

- Difference between & and |?
+ & is the AND operator for masks when considering ranges or different conditions that must be fulfilled completely
+ | is the OR operator for masks when considering options to be fulfilled, only one needs to be fulfilled

- What ~mask does?
+ It makes the NOT operator for a mask

- What np.any() returns?
+ Returns True if any or one of the values inside the function the mask condition

- What np.all() returns?
+ Returns True if all of the values inside the function fulfills the mask condition

- Why np.diff(times) has one element less than times?
+ Because it is considering the difference with two subsequent times (k) to (k+1) that is why
  the first is taken as reference: so there are N-1 intervals instead of N 

'''