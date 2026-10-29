'''
This is a new class in which we are going to use the I/O concept: Input/Ouput.

This is the module where we are going to define the functions to write the CSV and also read it.

In addition, we are going to generate 2 CSV files:
    1. OK
    2. Corrupted

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
# BLOCK 0: Generate reference files
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

            file.write(f'{h}, ' if isinstance(h, str) else f'{h:.6f}, ')    # We put the comma after each sentence of the if
            file.write(f'{v}, ' if isinstance(v, str) else f'{v:.6f}, ') 
            file.write(f'{t}\n' if isinstance(t, str) else f'{t:.6f}\n')
            # Alternatively
            # file.write(
            #     (f'{h}' if isinstance(h, str) else f'{h:.6f}')
            #     + ', '
            # )

            # h_text = h if isinstance(h, str) else f'{h:.6f}'
            # v_text = v if isinstance(v, str) else f'{v:.6f}'
            # t_text = t if isinstance(t, str) else f'{t:.6f}'

            # Alternatively 2
            # file.write(
            #     f'{h_text},{v_text},{t_text}\n'
            # )


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

    rows = []

    with open(file_path, 'r', encoding = 'utf-8') as file:

        header = file.readline().strip()

        if header != 'h_m, v_m/s, t_s':

            raise ValueError('Invalid CSV header')



        # BLOCK C: enumerate(..., start = 2)
        #--------------------------------------
        for line_number, line in enumerate(file, start = 2):        # We put start = 2 to start counter in the natural line 2 of the file as header would be line 1
                                                                    # So, when we as human or naturally count the first line as line 1, the line 2 will be the first
            clean_line = line.strip()                               # with values. 
                                                                    # enumerate(items) generate a tupple as (index, item)
            if clean_line == '':
                continue

            values = clean_line.split(',')                          # Remember: It reads the values as string


            # BLOCK B: raise ValueError(...)
            #--------------------------------------
            if len(values) != 3:                                    # Error not only for failing in Python if not to fulfill a format rule that we want.

                raise ValueError(f'Line {line_number}: expected 3 columns')     # Raises deliverately an exception

            h = float(values[0])
            v = float(values[1])
            t = float(values[2])

            rows.append( [h, v, t] )

    return np.array(rows) 