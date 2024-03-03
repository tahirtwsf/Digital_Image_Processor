from Cimpl import choose_file, load_image, copy, create_color, create_image, set_color,\
                  show, Image, get_color, get_width, get_height
from L1_12_image_filters import two_tone, three_tone, sepia, posterize, extreme_contrast, \
     flip_horizontal, flip_vertical, detect_edges, detect_edges_better


# P4 Refactored Tests

def test_two_tone()->None:
    """ Author: Tahir Towsif
    Tests if the two tone filter works as intended.
    
    >>> orig = load_image("riveter.jpg")
    >>> test_two_tone()
    Color 1: (input color)
    Color 2: (input color)
    Pixels passed: (no. of pixels passed)
    Pixels failed: (no. of pixels failed)
    """
    passed = 0
    failed = 0
    color_1 = input("Color 1:")
    color_2 = input("Color 2:")
    test_img = copy(two_tone(orig, color_1, color_2))
    
    
    colors = [color_1, color_2]
    
    rgb = []
    
    for i in range(len(colors)):
        if colors[i] == "black":
            rgb += (0, 0, 0)
            
        if colors[i] == "white":
            rgb += (255, 255, 255)
            
        if colors[i] == "red":
            rgb += (255, 0, 0)
            
        if colors[i] == "lime":
            rgb += (0, 255, 0)
            
        if colors[i] == "blue":
            rgb += (0, 0, 255)
        
        if colors[i] == "yellow":
            rgb += (255, 255, 0)
            
        if colors[i] == "cyan":
            rgb += (0, 255, 255)
            
        if colors[i] == "magenta":
            rgb += (255, 0, 255)
            
        if colors[i] == "gray":
            rgb += (128, 128, 128)
            
    color_1 = create_color(rgb[0], rgb[1], rgb[2])
    color_2 = create_color(rgb[3], rgb[4], rgb[5])
    
    for x,y, (r, g, b) in test_img:
        if color_1 == get_color(test_img, x, y) or color_2 == get_color(test_img, x, y):
            passed +=1
        else: 
            failed +=1
            
    print("Pixels passed:", passed)
    print("Pixels failed:", failed)

def test_three_tone() -> None:
    """Author: Tahir Towsif
    Tests if the three tone filter works as intended
    
    >>> orig = load_image("riveter.jpg")
    >>> test_three_tone()
    Color 1: (input color)
    Color 2: (input color)
    Color 3: (input color)
    Pixels passed: (no. of pixels passed)
    Pixels failed: (no. of pixels failed)
    """
    passed = 0
    failed = 0
    color_1 = input("Color 1:")
    color_2 = input("Color 2:")
    color_3 = input("Color 3:")
    test_img = copy(three_tone(orig, color_1, color_2, color_3))
    colors = [color_1, color_2, color_3]
    rgb = []
    
    for i in range(len(colors)):
        if colors[i] == "black":
            rgb += (0, 0, 0)
            
        if colors[i] == "white":
            rgb += (255, 255, 255)
            
        if colors[i] == "red":
            rgb += (255, 0, 0)
            
        if colors[i] == "lime":
            rgb += (0, 255, 0)
            
        if colors[i] == "blue":
            rgb += (0, 0, 255)
        
        if colors[i] == "yellow":
            rgb += (255, 255, 0)
            
        if colors[i] == "cyan":
            rgb += (0, 255, 255)
            
        if colors[i] == "magenta":
            rgb += (255, 0, 255)
            
        if colors[i] == "gray":
            rgb += (128, 128, 128)
            
    color_1 = create_color(rgb[0], rgb[1], rgb[2])
    color_2 = create_color(rgb[3], rgb[4], rgb[5])
    color_3 = create_color(rgb[6], rgb[7], rgb[8])
    
    for x,y, (r, g, b) in test_img:
        if color_1 == get_color(test_img, x, y) or color_2 == get_color(test_img, x, y) or color_3 == get_color(test_img, x, y):
            passed +=1
            
        else: 
            failed +=1
            
    print("Pixels passed:", passed)
    print("Pixels failed:", failed)    
    
