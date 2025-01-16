from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def cube():
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
    colors = [
        [0, 0.3921, 0], [0, 0.3921, 0], [0, 0.3921, 0], [0, 0.3921, 0], [0.7,1,0], [0.7,1,0], [0.7,1,0], [0.7,1,0]
    ]
   
    glScale(1,1,1)
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
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
    

def sphere(radius, slices, stacks):
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
            glColor3f(0.1,0.4,0)
            glVertex3f(x * zr0, y * zr0, z0)
            glVertex3f(x*zr1, y*zr1, z1)
        glEnd()
