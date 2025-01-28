from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

def cube(colors:list):
    vertices = [
        [-0.5, -0.5, -0.5],
        [0.5, -0.5, -0.5],
        [0.5, 0.5, -0.5],
        [-0.5, 0.5, -0.5],
        [-0.5, -0.5, 0.5],
        [0.5, -0.5, 0.5],
        [0.5, 0.5, 0.5],
        [-0.5, 0.5, 0.5],
    ]
    faces = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 1, 5, 4],
        [2, 3, 7, 6],
        [0, 3, 7, 4],
        [1, 2, 6, 5],
    ]
    
   
    glScale(1,1,1)
    glBegin(GL_QUADS)
    c=0
    for face in faces:
        glColor3fv(colors[c])
        for vertex in face: 
            glVertex3fv(vertices[vertex])
        c+=1
    glEnd()
   

def piramide():
    vertices = [
        [1, 1, 1],
        [-1, -1, 1],
        [-1, 1, -1],
        [1, -1, -1],
    ]
    faces = [
        [0, 1, 2],
        [0, 1, 3],
        [0, 2, 3],
        [1, 2, 3],
    ]
    cores = [
        [0, 0.3921, 0], [0, 0.3921, 0], [0, 1, 0], [0, 1, 0],
    ]
    
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex in face:
            glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()
    

def sphere(radius, slices, stacks,cor=list):
    for i in range(stacks):
        lat0 = np.pi * (-0.5 + float(i) / stacks)
        z0 = radius * np.sin(lat0)
        zr0 = radius * np.cos(lat0)

        lat1 = np.pi * (-0.5 + float(i + 1) / stacks)
        z1 = radius * np.sin(lat1)
        zr1 = radius * np.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(slices+1):
            lng = 2 * np.pi * float(j) /slices
            x = np.cos(lng)
            y = np.sin(lng)
            glColor3f(*cor)
            glVertex3f(x * zr0, y * zr0, z0)
            glVertex3f(x*zr1, y*zr1, z1)
        glEnd()


class quads:
    def __init__(self,cor):
        self.cor=cor
        
    def desenha(self):
        quadrado(self.cor)

    def mudarCor(self,cor):
        self.cor=cor


def quadrado(color:list):

    vetor=[ [ 0 , 0 ],
            [1, 0 ],
            [1,1],
            [ 0 ,1,]]
    
    glColor3f(*color)
    glBegin(GL_QUADS)
    for i in vetor:
        glVertex2f(i[0],i[1]) 
    glEnd()




  
def circulo(x,y,raio,segments,cor:list):
    glColor3f(*cor)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(segments+1):
        angulo = 2 * np.pi * i / segments
        glVertex2f(x + np.cos(angulo)*raio,y + np.sin(angulo) * raio)
    glEnd()

def circle(radius,cor=list):
        glColor3f(*cor)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, 0)  # Centro do círculo
        for angle in range(361):
            x = math.cos(math.radians(angle)) * radius
            y = math.sin(math.radians(angle)) * radius
            glVertex3f(x, y, 0)
        glEnd()