def test_sepia()->None:
    """ Author: Tahir Towsif
    Tests the function speia with 3 test scenarios.
    Prints the actual filter rgb values and the expected rgb values.
    
    >>>test_sepia()
    """
    image=create_image(3,1)
    set_color(image, 0, 0, create_color(60,60,60))     # If pixels are Less than 63
    set_color(image, 1, 0, create_color(91,91,91))     # If pixels are between 63 and 191
    set_color(image, 2, 0, create_color(207,207,207))  # If pixels are greater than 191
    
    new_image=sepia(image)
    
    actual_color=get_color(new_image, 0, 0)
    expected_color=create_color(60*1.1, 60, 60*0.9)
    print("Actual:  ", actual_color)
    print("Expected:", expected_color,)
    print()
    
    actual_color=get_color(new_image, 1, 0)
    expected_color=create_color(91*1.15, 91, 91*0.85)
    print("Actual:  ", actual_color)
    print("Expected:", expected_color,)
    print()
    
    actual_color=get_color(new_image, 2, 0)
    expected_color=create_color(207*1.08, 207, 207*0.93)
    print("Acutal:  ", actual_color)
    print("Expected:", expected_color,)
    print()

def adjust_test_posterize() -> None:
    """
    Author: Tahir Towsif
    Fucntion will test weather or not a image has been posterized by determining if the values are 31, 95, 159, or 223, if they are not then the picture is not posterized.
    >>>adjust_test_posterize()
    FAIL: Pixel @ x = 0 y = 0 r = 29 g = 37 b = 223
    FAIL: Pixel @ x = 1 y = 0 r = 30 g = 159 b = 223
    PASS: Pixel @ x = 2 y = 0 r = 31 g = 159 b = 223
    """
    image = create_image(3, 1, )
    set_color(image, 0, 0, create_color(29,37,223)) #Should fail test 
    set_color(image, 1, 0, create_color(30,159,223)) #Should fail test 
    set_color(image, 2, 0, create_color(31,159,223)) #Should pass test 
     
    for x, y, (r,g,b) in image:
        r, g, b = get_color(image, x, y)
        if r ==  (31 or 95 or 159 or 223) or g == (31 or 95 or 159 or 223) or b ==   (31 or 95 or 159 or 223):
            print('PASS: Pixel @ x =', x, 'y =', y, 'r =', r, 'g =', g, 'b =', b,)
        else: 
            print('FAIL: Pixel @ x =', x, 'y =', y, 'r =', r, 'g =', g, 'b =', b,)
    
def test_posterize() -> None:
    """
    Author: Tahir Towsif
    Function will test weather an image has been posterized correctly. The function will take original rgb values and compare them with their value after having been posterized. If the correct numbvers are returned (31 or 95 or 159 or 223 then the iamge is posterized, however if not then it has not been psoterized.
    """
    original_image=create_image(3,1)
    set_color(original_image, 0, 0, (255,200,100))
    set_color(original_image, 1, 0, (10,30,45))
    set_color(original_image, 2, 0, (0,10,180))
    posterized = posterize(original_image)
    wrong = 0 
    for x, y, rgb in original_image:
        for i in range(3):
            if rgb[i] <= 63:
                test = 31
            elif 63 < rgb[i] <= 127:
                test = 95
            elif 127 < rgb[i] <= 191:
                test = 159
            else:
                test = 223
            if get_color(posterized, x, y, )[i] !=test:
                wrong += 1
        if wrong != 0:
            print('Test Failed')
        if wrong == 0:
            print('Test passed')

