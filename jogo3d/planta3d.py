from formas import *
import random
 

class Planta:
    def __init__(self, x, y,z):
        """Inicializa uma planta na posição dada."""
        self.x = x
        self.y = y
        self.z= z
        self.color = [[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0]] # Verde
        self.projeteis = []  # Lista de projéteis disparados
        self.viva = True

    def desenhar(self):
        glPushMatrix()
        glTranslatef(self.x,self.y,self.z)
        glScale(0.2,1,0.2)
        cube(self.color)
        glPopMatrix()
        glPushMatrix()

        glTranslatef(self.x+0.2,self.y+0.7,self.z)
        glRotatef(40,0,1,0)
        glScale(0.1,0.1,0.1)
        piramide()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.x,self.y+0.7,self.z)
        cor=[0.1,0.4,0]
        sphere(0.2,8,8,cor)
        glPopMatrix()
        
    def disparar(self):
        """Dispara um projétil."""
        self.projeteis.append(Projeteis(self.x+0.3, self.y+0.7 ,self.z ))

    def atualizar_projeteis(self):
        """Atualiza e desenha os projéteis."""
        for proj in self.projeteis:
            proj.mover()
            proj.desenhar()
        # Remove projéteis que saíram da tela
        self.projeteis = [proj for proj in self.projeteis if proj.x < 12]


class Projeteis:
    def __init__(self, x, y,z):
        """Inicializa o projétil."""
        self.x = x
        self.y = y
        self.z= z
        self.velocidade = 0.3
        self.color = (0.0, 1.0, 0.3)  # Amarelo

    def desenhar(self):
        """Desenha o projétil."""
       
        glPushMatrix()
       
        glTranslatef(self.x,self.y,self.z)
       
        sphere(0.1,8,8,self.color)

        glPopMatrix()

    def mover(self):
        """Move o projétil para a direita."""
        self.x += self.velocidade

class Girasol:
    def __init__(self, x, y,z):
        """Inicializa uma planta na posição dada."""
        self.x = x
        self.y = y
        self.z= z
        self.color = [[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0],[0.0, 0.8, 0.0]] # Verde
        self.marrom= [0.6, 0.4, 0.2]
        self.c=[1.0, 0.7, 0.0]
        self.listaDeSol=[]

    def desenha(self):
        glPushMatrix()
        glTranslatef(self.x,self.y,self.z)
        glScalef(0.2,1,0.2)
        cube(self.color)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.x,self.y+0.7,self.z)
       
        sphere(0.2,8,8,self.marrom)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.x+0.1,self.y+0.7,self.z)
        glRotatef(20,0,0,1)
        glRotatef(90,0,1,0)
        self.petalas()
        glPopMatrix()

    def petalas(self):
        num_petals = 20
        petal_radius = 0.15
        for i in range(num_petals):
            angle = i * (360 / num_petals)
            glPushMatrix()
            glRotatef(angle, 0, 0, 1)
            glTranslatef(0.25, 0, 0)  # Move para a borda do centro
            
            circle(petal_radius,self.c )  # Amarelo para as pétalas
            glPopMatrix()
    
    def absorverLuzDoSol(self):
        if self.c[1]>=1:
            x=round(random.uniform(self.x,self.x + 1.3),2)
            z=round(random.uniform(self.z,self.z + 1.3),2)
            self.listaDeSol.append(Sol(x,self.y+0.1,z))
            self.c[1] = 0.7
        else:
            self.c[1]+=0.1

    def printSol(self):
        if len(self.listaDeSol) > 0:
            for sol in self.listaDeSol:
                if sol.get_tempo() !=0:
                    sol.desenha()
                    
                
    def atualisarSol(self):
        if len(self.listaDeSol) > 0:
            for sol,t in zip(self.listaDeSol,range(len(self.listaDeSol))):
                if sol.get_tempo() !=0:
                    sol.set_tempo(1)
                else:
                    self.listaDeSol.pop(t)

class Sol:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.tempo=10
        self.cor=[1,1,0]

    def desenha(self):
        glPushMatrix()
        glTranslatef(self.x+0.15,self.y,self.z+0.15)
        sphere(0.1,8,8,self.cor)
        glPopMatrix()
    
    def get_tempo(self)->int:
        return self.tempo
    
    def set_tempo(self,t):
        self.tempo-=t

    