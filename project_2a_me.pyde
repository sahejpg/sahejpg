# Object Modeling Example Code

from __future__ import division
import traceback

time = 0   # time is used to move objects from one frame to another

def setup():
    size (800, 800, P3D)
    try:
        frameRate(120)       # this seems to be needed to make sure the scene draws properly
        perspective (60 * PI / 180, 1, 0.1, 1000)  # 60-degree field of view
    except Exception:
        traceback.print_exc()

def draw():
    try:
        global time
        time += 0.02

        camera (0, 0, 150, 0, 0, 0, 0,  1, 0)  # position of the virtual camera

        background (200, 200, 255)  # clear screen and set background to light blue
        
        # set up the lights
        ambientLight(200, 200, 200);
        lightSpecular(255, 255, 255)
        directionalLight (100, 100, 100, 1.3, 0.5, -3.5)
        
        # set some of the surface properties
        noStroke()
        specular (180, 180, 180)
        shininess (70.0)
        
        rotateY(time)
        helloKitty()


    except Exception:
        traceback.print_exc()



# helloKitty function    
def helloKitty():
    head()
    body()


#head func
def head():
    # head
    fill (255, 255, 255) #white
    pushMatrix()
    # translate (1, 1, 1)
    scale(2.4, 1.85, 2.1)
    sphere(10)
    popMatrix()
    
    # nose
    fill(200, 200, 5) #yellow
    pushMatrix()
    translate(0, 4, 20)
    scale(0.3, 0.2, 0.2)
    sphere(8)
    popMatrix()
    
    # eye left
    fill(0,0,0)
    pushMatrix()
    translate(-8, 1.5, 20)
    scale(0.2, 0.3, 0.2)
    sphere(6)
    popMatrix()
    
    # eye right
    fill(0,0,0)
    pushMatrix()
    translate(8, 1.5, 20)
    scale(0.2, 0.3, 0.2)
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
    fill(255, 150, 150)
    pushMatrix()
    translate(10, -15, 12)
    rotateZ(radians(35))
    rotateX(radians(45))
    scale(1, 1, 0.3)
    sphere(6)
    popMatrix()

    # bow right
    fill(255, 150, 150)
    pushMatrix()
    translate(20, -10, 12)
    rotateZ(radians(35))
    rotateX(radians(40))
    scale(1, 1, 0.3)
    sphere(6)
    popMatrix()
    
    # bow middle
    fill(255, 200, 200)
    pushMatrix()
    translate(15, -12, 14)
    rotateZ(radians(35))
    rotateX(radians(40))
    scale(1, 1, 0.3)
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
def body():
    # main body
    fill(255, 200, 200)
    pushMatrix()
    translate(0, 40, 0)
    scale(20)
    cone()
    popMatrix()
    
    # legl
    fill(255, 255, 255)
    pushMatrix()
    translate(-7, 45, 0)
    scale(8)
    cylinder()
    popMatrix()
    
    # legr
    fill(255, 255, 255)
    pushMatrix()
    translate(7, 45, 0)
    scale(8)
    cylinder()
    popMatrix()
    
    # arml
    fill(255, 150, 150)
    pushMatrix()
    translate(-18, 30, 0)
    rotateZ(radians(30))
    scale(4, 15, 4)
    cone()
    popMatrix()
    
    # armr
    fill(255, 150, 150)
    pushMatrix()
    translate(18, 30, 0)
    rotateZ(radians(-30))
    scale(4, 15, 4)
    cone()
    popMatrix()
    
    # handl
    fill(255, 255, 255)
    pushMatrix()
    translate(-18, 30.5, 0)
    rotateZ(radians(30))
    scale(2)
    sphere(2)
    popMatrix()
    
    # handr
    fill(255, 255, 255)
    pushMatrix()
    translate(18, 30.5, 0)
    rotateZ(radians(30))
    scale(2)
    sphere(2)
    popMatrix()
    
    # tail
    fill(255, 255, 255)
    pushMatrix()
    translate(0, 30.5, -15)
    scale(1, 1, 2)
    sphere(2)
    popMatrix()
    
    
# whisker
def whisker():
    fill(0, 0, 0)
    pushMatrix()
    scale(12, 0.1, 0.2)
    box(1)
    popMatrix()


# cone shape
def cone():
    # base
    beginShape()
    for i in range(800):
        theta = i * 2 * PI / 800
        x = cos(theta)
        z = sin(theta)
        vertex(x, 0, z)
    endShape(CLOSE) 
    
    x1 = 1 
    z1 = 0
    
    # main body
    for i in range(800):
        beginShape()
        theta = i * 2 * PI / 800
        x2 = cos(theta)
        z2 = sin(theta)
        vertex (x1, 0, z1)
        vertex(x2, 0, z2)
        vertex(0, -2, 0)
        endShape(CLOSE) 
        x1 = x2
        z1 = z2


# my cylinder shape
def cylinder(sides = 500):
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
        # normal (x2, 0, z2)
        vertex (x2, -1, z2)
        vertex (x2, 1, z2)
        endShape(CLOSE)
        x1 = x2
        z1 = z2
    
    
    
        
    
    
    
