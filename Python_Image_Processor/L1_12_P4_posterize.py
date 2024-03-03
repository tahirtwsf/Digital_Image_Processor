from Cimpl import *

file = choose_file()
image = load_image(file)


def posterize(image: image) -> Image:
    """Author: Tahir Towsif
    The function calls the _adjust_component function to determine
    the quadrant in which the components (r, g, b) of each pixel in 
    the loaded image lies and changes each component to the midpoint 
    of their specified quadrant. 
    
    >>>posterize(image)
    """
    new_image = copy(image)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        #Changes each component to the midpoint of their specific quadrant.
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        #Changes the colour of each pixel. 
        new_colour = create_color(r, g, b)
        set_color(new_image, x, y, new_colour)

    show(new_image) #Shows image with applied filter to user.
    return new_image


def _adjust_component(orig_value: int) -> int:
    """Author: Tahir Towsif
    Determines where each component (r, g, b) of a pixel is positioned in the 4 
    quadrants (0 to 63, 64 to 127, 128 to 191, and 192 to 255) and adjusts the 
    component values to the midpoint of that specific quadrant.
    
    >>> _adjust_component(25)
    31
    >>> _adjust_component(250)
    223
    >>> _adjust_component(127)
    95
    >>> _adjust_component(150)
    159
    """
    if orig_value <= 63:
        value = 31
    elif orig_value <= 127:
        value = 95
    elif orig_value <= 191:
        value = 159
    elif orig_value <= 255:
        value = 223
    return value
