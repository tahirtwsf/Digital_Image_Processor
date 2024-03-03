#P5 Edge Detection Test
#L1-12 
#Submitted on November 22, 2019

from Cimpl import *
from L1_12_P5_edge import *

def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.

    Parameter description should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.

    Parameters outcome and expected are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:

        # The format method is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.

        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")

    
def test_edge():
    """Author: Tahir Towsif
    Tests whether the edge detection filter works as required. 
    
    >>>test_edge()
    
    (0,0) PASSED
    ------
    (1,0) PASSED
    ------
    (2,0) PASSED
    ------
    (3,0) PASSED
    ------
    """
    
    threshold = 45 #The test threshold is set to 45.
    
    original_image = create_image(4,4)
    set_color(original_image, 0,0, create_color(206, 164, 185))
    set_color(original_image, 1,0, create_color(145, 34, 156)) 
    set_color(original_image, 2,0, create_color(267, 240, 99)) 
    set_color(original_image, 3,0, create_color(94, 167, 116))
    set_color(original_image, 0,1, create_color(256, 223, 206))
    set_color(original_image, 1,1, create_color(100, 89, 76))
    set_color(original_image, 2,1, create_color(55, 179, 87))
    set_color(original_image, 3,1, create_color(255, 33, 1)) 
    set_color(original_image, 0,2, create_color(7, 55, 100))
    set_color(original_image, 1,2, create_color(5, 5, 5))
    set_color(original_image, 2,2, create_color(17, 18, 19))
    set_color(original_image, 3,2, create_color(15, 155, 200))
    set_color(original_image, 0,3, create_color(14, 17, 16))
    set_color(original_image, 1,3, create_color(156, 247, 32))
    set_color(original_image, 2,3, create_color(76, 56, 67))
    set_color(original_image, 3,3, create_color(23, 67, 100))
    
    edited_image = create_image(4,4)    
    set_color(edited_image, 0,0, create_color(255, 255, 255))
    set_color(edited_image, 1,0, create_color(255, 255, 255)) 
    set_color(edited_image, 2,0, create_color(0, 0, 0)) 
    set_color(edited_image, 3,0, create_color(255, 255, 255))
    set_color(edited_image, 0,1, create_color(0, 0, 0))
    set_color(edited_image, 1,1, create_color(0, 0, 0))
    set_color(edited_image, 2,1, create_color(0, 0, 0))
    set_color(edited_image, 3,1, create_color(255, 255, 255)) 
    set_color(edited_image, 0,2, create_color(255, 255, 255))
    set_color(edited_image, 1,2, create_color(0, 0, 0))
    set_color(edited_image, 2,2, create_color(0, 0, 0))
    set_color(edited_image, 3,2, create_color(0, 0, 0))
    set_color(edited_image, 0,3, create_color(14, 17, 16))    #The last row of the image 
    set_color(edited_image, 1,3, create_color(156, 247, 32))  #stays the same because the 
    set_color(edited_image, 2,3, create_color(76, 56, 67))    #filter does not run through the
    set_color(edited_image, 3,3, create_color(23, 67, 100))   #last row. 
    
    edge_detection = detect_edges(original_image, threshold)
    
    for x, y, col in edge_detection:
    
            check_equal('(' + str(x) + ',' + str(y) + ')', col, get_color(edited_image, x, y)) 

