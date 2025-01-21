import numpy as np
from OpenGL.GL import *
import math

class girassol:
    def __init__(self, x, y):
        """Inicializa uma planta na posição dada."""
        self.x = x
        self.y = y
        self.color = (0.59,0.41,0.30)  # marrom
        self.corp=(1,1,0)
        self.corcentro=(0.85,0.52,0.09)
        self.viva = True
    
    def desenhar(self):
        """Desenha a planta como um retângulo."""
        if self.viva:
            vetor=[
                [0,0],
                [1,0],
                [1,1],
                [0,1],
                ] 
            glColor3f(*self.color)
            glPushMatrix()
            glTranslatef(self.x, self.y,0)
            glScale(0.5,1,0)
            glBegin(GL_QUADS)
            for i in vetor:
                glVertex2f(i[0],i[1])
            glEnd()
            glPopMatrix()

            glPushMatrix()
            glTranslatef(self.x+2,self.y+3.5,0)
            glScale(2,2,0)
            self.petala()
            core_color = (0.6, 0.3, 0.0)  # Marrom
            self.criar_circulo(0, 0, 0.15, core_color)
            glPopMatrix()
            
            self.ponto(0.7,2.7)
          
          
           
    def petala(self):
        petal_color = (1.0, 0.8, 0.0)  # Amarelo
        for angle in range(0, 360, 30):  # 12 pétalas espaçadas uniformemente
            rad = math.radians(angle)
            x = math.cos(rad) * 0.15
            y = math.sin(rad) * 0.15
            self.criar_circulo(x, y, 0.1, petal_color)
        
    def desenharSol():
        pass
    
    def criar_circulo(self,x, y, radius, color):
        glColor3f(*color)  # Define a cor
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x, y)  # Centro do círculo
        for angle in range(361):  # Desenha o contorno
            rad = math.radians(angle)
            glVertex2f(x + math.cos(rad) * radius, y + math.sin(rad) * radius)
        glEnd()


    def gerarsol():
        pass

    def ponto(self,x,y):
        glColor3f(0,0,0)
        glPointSize(5.0)
       
        glTranslatef(x,y,0)
        glBegin(GL_POINTS)
        glVertex2f(0,0)
        glVertex2f(0.3,0)
        glEnd()        
