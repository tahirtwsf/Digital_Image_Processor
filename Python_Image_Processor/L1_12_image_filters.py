from Cimpl import choose_file, load_image, copy, create_color, create_image, set_color,\
                  show, Image, get_color, get_width, get_height

# P4 Refactored Filters

def two_tone(orig: Image, colour1: str, colour2: str)->Image:
    """Author: Tahir Towsif
    Takes an image and caclulates the brightness of each pixel.
    If brightness is <=127, set the pixel to the c1 colour.
    If brightness is >=128, set the pixel to the c2 colour.
    c1 and c2 must below lowercase colour names and should not be the same colour.
    Available colours: black, white, red, lime, blue, yellow, cyan, magenta, gray
    
    >>>two_tone(test.png, "black", "white")
    """
    new_image=copy(orig)
    colours=[("black",(0,0,0)), ("white",(255,255,255)), ("red", (255,0,0)), ("lime",(0,255,0)), ("blue",(0,0,255)), 
             ("yellow",(255,255,0)), ("cyan",(0,255,255)), ("magenta",(255,0,255)), ("gray",(128,128,128))]
    #Now we will determine the values of each colour string
    for i in colours:
        if colour1==i[0]:
            c1=create_color(i[1][0], i[1][1], i[1][2])
        if colour2==i[0]:
            c2=create_color(i[1][0], i[1][1], i[1][2])
    
    if c1==0 or c2==0:
        print("Invalid Colour!")
        return None    

    #Now apply the filter to the image
    for x, y, (r, g, b) in orig:
        if (r+g+b)/3<=127:
            set_color(new_image, x, y, c1)
        else:
            set_color(new_image, x, y, c2)
    return new_image

def three_tone(orig: Image, colour1: str, colour2: str, colour3: str)->Image:
    """Author: Tahir Towsif
    Takes an image and caclulates the brightness of each pixel.
    If brightness is between 0 and 84, set the pixel to the first colour.
    If brightness is between 85 and 170, set the pixel to the second colour.
    If brightness is between 171 and 255, set the pixel to the third colour.
    c1, c2, c3 must below lowercase colour names and should not be the same colour.
    Available colours: black, white, red, lime, blue, yellow, cyan, magenta, gray
    
    >>>three_tone(test.png, "black", "blue", "red")
    """
    new_image=copy(orig)
    colours=[("black",(0,0,0)), ("white",(255,255,255)), ("red", (255,0,0)), ("lime",(0,255,0)), ("blue",(0,0,255)), 
             ("yellow",(255,255,0)), ("cyan",(0,255,255)), ("magenta",(255,0,255)), ("gray",(128,128,128))]
    #Now we will determine the values of each colour string
    c1=c2=c3=0
    for i in colours:
        if colour1==i[0]:
            c1=create_color(i[1][0], i[1][1], i[1][2])
        if colour2==i[0]:
            c2=create_color(i[1][0], i[1][1], i[1][2])
        if colour3==i[0]:
            c3=create_color(i[1][0], i[1][1], i[1][2])
            
    if c1==0 or c2==0 or c3==0:
        print("Invalid Colour!")
        return None
    
    #Now apply the filter to the image
    for x, y, (r, g, b) in orig:
        avg=(r+g+b)/3
        if avg<=84:
            set_color(new_image, x, y, c1)
        elif 84<avg<=170:
            set_color(new_image, x, y, c2)
        else:
            set_color(new_image, x, y, c3)
    return new_image    

def grayscale(image: Image) -> Image:
    """Author: Tahir Towsif
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
    return new_image

def sepia(image: Image) -> Image:
    """Author: Tahir Towsif
    Returns a sepia-tinted image by taking each pixel and giving it a tint of yellow 
    depending on its shade of gray.
    
    >>>image = load_image(choose_file())
    >>>sepia(image)
    (copy of image is shown with sepia filter applied)
    """
    new_img = copy(grayscale(image))
    for x,y, (r, g, b) in image:
        if r < 63:
            dark_gray = create_color(r*1.1, g, b*0.9)
            set_color(new_img, x, y, dark_gray)
        elif r >=63 and r <= 191:
            b * 0.85 and r * 1.15
            medium_gray = create_color(r*1.15, g, b*0.85)
            set_color(new_img, x, y, medium_gray)
        elif r > 191:
            b * 0.93 and r * 1.08
            light_gray = create_color(r*1.08, g, b*0.93)
            set_color(new_img, x, y, light_gray)
    return new_img

def posterize(image: Image) -> Image:
    """Author: Tahir Towsif
    The function calls the _adjust_component function to determine
    the quadrant in which the components (r, g, b) of each pixel in 
    the loaded image lies and changes each component to the midpoint 
    of their specified quadrant. 
    
    >>>image = load_image(choose_file())
    >>>posterize(image)
    >>>show(new_image)
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

