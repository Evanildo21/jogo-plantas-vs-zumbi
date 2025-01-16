from formas import *
 

class planta:
    def __init__(self, x, y,z):
        """Inicializa uma planta na posição dada."""
        self.x = x
        self.y = y
        self.z= z
        self.color = (0.0, 0.8, 0.0)  # Verde
        self.projeteis = []  # Lista de projéteis disparados
        self.viva = True
    
    def desenha(self):
        glPushMatrix()
        glTranslatef(self.x,self.y,self.z)
        glScale(1,2,1)
        cube()
        glPopMatrix()
        glPushMatrix()

        glTranslatef(self.x+0.5,self.y+1.3,self.z)
        glRotatef(60,0,1,0)
        glScale(0.3,0.3,0.3)
        piramide()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.x,self.y+1.3,self.z)
        glScale(0.06,0.06,0.06)
        sphere(10,20,20)
        glPopMatrix()