from formas import *
from OpenGL.GL import *
from formas import *

class seleção:
    def __init__(self,x,y,z):
        self.x= x
        self.y= y
        self.z=z
        self.color = [[1, 1, 0],[1, 1, 0],[1, 1, 0],[1, 1, 0],[1, 1, 0],[1, 1, 0],[1, 1, 0],[1, 1, 0]]
      
    def desenha(self):   
        glPushMatrix()
        glTranslatef(self.x, self.y,self.z)
        glScalef(1,0,1)
        quadrado(self.color[1])
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


       
class gramado:
    def __init__(self,x,y):
        self.x= x
        self.y= y
        self.color = [[0.81, 0.6, 0.41],[0.81, 0.6, 0.41],[0.81, 0.6, 0.41],[0.81, 0.6, 0.41],[0.81, 0.6, 0.41],[0.81, 0.6, 0.41],[0.81, 0.6, 0.41],[0.81, 0.6, 0.41]]

    def desenha(self):
        
        glPushMatrix()
        glTranslatef(self.x, 0,self.y)
        glScalef(1,0.1,1)
        cube(self.color)
        glPopMatrix()

    
selecionador=seleção(-5.45,-4.45,0.1)

def criar_cenario():
    cor=[[0.18,0.55,0.34],[0.53,0.81,0.92],[1,1,0]]
    glPushMatrix()
    glTranslatef(0,5,-1.9)
    circulo(0,0,1,40,cor[2])
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-9,0.3,-2)
    glScalef(20,10,0)
    quadrado(cor[1])
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-9,0,5)
    glRotatef(270,1,0,0)
    glScalef(20,10,14)
    quadrado(cor[0])
    glPopMatrix()
    gramado1=[]
    x=-4
    y=-1
    for i in range(5):
        for j in range(9):
            gramado1.append(gramado(x,y))
            x=x+1.2
        y=y+1.2
        x=-4
        
    for i in gramado1:
       i.desenha()

    selecionador.desenha()

def cenario():
    criar_cenario()
    


     
def menu():
    s=seleção(-4,-1,1.5)
    glPushMatrix()
    glTranslatef(-4.5,-1.5,1)
    glScalef(8.2,0,3)
    quadrado([0,1,0.5])
    glPopMatrix()

    x=-4
    y=-1
    while(y<1):
        while(x<3):
            glPushMatrix()
            glTranslatef(x,y,1.1)
            quadrado([1,1,1])
            glPopMatrix()
            x+=1.5
        x=-4
        y+=1.2

    s.desenha()





