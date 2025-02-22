import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np



class Camera:
    def __init__(self):
        self.rotation_index = False
        self.angle=0
        self.x=0
        self.z=0
    def get_rotacao_camera(self):
        return self.rotation_index
    
    def exibir_camera(self):
        
        vetor=[ [ 1 ,3.5, 14 ],
                [ 0 , 0 ,-1.0],
                [0.0,1.0, 0.0]]
        
        c=[x + y for x,y in zip(vetor[0],vetor[1])]
        
        if self.rotation_index == True:
            self.d_input()
        else:
            if self.angle != 0 or self.x != 0:
                self.volta_input()

        gluLookAt(vetor[0][0],vetor[0][1],vetor[0][2],c[0],c[1],c[2],vetor[2][0],vetor[2][1],vetor[2][2])


    def d_input(self):
        
        if self.x<13:
            self.x+=1
            self.z-=1
        if self.angle < 90:
            self.angle+=7
        if self.x>=13 and self.z<(-13+0):
          self.z+=1
        glTranslated(self.x,1,self.z)
        glRotatef(self.angle,0,1,0)


    def volta_input(self):
        
        if self.x != 0:
            self.x-=1
        if self.z != -1:
            self.z+=1
        if self.angle >6.9:
            self.angle-=6.9
        
        glTranslated(self.x,0.1,self.z)
        glRotatef(self.angle,0,1,0)
        
    
    def process_input(self):
        self.rotation_index = not self.rotation_index
        