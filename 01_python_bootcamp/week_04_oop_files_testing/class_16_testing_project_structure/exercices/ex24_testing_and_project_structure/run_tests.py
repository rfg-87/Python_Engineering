# BLOCK G: Generate our own test runner
#--------------------------------------
'''
From here we are going to call the test functions and modules generated in the folder tests/

and then evaluate if the test has been passed or not

'''



############################
#           CODE            
############################

##################################
# EXERCICE
##################################

# Import external functions
#---------------------------------------



# Import Internal Functions
#---------------------------------------
from tests.test_vertical_state import test_initial_state, test_euler_step
from tests.test_file_io import test_csv_round_trip, test_missing_file_raises



# Define Internal Functions
#---------------------------------------

TESTS = [
    test_initial_state,
    test_euler_step,
    test_csv_round_trip,
    test_missing_file_raises
]

def main():

    passed = 0
    failed = 0
    errors = 0

    print('\n')

    for test in TESTS:

        try:

            test()

        except AssertionError as error:

            failed += 1
            print(f'FAIL {test.__name__}')
            print(f'     {type(error).__name__}: {error}')

        except Exception as error:              # We want to avoid to stop test and we label it as an error (we are not hiding it)

            errors += 1
            print(f'ERROR {test.__name__}')
            print(f'      {type(error).__name__}: {error}')

        else:

            passed += 1
            print(f'PASS {test.__name__}')

    print('\n')
    print('SUMMARY:')
    print('--------')
    print(f'Passed: {passed}')
    print(f'Failed: {failed}')
    print(f'Errors: {errors}')
    print('\n')


# Main BLOCK
if __name__ == '__main__':
    main()