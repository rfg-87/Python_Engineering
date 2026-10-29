'''
In this exercice we are going to generate a reusable mathematical module for engineering in which
we will have the next modules:

- main
- engineering_toolkit
    + vector_norm()
    + unit_vector()
    + angle_between_vectors()
    + project_vector()
    + rotation_matrix_2d_angle
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
from engineering_toolkit import (vector_norm, unit_vector, angle_between_vectors, project_vector,
                                 rotation_matrix_2d_angle, rotate_2d_vector, check_rotation_matrix)


# Define Internal Functions
#---------------------------------------
def main():
    
    norm_of_vector = vector_norm(v1)

    unitary_vector = unit_vector(v1)

    angle_v1_v2 = angle_between_vectors(v1, v_direction)            # In rad

    projected_vector_v1_over_v2 = project_vector(v1, v_direction)

    R = rotation_matrix_2d_angle(angle_deg)

    rotated_vector = rotate_2d_vector(np.array([100.0, 0]), 90.0)

    dict_check_rot_matrix = check_rotation_matrix(R)


    np.set_printoptions(formatter = {'float': '{:0.2f}'.format})
    print(f'''
        The norm of the vector v1 {v1} is: {norm_of_vector}.
        The unitary vector of v1 {v1} is: {unitary_vector}.
        The angle between v1 {v1} and v_direction {v_direction} is: {np.rad2deg(angle_v1_v2):.2f}º.
        The projected vector v1 {v1} over the direction {v_direction} is: {projected_vector_v1_over_v2}.
        The rotation matrix at {angle_deg}º is:
        {R}
        A general vector {np.array([100.0, 0])} rotated {90.0}º gives: {rotated_vector}.
        The checks for the rotation matrix are the next:''')

    for key, value in dict_check_rot_matrix.items():

        print(f'''              {key} : {value}''')





# Main Calculations
#---------------------------------------
# Reference values
v1 = np.array([3.0, 4.0])
v_direction = np.array([1.0, 0.0])
angle_deg = 30.0



##################################
# EXERCICE
##################################

# BLOCK G: Define main module
#--------------------------------------
if __name__ == "__main__":
    main()




# FINAL VALIDATION
#-------------------------------------------------
'''
Explain:
- What does vector_norm() represent physically/geometrically?
+ It calculates the magnitude (or length) of the vector.

- Why does unit_vector() fail for the zero vector?
+ Because the unitary vector is calculated dividing by the norm, if it is zero, it cannot be computed.

- What does np.dot(v1, v2) represent?
+ It is the dot product between two vectors.

- Why does the angle formula divide by both vector norms?
+ Because it is calculated over the unitary vectors between them.

- Why do we use np.clip() before np.arccos()?
+ To limit the values of a known function [-1.0, 1.0] as the floating round can go above those limits.

- What does np.arccos() receive and return?
+ It receives a value and returns an angle in radians.

- What is the difference between a vector and its projection onto another direction?
+ The projection is how much of that vector is projected in that direction.

- Why does check_rotation_matrix() test both R.T @ R = I and det(R) = 1?
+ Because it is an orthogonal and to discard a reflexion that can also be orthogonal but with det(R) = -1
Reflexion: it inverts a vector to another side of a line or a plane (like a mirror). For example:
reflexion over X axes:
[
[1,  0],
[0, -1]
]

- Why is returning a dictionary useful in check_rotation_matrix()?
+ Because we can have a descriptive name for the checks: linking algebra and dictionary.

- What advantages do we gain by putting these tools in engineering_toolkit.py?
+ Because they can be reused. These operations appear repeatedly and using this module we can
avoid duplicating formulas, reduce errors and validate every tool before using in other physical
phenomena.

'''