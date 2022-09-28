# Drawing Routines that are similar to those in OpenGL
import math

from matrix_stack import *
arr_vars = []
lootie = None
rootie = None
bootie = None
tootie = None
trans = None
foovie = None

def gtOrtho(left, right, bottom, top, near, far):
    global lootie, rootie, bootie, tootie, trans
    lootie = float(left)
    rootie = float(right)
    bootie = float(bottom)
    tootie = float(top)
    trans = 1

def gtPerspective(fov, near, far):
    global foovie, trans
    foovie = fov
    trans = 0

def gtVertex(x, y, z):
    global arr_vars
    global lootie, rootie, bootie, tootie, trans, foovie
    currArr = [x, y, z, 1]
    currCtm = getMatrix()
    currArr = gtVectorMult(currCtm, currArr)
    x = currArr[0]
    y = currArr[1]
    z = currArr[2]
    if trans == 1:
        xEVO = (x - lootie) * (width / (rootie - lootie))
        yEVO = (y - bootie) * (height / (tootie - bootie))
        currArr[0] = xEVO
        currArr[1] = yEVO
    else:
        xP = (x/(abs(z)))
        yP = (y/(abs(z)))
        k = tan((radians(foovie)) / 2)
        xPP = (xP + k) * (width/ (2 * k))
        yPP = (yP + k) * (height/ (2 * k))
        currArr[0] = xPP
        currArr[1] = yPP
    arr_vars.append(currArr)

def gtBeginShape():
    global arr_vars
    arr_vars = []

def gtEndShape():
    global arr_vars
    for vert in range(0,len(arr_vars), 2):
        x1 = arr_vars[vert][0]
        y1 = height - arr_vars[vert][1]
        x2 = arr_vars[vert + 1][0]
        y2 = height - arr_vars[vert + 1][1]
        line(x1, y1, x2, y2)
        
def gtVectorMult(ctm, vec):
    toRet = [0, 0, 0, 0]
    for row in range(len(ctm)):
        for val in range(len(ctm[0])):
            toRet[row] += vec[val] * ctm[row][val]
    return toRet
