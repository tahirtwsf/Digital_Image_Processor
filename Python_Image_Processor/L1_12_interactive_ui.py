from L1_12_image_filters import *

def display_menu()->None:
    """Author: Tahir Towsif
    Prints the menu in the shell.
    
    >>>display_menu()
    L)oad Image  S)ave As
    2)-tone  3)-tone  X)treme contrast  T)int Speia  P)osterize
    E)dge Detect  I)mproved edge detect  V)ertical flip  H)orizontal flip
    Q)uit

    : 
    """
    print("L)oad Image  S)ave As")
    print("2)-tone  3)-tone  X)treme contrast  T)int Speia  P)osterize")
    print("E)dge Detect  I)mproved edge detect  V)ertical flip  H)orizontal flip")
    print("Q)uit")
    print()
    print(": ", end="")
    
def check_input(choice , valid_inputs: tuple)->bool:
    """Author: Tahir Towsif
    Check a variable against a tuple of variables valid_inputs.
    Returns True if the variable existts in the tuple.
    ELse, returns False.
    
    >>>check_input("test", ("potato", "a", "1", "test" "3") )
    True
    
    >>>check_input(1, ("a", 1, "2") )
    True
    
    >>>check_input("c", ("a", 1, "2") )
    False
    """
    for i in valid_inputs:
        if choice==i:
            return True
    return False

def input_int()->int:
    """Author: Tahir Towsif
    Takes an input and check if it is a positive int.
    If input is not a positive int, the function will keep prompt the user to enter a positive integer.
    If the input is a positive int, returns the integer.
    
    >>>input_int()
    a
    Please enter a postive integer
    >>>-2
    Please enter a postive integer
    >>>2.1
    Please enter a postive integer
    >>>3
    3
    """
    number=input()
    while number.isdigit() == False:
        print("Please enter a postive integer")
        number=input()
    return int(number)

def call_filter(choice: str, img: Image)->Image:
    """Author: Tahir Towsif
    Take a str input and an Image and calls the respective filter on the image.
    Works with both uppercase and lowercase inputs.
    
    Returns a copy of the modified image after calling the filter.
    
    choice should be either 2, 3, "X", "T", "P", "E", "I", "V", "H" or
    any repective lowercase letter.
    Returns the unmodified img if an invalid choice is selected.
    
    >>>call_filter("t", my_image)
    Returns a sepia tinted copy of my_image
    
    >>>call_filter("Z", my_image)
    Returns unmodified version of my_image
    """
    if choice=="2":
        return two_tone(img,  "yellow", "cyan")
    
    elif choice=="3":
        return three_tone(img,  "yellow", "magenta", "cyan")
    
    elif choice=="X" or choice=="x":
        return extreme_contrast(img)
        
    elif choice=="T" or choice=="t":
        return sepia(img)
        
    elif choice=="P" or choice=="p":
        return posterize(img)
    
    elif choice=="E" or choice=="e":
        print("Please input a threshold value")
        threshold=input_int()
        return detect_edges(img, threshold)
    
    elif choice=="I" or choice=="i":
        print("Please input a threshold value")
        threshold=input_int()
        return detect_edges_better(img, threshold)        
    
    elif choice=="V" or choice=="v":
        return flip_vertical(img)
    
    elif choice=="H" or choice=="h":
        return flip_horizontal(img)
    
    else:
        return img
        
        
#Main script
exit=False
img=None
slq=("S", "s", "L", "l", "Q", "q")
filters = ("2", "3", "x", "X", "t", "T", "p", "P", "e", "E", "i", "I", "v", "V", "h", "H")

while exit == False:
    display_menu()
    valid_input = False
    while valid_input == False:
        choice = input()
        if check_input(choice, slq):
            if choice=="S" or choice=="s":
                save_as(img, )
                
            elif choice=="L" or choice=="l":
                img=load_image(choose_file())
                
            elif choice=="Q" or choice=="q":
                exit=True
                
            valid_input=True
            
        elif check_input(choice, filters):
            if img != None:
                img=call_filter(choice, img)
                show(img)
                valid_input=True
            else:
                print("No image loaded")
        else:
            print("No such command")
                
    
    