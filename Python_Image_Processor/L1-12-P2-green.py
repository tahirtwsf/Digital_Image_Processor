import logging, os
from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, Image, save_as



log = open('greentest.txt', 'a') #creates new log text file in the same folder 

def green_channel() -> Image:
    """Author: Tahir Towsif
    Returns a green copy of an image that was chosen by the user when 
    prompted. Each pixel's green component provides the RGB components 
    for the corresponding green shade. The program then shows the edited image. 
    
    >>> green_channel()
    """
    original_image = load_image(choose_file()) #Prompts user to choose image.
    new_image = copy(original_image)
    
    for x, y, (r, g, b) in new_image:
        green = create_color(0, g, 0)    
        set_color(new_image, x, y, green)
        
    show(new_image) #Shows user edited image.
    save_as(new_image, ) #Prompts user to save the edited image. 
    return new_image

def test_green() -> None:
    '''Start of a test function for green_channel.
    
    Tests if the all pixels are green.
    
    >>> test_green()
    (Note: The new image must be closed and saved once prompted before the test 
    function can continue)
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
    