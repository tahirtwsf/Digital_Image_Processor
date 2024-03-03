from Cimpl import*


def detect_edges_better(img: Image, threshold: int) -> Image:
    """Author: Tahir Towsif
    Takes an image, makes a copy of it and changes the color of the pixels
    to black or white, depending on their contrast.
    
    >>> image = load_image(choose_file()) 
    >>> detect_edges(image, >Input threshold here<)
    It is recommended that the user input a threshold from a range of 1-20 in 
    in order to recieve optimal results. 
    The program will then run and show the user the edited image. 
    
    
    """
    img = copy(image)
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    for x in range(0, get_width(img) - 1):
        for y in range(0, get_height(img) - 1):
            (r, g, b) = get_color(img, x, y)
            (r2, g2, b2) = get_color(img, x, y + 1)
            (r3, g3, b3) = get_color(img, x + 1, y)
            if abs(((r + g + b) // 3) - ((r2 + g2 + b2) // 3)) > threshold or abs(((r + g + b) // 3) - ((r3 + g3 + b3) // 3)) > threshold:
                set_color(img, x, y, black)
            else:
                set_color(img, x, y, white)
    show(img)
    return img
