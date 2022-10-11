from __future__ import division
import traceback

time = 0


def setup():
    size(800, 800, P3D)
    try:
        frameRate(120)      
        perspective (60 * PI / 180, 1, 0.1, 1000)     # 60-degree field of view
    except Exception:
        traceback.print_exc()

def draw():
    try:
        global time
        time += 0.02
        fall = False
        
        if (time <= 3):
            camera(time * 20, -50, 150, -time * 90, 0, 0, 0, 1, 0)
            pointLight(20, 20, 20, 0, -300, -1800)
            ambientLight(120, 120, 120);
            lightSpecular(255, 255, 255)
            directionalLight (100, 100, 100, 1.3, 0.5, -3.5)
            darkSky = loadImage("darkSky.jpg")
            background(darkSky)
        if (3 < time <= 6):
            camera(3 * 20, -50, 0.25 * -time * 150, -3 * 200, 0, 0, 0, 1, 0)
            pointLight(20, 20, 20, 0, -300, -1800)
            ambientLight(100, 100, 100);
            lightSpecular(255, 255, 255)
            directionalLight (100, 100, 100, 1.3, 0.5, -3.5)
            darkSky = loadImage("darkSky.jpg")
            background(darkSky)
        elif (6 < time < 9):
            camera(60, -50, -225, -600, 0, 0, 0, 1, 0)
            pointLight(20, 20, 20, 0, -300, -1800)
            ambientLight(180, 180, 180);
            lightSpecular(255, 255, 255)
            directionalLight (100, 100, 100, 1.3, 0.5, -3.5)
            sky = loadImage("sky.jpg")
            background(sky)
        elif (time >= 9):
            camera(60, -50, -225, -600, 0, 0, 0, 1, 0)
            pointLight(20, 20, 20, 0, -300, -1800)
            ambientLight(180, 180, 180);
            lightSpecular(255, 255, 255)
            directionalLight (100, 100, 100, 1.3, 0.5, -3.5)
            sky = loadImage("sky.jpg")
            background(sky)
    
        
        
        # set some of the surface properties
        noStroke()
        specular (180, 180, 180)
        shininess (70.0)
        
        # moving main hello kitty
        pushMatrix()
        if (time < 3):
            translate(100 * -time, 0, 0)
            rotateY(radians(-90))
        elif (3 < time < 5):
            translate(100 * -3, 0, 20 * -time)
            rotateY(radians(-180))
        else:
            translate(100 * -3, 0, -100)
            rotateY(radians(180))
        myKitty = helloKitty(30, 30, 30, 30, 255, 150, 150)
        popMatrix()
        
        pushMatrix()
        translate(-308, 0, -150)
        if (time > 5.5):
            translate(-35, 0, 0)
            rotateY(radians(135))
        door()
        popMatrix()
        
        # placing other hello kitty
        pushMatrix()
        translate(-330, 0, -200)
        rotateY(radians(30))
        otherKitty = helloKitty(0, 0, 0, 0, 200, 150, 205)
        popMatrix()
        
        # falling flowers these are being instanced
        f1 = fallFlower(255, 100, 200, 20, 100)
        f2 = fallFlower(200, 200, 255, 100, 200)
        f3 = fallFlower(255, 200, 200, 180, 50)
        f4 = fallFlower(200, 200, 255, 600, 150)
        f5 = fallFlower(250, 250, 100, 340, 250)
        f6 = fallFlower(200, 250, 175, 550, 350)
        f7 = fallFlower(100, 250, 250, 450, 20)
        f8 = fallFlower(255, 100, 200, 680, 40)
        f9 = fallFlower(255, 200, 200, 790, 180)
        
        ground()
        
        # implementing the ending scene message
        FallMessage()
        
        # adding trees to the scene for depth and because kitty needs shade
        pushMatrix()
        translate(-380, 0, -210)
        scale(2)
        tree()
        popMatrix()
            
        
    except Exception:
        traceback.print_exc()

# falling flowers method    
def fallFlower(r,g,b,x, y):
    global time
    
    if (time > 6):
        pushMatrix()
        translate(-500, -1600 + (time * 200) + y, -350 + x)
        rotateY(radians(100))
        rotateZ(radians(time) * 400)
        scale(4)
        flower(r,g,b)
        popMatrix()

# falling message method    
def FallMessage():
    global time
    
    if (time >= 7):
        pushMatrix()
        if (time > 9):
            translate(-800, -200, 0)
        else:
            translate(-800, -2000 + (time * 200), 0)
        rotateY(radians(110))
        scale(2)
        endScene()
        popMatrix()
 
#hello kitty function    
def helloKitty(arml, armr, legl, legr, R, G, B):
    global time
    if (time > 5):  # ab 6 secs
        head(R, G, B)
        body(0, 0, 0, 0, R, G, B)
    else:
        head(R, G, B)
        body(arml, armr, legl, legr, R, G, B) # arm and leg rotation for when she walks

