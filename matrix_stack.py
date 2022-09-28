# Your Matrix Stack Library
import math
# you should modify the provided empty routines to complete the assignment

stackMatrix = None
ctm = None
scaleMatrix = None
transMatrix = None
rad = None
rotX = None
rotY = None
rotZ = None
ctmCopy = None

def gtInitialize():
    global stackMatrix, ctm
    stackMatrix = [[[1, 0, 0, 0], 
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]]]
    ctm = stackMatrix[0]

def gtPopMatrix():
    global ctm, stackMatrix
    if len(stackMatrix) == 1:
         print("Cannot pop the stack matrix")
    else:
        ctm = stackMatrix[len(stackMatrix) - 1]
        stackMatrix = stackMatrix[0:len(stackMatrix) - 1]

def gtPushMatrix():
    global ctm, stackMatrix, ctmCopy
    ctmCopy = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    for row in range(len(ctm)):
        for col in range(len(ctm[0])):
            ctmCopy[row][col] = ctm[row][col]
    stackMatrix.append(ctmCopy)

def gtScale(x,y,z):
    global stackMatrix, ctm, scaleMatrix
    scaleMatrix = [[x, 0, 0, 0],
                   [0, y, 0, 0],
                   [0, 0, z, 0],
                   [0, 0, 0, 1]]
    ctm = gtMatrixMulti(ctm, scaleMatrix)

def gtTranslate(x,y,z):
    global stackMatrix, ctm, transMatrix
    transMatrix = [[1, 0, 0, x],
                   [0, 1, 0, y],
                   [0, 0, 1, z],
                   [0, 0, 0, 1]]
    ctm = gtMatrixMulti(ctm, transMatrix)

def gtRotateX(theta):
    global stackMatrix, ctm, rad, rotX
    rad = theta * math.pi/180
    rotX = [[1, 0, 0, 0],
            [0, cos(rad), -sin(rad), 0],
            [0, sin(rad), cos(rad), 0],
            [0, 0, 0, 1]]
    ctm = gtMatrixMulti(ctm, rotX)

def gtRotateY(theta):
    global stackMatrix, ctm, rad, rotY
    rad = theta * math.pi/180
    rotY = [[cos(rad), 0, sin(rad), 0],
            [0, 1, 0, 0],
            [-sin(rad), 0, cos(rad), 0],
            [0, 0, 0, 1]]
    ctm = gtMatrixMulti(ctm, rotY)

def gtRotateZ(theta):
    global stackMatrix, ctm, rad, rotZ
    rad = theta * math.pi/180
    rotZ = [[cos(rad), -sin(rad), 0, 0],
            [sin(rad), cos(rad), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]
    ctm = gtMatrixMulti(ctm, rotZ)

def print_ctm():
    global ctm
    for row in ctm:
        print(str(row[0]) + "  " + str(row[1]) 
              + "  " + str(row[2]) + "  " + str(row[3]))
    print
    
def gtMatrixMulti(m1, m2):
    global stackMatrix, scaleMatrix, ctm, transMatrix
    global rad, rotX, rotY, rotZ
    toRet = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    for row1 in range(len(m1)):
        for col in range(len(m2[0])):
            for row2 in range(len(m2)):
                toRet[row1][col] = toRet[row1][col] + m1[row1][row2] * m2[row2][col]
    
    return toRet
    
        

        