def extreme_contrast(image: Image) -> Image:
    """
    Author: Tahir Towsif
    Fucntion takes in an image and will turn rgb values greater than or equal 127 into a value of 255, and will take rgb values lower than 127 and they will become 0. These new rgb values will be usesd to produce a new image with extreme contrast on either end of the spectrum.
    >>>extreme_contrast(load_image('work.jpg'))
    >>>
    """
    image_new = copy(image)    
    for x, y, (r,g,b) in image:
        if r > 127:
            r_new = 255
        else:
            r_new = 0
        if g > 127:
            g_new = 255
        else:
            g_new = 0
        if b > 127:
            b_new = 255
        else:
            b_new = 0
        set_color(image_new, x, y, create_color(r_new, g_new, b_new))
    show(image_new)
    return image_new

#P5 Refactored Filters

def flip_horizontal(orig: Image) -> Image:
    """Author: Tahir Towsif
    Takes an image and flips it though an imaginary horizontal line in the center of the screen.
    Returns a copy of the image containing the flipped image.
    
    >>>flip_horizontal(choose_file())
    """
    width = get_width(orig)
    height = get_height(orig)
    new_image = copy(orig)

    for y in range(0, height // 2):
        for x in range(0, width):
            pTop = get_color(orig, x, y)
            pBottom = get_color(orig, x, height - 1 - y)

            set_color(new_image, x, y, pBottom)
            set_color(new_image, x, height - 1 - y, pTop)

    return orig

def flip_vertical (image:Image) -> Image:
    """
    Author: Tahir Towsif
    Function takes an image and mirrors it across the vertical axis.
    
    >>>flip_vertical(choose_file())
    """
    copy_image=copy(image)
    
    width = get_width(copy_image)
    height = get_height(copy_image)
    for x in range(0, get_width(copy_image)//2):
        for y in range(0, get_height(copy_image)):
            left = get_color(copy_image, x, y)
            right = get_color(copy_image, width - 1 - x, y)
            set_color(copy_image, x, y, right)
            set_color(copy_image, width - 1 - x, y, left)
    return copy_image

def detect_edges(img: Image, threshold: int) -> Image:
    """Author: Tahir Towsif
    Takes an image, makes a copy of it and changes the color of the pixels
    to black or white, depending on their contrast.
    
    >>> img = load_image(choose_file())
    >>> detect_edges(img)
    >>> show(img)
    """
    image = copy(img)
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)

    for x in range(0, get_width(image)):
        for y in range(0, get_height(image) - 1):
            (r, g, b) = get_color(image, x, y)
            (r2, g2, b2) = get_color(image, x, y + 1)  #Brightness of the pixel below
            if abs(((r + g + b) // 3) - ((r2 + g2 + b2) // 3)) > threshold:  #Checking if difference is greater than threshold
                set_color(image, x, y, black)
            else:
                set_color(image, x, y, white)

    return image

def detect_edges_better(img: Image, threshold: int) -> Image:
    """Author: Tahir Towsif
    Takes an image, makes a copy of it and changes the color of the pixels
    to black or white, depending on their contrast.
    
    >>>image = load_image(choose_file()) 
    >>>detect_edges(image, >Input threshold here<)
    >>>show(image)
    It is recommended that the user input a threshold from a range of 1-20 in 
    in order to recieve optimal results. 
    The program will then run and return the edited image. 
    """
    new_image = copy(image)
    
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    
    for x in range(0, get_width(img) - 1):
        for y in range(0, get_height(img) - 1):
            (r, g, b) = get_color(img, x, y)
            (r2, g2, b2) = get_color(img, x, y + 1)
            (r3, g3, b3) = get_color(img, x + 1, y)
            if abs(((r + g + b) // 3) - ((r2 + g2 + b2) // 3)) > threshold \
               or abs(((r + g + b) // 3) - ((r3 + g3 + b3) // 3)) > threshold: \
               set_color(img, x, y, black)
            else:
                set_color(img, x, y, white)
    return new_image