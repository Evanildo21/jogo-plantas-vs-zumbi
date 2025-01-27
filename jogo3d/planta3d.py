from formas import *
 

class planta:
    def __init__(self, x, y,z):
        """Inicializa uma planta na posição dada."""
        self.x = x
        self.y = y
        self.z= z
        self.color = [[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0]] # Verde
        self.projeteis = []  # Lista de projéteis disparados
        self.viva = True
    
    def desenha(self):
        glPushMatrix()
        glTranslatef(self.x,self.y,self.z)
        glScale(0.5,1,0.5)
        cube(self.color)
        glPopMatrix()
        glPushMatrix()

        glTranslatef(self.x+0.3,self.y+0.7,self.z)
        glRotatef(40,0,1,0)
        glScale(0.1,0.1,0.1)
        piramide()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.x,self.y+0.7,self.z)
      
        sphere(0.3,8,8)
        glPopMatrix()