# head function        
def head(R, G, B):
    # head
    fill (255, 255, 255) #white
    pushMatrix()
    scale(2.4, 1.85, 2.1)
    sphereDetail(15)
    sphere(10)
    popMatrix()
    
    # nose
    fill(200, 200, 5) #yellow
    pushMatrix()
    translate(0, 4, 20)
    scale(0.3, 0.2, 0.2)
    sphereDetail(15)
    sphere(8)
    popMatrix()
    
    # eye left
    fill(0,0,0)
    pushMatrix()
    translate(-8, 1.5, 20)
    scale(0.2, 0.3, 0.2)
    sphereDetail(15)
    sphere(6)
    popMatrix()
    
    # eye right
    fill(0,0,0)
    pushMatrix()
    translate(8, 1.5, 20)
    scale(0.2, 0.3, 0.2)
    sphereDetail(15)
    sphere(6)
    popMatrix()
    
    # ear left
    fill(255, 255, 255)
    pushMatrix()
    translate(-15, -12, 0)
    rotateZ(radians(-35))
    scale(8)
    cone()
    popMatrix()
    
    # ear right
    fill(255, 255, 255)
    pushMatrix()
    translate(15, -12, 0)
    rotateZ(radians(35))
    scale(8)
    cone()
    popMatrix()
    
    # bow left
    fill(R, G, B)
    pushMatrix()
    translate(10, -15, 12)
    rotateZ(radians(35))
    rotateX(radians(45))
    scale(1, 1, 0.3)
    sphereDetail(15)
    sphere(6)
    popMatrix()

    # bow right
    fill(R, G, B)
    pushMatrix()
    translate(20, -10, 12)
    rotateZ(radians(35))
    rotateX(radians(40))
    scale(1, 1, 0.3)
    sphereDetail(15)
    sphere(6)
    popMatrix()
    
    # bow middle
    fill(R, G + 50, B + 50)
    pushMatrix()
    translate(15, -12, 14)
    rotateZ(radians(35))
    rotateX(radians(40))
    scale(1, 1, 0.3)
    sphereDetail(15)
    sphere(4)
    popMatrix()
    
    # whisker topl
    pushMatrix()
    translate(-18, 2, 18)
    rotateZ(radians(-2))
    whisker()
    popMatrix()
    
    # whisker midl
    pushMatrix()
    translate(-18, 5, 17.8)
    rotateZ(radians(-3))
    whisker()
    popMatrix()
    
    # whisker botl
    pushMatrix()
    translate(-18, 8, 16.6)
    rotateZ(radians(-4))
    whisker()
    popMatrix()
    
    # whisker topr
    pushMatrix()
    translate(18, 2, 18)
    rotateZ(radians(2))
    whisker()
    popMatrix()
    
    # whisker medr
    pushMatrix()
    translate(18, 5, 17.8)
    rotateZ(radians(3))
    whisker()
    popMatrix()
    
    # whisker botr
    pushMatrix()
    translate(18, 8, 16.6)
    rotateZ(radians(4))
    whisker()
    popMatrix()
    
# body function
def body(arml, armr, legl, legr, R, G, B):
    global time
    
    # main body
    fill(R, G + 50, B + 50)
    pushMatrix()
    translate(0, 40, 0)
    scale(20)
    cone()
    popMatrix()
    
    # legl
    fill(255, 255, 255)
    pushMatrix()
    translate(-7, 45, 0)
    if (legl != 0):
        rotateX(radians(-legl) * sin(4 * time))   # move leg back and forth
    scale(8)
    cylinder()
    popMatrix()
    
    # legr
    fill(255, 255, 255)
    pushMatrix()
    translate(7, 45, 0)
    if (legr != 0):
        rotateX(radians(legr) * sin(4 * time))   # move leg back and forth
    scale(8)
    cylinder()
    popMatrix()
    
    # arml
    fill(R, G, B)
    pushMatrix()
    if (arml != 0):
        rotateX(radians(arml) * sin(4 * time))
    if (time > 6):
        translate(0, 14, 0)
        rotateZ(radians(45))
    translate(-18, 30, 0)
    rotateZ(radians(30))
    scale(4, 15, 4)
    cone()
    popMatrix()
    
    # armr
    fill(R, G, B)
    pushMatrix()
    if (armr != 0):
        rotateX(radians(-armr) * sin(4 * time))
    if (time > 6):
        translate(0, 14, 0)
        rotateZ(radians(-45))
    translate(18, 30, 0)
    rotateZ(radians(-30))
    scale(4, 15, 4)
    cone()
    popMatrix()
    
    # handl
    fill(255, 255, 255)
    pushMatrix()
    if (arml != 0):
        rotateX(radians(arml) * sin(4 * time))
    if (time > 6):
        translate(0, 14, 0)
        rotateZ(radians(45))
    translate(-18, 30.5, 0)
    rotateZ(radians(30))
    scale(2)
    sphereDetail(15)
    sphere(2)
    popMatrix()
    
    # handr
    fill(255, 255, 255)
    pushMatrix()
    if (armr != 0):
        rotateX(radians(-armr) * sin(4 * time))
    if (time > 6):
        translate(0, 14, 0)
        rotateZ(radians(-45))
    translate(18, 30.5, 0)
    rotateZ(radians(30))
    scale(2)
    sphereDetail(15)
    sphere(2)
    popMatrix()
    
    # tail
    fill(255, 255, 255)
    pushMatrix()
    translate(0, 30.5, -15)
    scale(1, 1, 2)
    sphereDetail(15)
    sphere(2)
    popMatrix()
    
