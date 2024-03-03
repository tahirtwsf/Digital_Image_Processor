from Cimpl import*
import logging, os 

def red_channel() -> Image:
    """created by Tahir Towsif
    program loads 'p2-original.jpg' and applies the red filter to it. prompts user to save new image (must be saved as 'L1-12_P2_RED.png'
    >>> red_channel()
    (new pop-up displays the image with only the red component visible)
    """
    image = load_image('p2-original.jpg')
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        red = create_color(r, 0, 0)
        set_color(new_image, x, y, red)
    
    save(new_image)
    return show(new_image)

def test_red() -> None:
    red_image = load_image('L1-12_P2_RED.png')
    for x, y, (r, g, b) in red_image:
        if g !=0 and b !=0:
            print('FAIL, r =', r, 'g =', g, 'b =', b)
    else:
        print('PASS')
        
        

log = open('greentest.txt', 'a') #creates new log text file in the same folder 
def green_channel() -> Image:
    """Author: Tahir Towsif
    Returns a green copy of an image that was chosen by the user when 
    prompted. Each pixel's green component provides the RGB components 
    for the corresponding green shade. The program then shows the edited image. 
    
    >>> green_channel()
    """
    original_image = load_image(choose_file()) #Prompts user to choose image    
    new_image = copy(original_image)
    
    for x, y, (r, g, b) in new_image:
        green = create_color(0, g, 0)    
        set_color(new_image, x, y, green)
        
    show(new_image)
    
    return new_image

def test_green() -> None:
    '''Start of a test function for green_channel.
    
    Tests if the all pixels are green.
    
    >>> test_green()
    '''
    test_image = green_channel()
    
    for x, y, (r, g, b) in test_image:
        r, g, b = get_color(test_image, x, y)
        
        if r != 0 and b != 0:
            fail_message = 'FAIL: Pixel @ ('+ str(x) +', '+ str(y) +'), r = '+ str(r) + ', g = '+ str(g) +', b = '+ str(b) +'\n'
            print(fail_message)
            log.write(fail_message) 
            
    
        else:
            pass_message = 'PASS: Pixel @ ('+ str(x) +', '+ str(y) +'), r = '+ str(r) + ', g = '+ str(g) +', b = '+ str(b) +'\n'
            log.write(pass_message) #Full filter test can be accessed in the log file
            print(pass_message)

    os.system("notepad.exe greentest.txt") #Displays contents of log file
    open('greentest.txt', 'w').close() #Erases contents of log file once closed


def blue_channel() -> Image:
    """
    Written by Tahir Towsif
    Function loads a chosen image and applies a blue filter to it.
    After applying the filter the user will be prompted to save it under 
    the name "bluetest.jpg".
    """
    image = load_image(choose_file())
    image_new = copy(image)
    for x, y, (r, g, b) in image:
        blue = create_color(0, 0, b)
        set_color(image_new, x, y, blue)       
    return save_as(image_new, )    

def test_blue() -> None:
    blue_image = load_image('bluetest.jpg')
    for x, y, (r,g,b) in blue_image:
        if r != 0 or g!= 0:
            print ('Fail, r = ', r, 'g =', g, 'b=', b)
    else:
        print ('Pass')
    

def combine(red: Image, green: Image, blue: Image)->Image:
    """ Author: Tahir Towsif
    Takes a red, green, and blue channel of an image and combines the three
    to form the original image.
    """
    new_image = copy(red)               #create a copy of img red
    for x, y, (r, g, b) in new_image:   #iterate through pixels in img
        redR, redG, redB = get_color(red, x, y)
        greenR, greenG, greenB = get_color(green, x, y)
        blueR, blueG, blueB = get_color(blue, x, y)
        new_color = create_color( (redR+greenR+blueR), (redG+greenG+blueG), (redB+greenB+blueB)) #add up all the rgb values
        set_color(new_image, x, y, new_color) #change colour of the combined img
        
    return new_image
    

def test_combine() -> bool:
    """ Author: Tahir Towsif
    Tests the combine function using the provided red, green, and blue channel pictures.
    Returns true if pass is sucessful, false if it is not.
    """
    #This test function appears to fail everytime. This is most lieky because we are working with jpgs and each time a jpg is saved it looses quality.
    #A soltion would be to use a lossless file format such as png.
    original = load_image("p2-original.jpg")
    newImage = combine(load_image("red_image.jpg"), load_image("green_image.jpg"), load_image("blue_image.jpg"))

    for x, y, (r, g, b) in currImage:
        newR, newG, newB = get_color(currImage, x, y)               #r, g, b values for current image
        origR, origG, origB = get_color(targetImage, x, y)          #r, g, b values for target image
        if newR != origR or newG != origG or newB != origB: 
            print("FAIL: Pixel @ (",x,",",y,") does not match", sep="")
            print("Red values: Combined Red = ",newR," Original Red = ",origR ,sep="")
            print("Green values: Combined Green = ",newG," Original Green = ",origG ,sep="")
            print("Blue values: Combined Blue = ",newB," Original Blue = ",origB ,sep="")
            return False
    print("PASS")
    return True