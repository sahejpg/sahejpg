def setup():
    size (600, 600) #size of the screen
    
def draw():
    background(255, 255, 255) #set the background to white
    noStroke()
    
    # declaring initial vars and square
    n = 5
    bigBoy = 200
    x = 300
    y = 300
    rectMode(CENTER)
    fill(255, 0, 40)
    rect(x, y, bigBoy, bigBoy)
    
    # setting up colors
    j = 100
    p = 0
    fill(255, p, j)
    
    # creating the satelliete displacement ratio 
    # if mouseY is on top edge, satellite is same size ratio = 1
    # if mouse Y is on bottom edge, satellite is 0
    k = (600 - mouseY)/600.0
    
    # scaling size of satellite square (cutie)
    cutie = bigBoy * k
    
    # finding displacement of x and y for center coordinate of cutie
    t = (bigBoy / 2.0) + (cutie / 2.0)
    s =  x - mouseX
    
    # drawing rectangle with displacements (s, t) and new size
    rect(x - s, y - t, cutie, cutie)
    rect(x + s, y + t, cutie, cutie)
    rect(x - t, y + s, cutie, cutie)
    rect(x + t, y - s, cutie, cutie)
    
    # recursive call to add cuties
    smallBabies(cutie, x - s, y - t, k, s, t, n, j, p)
    smallBabies(cutie, x + s, y + t, k, s, t, n, j, p)
    smallBabies(cutie, x - t, y + s, k, s, t, n, j, p)
    smallBabies(cutie, x + t, y - s, k, s, t, n, j, p)

    
def smallBabies(bigBoy, x, y, k, s, t, n, j, p):
    """    
    Recursively draws four rectangles around a given parent square by 
    updating displacement values, given a global displacement ratio
    
    bigBoy: side length of parent square
    x: x coord of parent square center
    y: y coord of parent square center
    k: displacement ratio of parent and child
    s: displacement from center of prev. parent and curr. parent
    t: displacement from center of prev. parent and curr. parent
    n: number of recursive calls left + 1
    j: color
    p: color
    
    """
    # base case
    if (n == 1):
        return 
    
    # scaling size of satellite sq.
    cutie = bigBoy * k
    
    # displacements for satellite sq. scaled
    t = t * k
    s = s * k
    
    # updated colors
    j = j + 50
    p = p + 40
    fill(255, p, j)
    
    # drawing satellite squares
    rect(x - s, y - t, cutie, cutie)
    rect(x + s, y + t, cutie, cutie)
    rect(x - t, y + s, cutie, cutie)
    rect(x + t, y - s, cutie, cutie)
    
    # recursive call
    smallBabies(cutie, x - s, y - t, k, s, t, n - 1, j, p)
    smallBabies(cutie, x + s, y + t, k, s, t, n - 1, j, p)
    smallBabies(cutie, x - t, y + s, k, s, t, n - 1, j, p)
    smallBabies(cutie, x + t, y - s, k, s, t, n - 1, j, p)

    