# cone shape
def cone():
    # base
    beginShape()
    for i in range(600):
        theta = i * 2 * PI / 600
        x = cos(theta)
        z = sin(theta)
        vertex(x, 0, z)
    endShape(CLOSE) 
    
    x1 = 1 
    z1 = 0
    
    # main body
    for i in range(600):
        beginShape()
        theta = i * 2 * PI / 600
        x2 = cos(theta)
        z2 = sin(theta)
        vertex (x1, 0, z1)
        vertex(x2, 0, z2)
        vertex(0, -2, 0)
        endShape(CLOSE) 
        x1 = x2
        z1 = z2

# whisker
def whisker():
    fill(0, 0, 0)
    pushMatrix()
    scale(12, 0.1, 0.2)
    box(1)
    popMatrix()
    
# my cylinder shape
def cylinder(sides = 400):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        z = sin(theta)
        vertex ( x,  -1, 0)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        z = sin(theta)
        vertex ( x,  1, z)
    endShape(CLOSE)
    # round main body
    x1 = 1
    z1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        z2 = sin(theta)
        beginShape()
        # normal (x1, 0, z1)
        vertex (x1, 1, z1)
        vertex (x1, -1, z1)
        vertex (x2, -1, z2)
        vertex (x2, 1, z2)
        endShape(CLOSE)
        x1 = x2
        z1 = z2

# flowers func
def flower(R, G, B):
    #center
    fill(255, 255, 255)
    pushMatrix()
    scale(1, 1, 0.3)
    sphere(4)
    popMatrix()
    
    #left
    fill(R, G, B)
    pushMatrix()
    translate(-7, 0, 0)
    scale(1.5, 1.5, 0.3)
    sphere(4)
    popMatrix()
    
    #right
    fill(R, G, B)
    pushMatrix()
    translate(7, 0, 0)
    scale(1.5, 1.5, 0.3)
    sphere(4)
    popMatrix()
    
    #botl
    fill(R, G, B)
    pushMatrix()
    translate(-5, 7, 0)
    scale(1.5, 1.5, 0.3)
    sphere(4)
    popMatrix()
    
    #botr
    fill(R, G, B)
    pushMatrix()
    translate(5, 7, 0)
    scale(1.5, 1.5, 0.3)
    sphere(4)
    popMatrix()
    
    #top
    fill(R, G, B)
    pushMatrix()
    translate(0, -7, 0)
    scale(1.5, 1.5, 0.3)
    sphere(4)
    popMatrix()
    
# door function
def door():
    # main frame
    fill(255, 100, 100)
    pushMatrix()
    scale(1, 2, 0.1)
    box(55)
    popMatrix()
    
    # knob
    fill(255, 150, 150)
    pushMatrix()
    translate(20, 0, 5)
    sphere(3)
    popMatrix()
    
def ground():
    fill(240, 220, 235)
    pushMatrix()
    translate(-400, 555, -400)
    scale(20, 10, 20)
    box(100)
    popMatrix()
    
def endScene():
    # bottom
    fill(200, 200, 255)
    pushMatrix()
    # rotateZ(radians(180))
    scale(25, 22, 0.6)
    box(6)
    popMatrix()
    
    fill(255, 255, 255)
    pushMatrix()
    textSize(20)
    text("Everything is ", -65, -40, 2)
    popMatrix()
    fill(255, 255, 255)
    pushMatrix()
    textSize(20)
    text("better with a ", -60, 0, 2)
    popMatrix()
    
    fill(255, 200, 200)
    pushMatrix()
    textSize(25)
    text("friend ", -40, 40, 2)
    popMatrix()
        
# tree
# hello kitty likes to stand in the shade
def tree():
    # trunk
    fill(60, 30, 0)
    pushMatrix()
    scale(10, 30, 10)
    cylinder()
    popMatrix()
    
    # leaves
    fill(100, 200, 100)
    pushMatrix()
    translate(0, -30, 0)
    sphereDetail(10)
    sphere(25)
    popMatrix()
    

    
    
    

    
    
    
    
    
    