def extreme_test() -> None:
    """Author: Tahir Towsif
    Checks whether the components of each pixel are set at their minimum (0) and 
    maximum (255) values after being edited by the extreme_contrast filter function.
    
    >>>extreme_test()
    """
    # Creates an image that is 8 pixels in length and 1 pixel in width.
    # Each pixel will test for each possible colour.
    image = create_image(8, 1, )
    set_color(image, 0, 0, color=create_color(50, 25, 50))     # Changes to Black
    set_color(image, 1, 0, color=create_color(230, 250, 175))  # Changes to White
    set_color(image, 2, 0, color=create_color(250, 0, 20))     # Changes to Red
    set_color(image, 3, 0, color=create_color(40, 230, 120))   # Changes to Lime
    set_color(image, 4, 0, color=create_color(50, 30, 240))    # Changes to Blue
    set_color(image, 5, 0, color=create_color(230, 200, 30))   # Changes to Yellow
    set_color(image, 6, 0, color=create_color(10, 255, 230))   # Changes to Cyan
    set_color(image, 7, 0, color=create_color(20, 195, 2))     # Changes to Magenta

    test_image = extreme_contrast(image)

    for x, y, (r, g, b) in test_image:
        r, g, b = get_color(test_image, x, y)

        if r != (0 or 255) or g != (0 or 255) and b != (0 or 255):
            fail_message = 'FAIL: Pixel @ (' + str(x) + ', ' + str(y) + '), r = ' + str(r) + ', g = ' + str(g) + ', b = ' + str(b) + '\n'
            print(fail_message)

        else:
            pass_message = 'PASS: Pixel @ (' + str(x) + ', ' + str(y) + '), r = ' + str(r) + ', g = ' + str(g) + ', b = ' + str(b) + '\n'
            print(pass_message)
            
#P6 Refactored Tests

def test_horizontal_flip() -> None:
    """
    Author: Tahir Towsif
    Function tests weather or not an image has been flipped horizontaly.
    >>> test_horizontal_flip()
    >>>
    """
    image = create_image(3,3)
    
    set_color(image, 0, 0, create_color(1, 2, 3))
    set_color(image, 1, 0, create_color(4, 5, 6))
    set_color(image, 2, 0, create_color(7, 8, 9))
    
    set_color(image, 0, 1, create_color(15, 30, 45))
    set_color(image, 1, 1, create_color(50, 60, 70))
    set_color(image, 2, 1, create_color(30, 20, 10))
    
    set_color(image, 0, 2, create_color(70, 30, 50))
    set_color(image, 1, 2, create_color(10, 50, 100))
    set_color(image, 2, 2, create_color(5, 7, 10))
    
    new_image = flip_horizontal(image.copy())
    
    for x in range (0,3):
        if get_color(new_image, x, 0) != get_color(image, x, 2):
            print ("Error, row 0 of the new image is not equal to row 2 of the original image")
    for x in range (0,3):
        if get_color(new_image, x, 1) != get_color(image, x, 1):
            print("Error: Row 1 should not change")
    for x in range (0,3):
        if get_color(new_image, x, 2) != get_color(image, x, 0):
            print ("Error: Row 2 of the new image is not equal to row 0 of the original image")

def test_flip_vertical() -> bool:
    """ Author: Tahir Towsif
    Tests flip_vertical using a 3 by 2 image.
    Check that cols 0 and 2 have switched values and that col 1 has not been changed.
    Returns True if all tests pass, otherwise returns False and prints the columns 
    that are incorrect.
    
    >>>test_flip_vertical()
    """
    image = create_image(3, 3)
    success = True

    # Create colours for col 0
    set_color(image, 0, 0, create_color(1, 2, 3))
    set_color(image, 0, 1, create_color(4, 5, 6))
    set_color(image, 0, 2, create_color(7, 8, 9))

    # Create colours for col 1
    set_color(image, 1, 0, create_color(5, 10, 15))
    set_color(image, 1, 1, create_color(20, 25, 30))
    set_color(image, 1, 2, create_color(35, 40, 45))

    # Create colours for col 2
    set_color(image, 2, 0, create_color(10, 20, 30))
    set_color(image, 2, 1, create_color(40, 50, 60))
    set_color(image, 2, 2, create_color(70, 80, 90))

    newImage = flip_vertical(image)

    # col 0 and 2 should be swapped, col 1 should remain the same
    for y in range(0, 3):
        if get_color(newImage, 0, y) != get_color(image, 2, y):
            print("Actual:", get_color(newImage, 0, y), " Expected:", get_color(image, 2, y))
            success = False

    for y in range(0, 3):
        if get_color(newImage, 1, y) != get_color(image, 1, y):
            print("Actual:", get_color(newImage, 1, y), "Expected:", get_color(image, 1, y))
            success = False

    for y in range(0, 3):
        if get_color(newImage, 2, y) != get_color(image, 0, y):
            print("Actual:", get_color(newImage, 2, y), " Expected:", get_color(image, 0, y))
            success = False
    if success:
        return True
    else:
        return False
    
