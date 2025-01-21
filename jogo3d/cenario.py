from formas import *
from OpenGL.GL import *

class seleção:
    def __init__(self,x,y):
        self.x= x
        self.y= y
        self.color = (1, 1, 0)

    def desenha(self):
        vetor=[ [ 0 , 0 ],
                [1, 0 ],
                [1,1],
                [ 0 ,1,]]
        
        glPushMatrix()
        glTranslatef(self.x, self.y,0)
        glColor3f(*self.color)
        glBegin(GL_QUADS)
        for i in vetor:
            glVertex2f(i[0],i[1]) 
        glEnd()
        glPopMatrix()

       
    def cordenada_X(self)->int:
        return self.x+0.3
    
    def cordenada_Y(self)->int:
        return self.y+0.3
    
    def mudar(self,key):
        if key =="ParaEsquerda":
            if self.x > -10:
                self.x=self.x-2
        if key =="ParaDireita":
            if self.x < 6:
                self.x=self.x+2
        if key == "ParaBaixo":
            if self.y > 2:
                self.y=self.y-2
        if key == "ParaCima":
            if self.y < 9:
                self.y=self.y+2


