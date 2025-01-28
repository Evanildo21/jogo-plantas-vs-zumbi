import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np




keys = {}

rotation_index = False
angle=0
x,z=0,0



def camera():
    global rotation_index,angle,x,z
    vetor=[[1, 3.5, 14],
           [0, 0, -1.0],
           [0.0, 1.0, 0.0]]
    c=[x + y for x,y in zip(vetor[0],vetor[1])]
    if rotation_index == True:
        d_input()
    else:
        if angle != 0 or x != 0:
            
            volta_input()

    gluLookAt(vetor[0][0],vetor[0][1],vetor[0][2],c[0],c[1],c[2],vetor[2][0],vetor[2][1],vetor[2][2])


def d_input():
    global x,z,angle
    if x<13:
        x+=1
        z-=1
    if angle < 90:
        angle+=6.9
    glTranslated(x,1,z)
    glRotatef(angle,0,1,0)


def volta_input():
    global x,z,angle
    if x != 0:
        x-=1
    if z != -1:
        z+=1
    if angle >6.9:
        angle-=6.9
    
    glTranslated(x,0.1,z)
    glRotatef(angle,0,1,0)
    
    







def process_input():
    global rotation_index
    if rotation_index == True:
        rotation_index = False
    else:   
        rotation_index = True
        