def check_equal(description: str, outcome, expected) -> None:
    """Author: Tahir Towsif
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

        print("{0} FAILED: expected ({1}) has type {2}, "
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
    threshold = 45  # The test threshold is set to 45.

    original_image = create_image(4, 4)
    set_color(original_image, 0, 0, create_color(206, 164, 185))
    set_color(original_image, 1, 0, create_color(145, 34, 156))
    set_color(original_image, 2, 0, create_color(267, 240, 99))
    set_color(original_image, 3, 0, create_color(94, 167, 116))
    set_color(original_image, 0, 1, create_color(256, 223, 206))
    set_color(original_image, 1, 1, create_color(100, 89, 76))
    set_color(original_image, 2, 1, create_color(55, 179, 87))
    set_color(original_image, 3, 1, create_color(255, 33, 1))
    set_color(original_image, 0, 2, create_color(7, 55, 100))
    set_color(original_image, 1, 2, create_color(5, 5, 5))
    set_color(original_image, 2, 2, create_color(17, 18, 19))
    set_color(original_image, 3, 2, create_color(15, 155, 200))
    set_color(original_image, 0, 3, create_color(14, 17, 16))
    set_color(original_image, 1, 3, create_color(156, 247, 32))
    set_color(original_image, 2, 3, create_color(76, 56, 67))
    set_color(original_image, 3, 3, create_color(23, 67, 100))

    edited_image = create_image(4, 4)
    set_color(edited_image, 0, 0, create_color(255, 255, 255))
    set_color(edited_image, 1, 0, create_color(255, 255, 255))
    set_color(edited_image, 2, 0, create_color(0, 0, 0))
    set_color(edited_image, 3, 0, create_color(255, 255, 255))
    set_color(edited_image, 0, 1, create_color(0, 0, 0))
    set_color(edited_image, 1, 1, create_color(0, 0, 0))
    set_color(edited_image, 2, 1, create_color(0, 0, 0))
    set_color(edited_image, 3, 1, create_color(255, 255, 255))
    set_color(edited_image, 0, 2, create_color(255, 255, 255))
    set_color(edited_image, 1, 2, create_color(0, 0, 0))
    set_color(edited_image, 2, 2, create_color(0, 0, 0))
    set_color(edited_image, 3, 2, create_color(0, 0, 0))
    set_color(edited_image, 0, 3, create_color(14, 17, 16))  # The last row of the image
    set_color(edited_image, 1, 3, create_color(156, 247, 32))  # stays the same because the
    set_color(edited_image, 2, 3, create_color(76, 56, 67))  # filter does not run through the
    set_color(edited_image, 3, 3, create_color(23, 67, 100))  # last row.

    edge_detection = detect_edges(original_image, threshold)

    for x, y, col in edge_detection:
            check_equal('(' + str(x) + ',' + str(y) + ')', \
            col, get_color(edited_image, x, y))    
            
def test_imp_edge():
    """Author: Tahir Towsif
    This function tests if the improved edges function works as inteneded.
    
    >>>test_imp_edge()
    Input threshold:
    
    (0,0) PASSED
    (1,0) PASSED
    (0,1) PASSED
    (1,1) PASSED
    """

    threshold = int(input("Input threshold:"))

    orig = create_image(4, 4)
    set_color(orig, 1, 0, create_color(205, 160, 187))
    set_color(orig, 1, 1, create_color(103, 115, 127))
    set_color(orig, 1, 2, create_color(234, 241, 250))
    set_color(orig, 2, 0, create_color(97, 126, 113))
    set_color(orig, 2, 1, create_color(221, 239, 205))
    set_color(orig, 2, 2, create_color(101, 92, 85))
    set_color(orig, 1, 3, create_color(147, 173, 162))

    expected = create_image(4, 4)
    set_color(expected, 0, 1, create_color(0, 0, 0))
    set_color(expected, 1, 1, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 2, 1, create_color(0, 0, 0))
    set_color(expected, 1, 2, create_color(0, 0, 0))
    set_color(expected, 2, 2, create_color(0, 0, 0))

    imp_edge_detection = detect_edges_better(orig, threshold)

    for x, y, col in imp_edge_detection:
            check_equal('(' + str(x) + ',' + str(y) + ')', col, get_color(expected, x, y))
