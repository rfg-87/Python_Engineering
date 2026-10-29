'''
In this exercice we are going to generate a reusable mathematical module for engineering in which
we will have the next modules:

- main
- engineering_toolkit
    + vector_norm()
    + unit_vector()
    + angle_between_vectors()
    + project_vector()
    + rotation_matrix_2d_angle()
    + rotate_2d_vector()
    + check_rotation_matrix()

main.py module will only:

define data
      ↓
call toolkit
      ↓
show resuls   

'''



############################
#           CODE            
############################


# Import external functions
#---------------------------------------
import numpy as np



# Import external functions
#---------------------------------------



# Define Internal Functions
#---------------------------------------
def vector_norm(vector):

    '''
    This function calculates the norm of a vector.

    INPUTS:
    - vector

    OUTPUTS:
    - norm

    '''

    norm = np.linalg.norm(vector)

    return norm


def unit_vector(vector):

    '''
    This function calculates the unitary vector of a vector.

    INPUTS:
    - vector

    OUTPUTS:
    - unitary_vector
        
    '''

    norm = vector_norm(vector)

    # Check for the norm different to 0.0
    if np.isclose(norm, 0.0):
        return None

    unitary_vector = vector / norm

    return unitary_vector


def angle_between_vectors(vector_1, vector_2):

    '''
    This function calculates the angle (theta) between two vectors. 
    Returns the angle in radians.

    INPUTS:
    - vector_1
    - vector_2

    OUTPUTS:
    - theta: angle between vectors in [rad]
    
    '''

    # Calculation of the numerator
    dot_product = np.dot(vector_1, vector_2)

    # Calculation of the denominator
    norm_vector_1 = vector_norm(vector_1)
    norm_vector_2 = vector_norm(vector_2)

    norm_products = norm_vector_1 * norm_vector_2

    # Check if norm if zero: the operation cannot be done
    if np.isclose(norm_products, 0.0):
        return None

    # Angle calculation: Limiting the limits of cosinus because of floating decimals that can lead to 1.00000000007
    cos_theta = dot_product / norm_products
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    theta = np.arccos(cos_theta)    

    return theta


def project_vector(vector, projection_direction):

    '''
    This function calculates the projection of a vector into a direction. 
    It scales the vector into the direction.
    
    INPUTS:
    - vector
    - projection_direction: direction of projection

    OUTPUTS:
    - projected_vector: vector projected in the direction

    '''

    # Calculation of the numerator
    dot_product_numerator = np.dot(vector, projection_direction)

    # Calculation of the denominator
    dot_product_denominator = np.dot(projection_direction, projection_direction)

    # Check if denominator is zero
    if np.isclose(dot_product_denominator, 0.0):
        return None
    
    # Calculation of the vector projected in the direction
    projected_vector = (dot_product_numerator / dot_product_denominator) * projection_direction

    return projected_vector


def rotation_matrix_2d_angle(angle_deg):

    '''
    This function defines the rotation matrix.
    
    INPUTS:
    - angle_deg: angle in degrees rotation

    OUTPUTS:
    - R :rotation matrix

    '''

    theta = np.deg2rad(angle_deg)

    R = np.array([
        [np.cos(theta), - np.sin(theta)],
        [np.sin(theta),   np.cos(theta)]
    ])

    return R


def rotate_2d_vector(vector, angle_deg):

    '''
    This function rotates a vector with a rotation matrix: calling the function 
    rotation_matrix_2d_angle.
    
    INPUTS:
    - vector   : vector to rotate
    - angle_deg: angle in degrees rotation

    OUTPUTS:
    - rotated_vector : it gives the rotated vector from the original

    '''

    R = rotation_matrix_2d_angle(angle_deg)

    rotated_vector = R @ vector

    return rotated_vector


def check_rotation_matrix(R):

    '''
    This function checks that the rotation matrix is a .
    
    INPUTS:
    - vector   : vector to rotate
    - angle_deg: angle in degrees rotation

    OUTPUTS:
    - rotated_vector : it gives the rotated vector from the original

    '''

    # Identity matrix definition
    number_dimensions_R = R.shape[0]

    I = np.eye(number_dimensions_R)

    # Check ortogonality
    orthogonal = np.allclose(R.T @ R, I)

    # Calculate determinant
    determinant = np.linalg.det(R)

    # Check if the rotation is ok: Boolean
    proper_rotation = orthogonal and np.allclose(determinant, 1.0)

    matrix_check_dictionary = {
        "orthogonal": orthogonal,
        "determinant": determinant,
        "proper_rotation": proper_rotation
    }

    return matrix_check_dictionary





##################################
# EXERCICE
##################################

'''
The main point of the exercice is to return the value of the funtions
'''

# BLOCK A: Norm of a vector
#--------------------------------------

# BLOCK B: Unitary vector
#--------------------------------------

# BLOCK C: Angle between vectors
#--------------------------------------

# BLOCK D: Project vector
#--------------------------------------

# BLOCK E: Reuse rotation matrix of ex19
#--------------------------------------

# BLOCK F: Check rotation matrix properties
#--------------------------------------