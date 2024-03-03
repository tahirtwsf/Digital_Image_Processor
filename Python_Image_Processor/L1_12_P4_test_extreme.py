from Cimpl import *
from L1_12_P4_extreme.py import *


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

    show(test_image)




