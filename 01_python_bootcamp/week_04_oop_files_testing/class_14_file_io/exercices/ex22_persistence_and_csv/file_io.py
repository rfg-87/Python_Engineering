'''
This is a new class in which we are going to use the I/O concept: Input/Ouput.

This is the module where we are going to define the functions to write the CSV and also read it

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



# Define Internal Functions
#---------------------------------------
# BLOCK D: Save CSV
#--------------------------------------
'''
We are going to define the functions to save and load CSV

'''

def save_trajectory_csv(file_path, trajectory):

    '''
    Function to open the CSV file where we have stablished in main.py with 'w' write conditions:
    it writes the files or overwrites what it has done before and encoding it as utf-8 (it is an
    standard format for CSV)

    For more information see 'Python_Engineering_Class14_File_IO_Reference_Guide_EN.pdf'

    with creates a context manager. When exit the block, Python closes the file even when we 
    abandon the block. It avoid that we forget the file.close():

        enter with block -> open resource
        inside block -> use resource
        leave block -> close/release resource

    We put the \n to make a line jump, if not all the data will be glued one continued the other.

    The CSV is a text file, so when coming back and reading it we have to format it back with float
    or the type of data that we saved.

    '''

    with open(file_path, 'w', encoding = 'utf-8') as file:

        file.write('h_m, v_m/s, t_s\n')

        for row in trajectory:

            h = row[0]

            v = row[1]

            t = row[2]

            file.write(f'{h:.6f}, {v:.6f}, {t:.6f}\n')


# BLOCK F: Load CSV
#--------------------------------------
'''
We are going to define a function to load the data from a CSV

'''

def load_trajectory_csv(file_path):

    '''
    Function to open the CSV.

    We define a first np.array of shape (0, 3): an empty array that will receive 3 variables: h, v, t

    What we do is format back the CSV. We can do it returning it as a list or as directly an np.array

    We omit the header reading a line and not using that variable.

    Then, we enter in a loop going through every line in the CSV file

    We use the strip() to clean of spaces in the limits of the data and line jumps. Also, if we see that a line is in
    blank '' we continue with the next line in the for loop.

    Then, we extract the values as a list with the split() method. Inside the () we put the separator
    that Python will consider to separate the data. In this case, a comma ','

    As the variable values is a list[] we have to select the indexes corresponding to each variable

    Then, we stack vertically every 1D array to increase the matrix

    '''

    rows = np.empty( (0,3) )

    with open(file_path, 'r', encoding='utf-8') as file:

        header = file.readline()

        for line in file:

            clean_line = line.strip()               # Returns a new string without empty spaces and line jumps \n

            if clean_line == '':
                continue

            values = clean_line.split(',')          # Separates values as a list [] considering each index separated by a comma ','

            h = float(values[0])
            v = float(values[1])
            t = float(values[2])

            new_row = np.array([h, v, t])
            rows = np.vstack( (rows, new_row) )

    return rows


# BLOCK H: Practice mode append 'a' inside with
#--------------------------------------
'''
We are going to use a log file to save a summary of each execution without deleting the previous data

'''
def append_run_log(file_path, message):

    with open(file_path, 'a', encoding = 'utf-8') as file:

        file.write(message + '\n') 