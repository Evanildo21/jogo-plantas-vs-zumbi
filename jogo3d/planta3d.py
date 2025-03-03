from formas import *
import random
 

        
class Planta:
    def __init__(self, x, y,z):
        """Inicializa uma planta na posição dada."""
        self.x = x
        self.y = y
        self.z= z
        self.color = [0.0, 0.8, 0.0] # Verde
        self.projeteis = []  # Lista de projéteis disparados
        self.viva = True
        self.controle=False
        self.dano_sofrido=0
        self.tipo='tiro'

    def desenhar(self):
        glPushMatrix()
        glTranslatef(self.x,self.y,self.z)
        glScale(0.2,0.5,0.2)
        cube(self.color)
        glPopMatrix()
        glPushMatrix()

        glTranslatef(self.x+0.2,self.y+0.4,self.z)
        glRotatef(40,0,1,0)
        glScale(0.1,0.1,0.1)
        piramide()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.x,self.y+0.4,self.z)
        cor=[0.1,0.4,0]
        sphere(0.2,8,8,cor)
        glPopMatrix()
        
    def disparar(self):
        """Dispara um projétil."""
        self.projeteis.append(Projeteis(self.x+0.3, self.y+0.7 ,self.z ))

    def atualizar_projeteis(self,cordenadas=(0,0,0)):
        """Atualiza e desenha os projéteis."""
        x,y,z=cordenadas
        if len(self.projeteis):
            for proj, i in zip(self.projeteis,range(len(self.projeteis))):
                proj.mover(self.controle,x,z)
                proj.desenhar()
                if proj.x >9:
                    self.projeteis.pop(i)
    def controlar(self):
        self.controle= not self.controle

    def sofrer_dano(self,dano):
        self.dano_sofrido+=dano
        if self.dano_sofrido >= 5:
            self.viva = False
        return self.viva

    


class Projeteis:
    def __init__(self, x, y,z):
        """Inicializa o projétil."""
        self.x = x
        self.y = y
        self.z= z
        self.velocidade = 0.3
        self.color = [0.0, 1.0, 0.3]  # Amarelo

    def desenhar(self):
        """Desenha o projétil."""
       
        glPushMatrix()
       
        glTranslatef(self.x,self.y,self.z)
       
        sphere(0.1,8,8,self.color)

        glPopMatrix()

    def mover(self,controle,x,z):
        """Move o projétil para a direita."""
        if controle:
            self.x += self.velocidade
            if z > self.z:
                self.z += self.velocidade
            else:
                self.z -= self.velocidade
            
        else:
            self.x += self.velocidade


class Girasol:
    def __init__(self, x, y,z):
        """Inicializa uma planta na posição dada."""
        self.x = x
        self.y = y
        self.z= z
        self.color = [0.0, 0.8, 0.0] # Verde
        self.marrom= [0.6, 0.4, 0.2]
        self.c=[1.0, 0.7, 0.0]
        self.listaDeSol=[]
        self.dano_sofrido=0
        self.viva = True
        self.tipo='girasol'

    def desenhar(self):
        glPushMatrix()
        glTranslatef(self.x,self.y,self.z)
        glScalef(0.2,0.5,0.2)
        cube(self.color)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.x,self.y+0.4,self.z)
       
        sphere(0.2,8,8,self.marrom)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.x+0.1,self.y+0.4,self.z)
        glRotatef(20,0,0,1)
        glRotatef(90,0,1,0)
        self.petalas()
        glPopMatrix()
        self.printSol()

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

    def sofrer_dano(self,dano):
        self.dano_sofrido+=dano
        if self.dano_sofrido >= 5:
            self.viva = False
        return self.viva
    
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

class planta_barreira:
    def __init__(self, x, y,z):
        """Inicializa uma planta na posição dada."""
        self.x = x
        self.y = y
        self.z= z
        self.color = [0.0, 0.8, 0.0] # Verde
        self.projeteis = []  # Lista de projéteis disparados
        self.viva = True
        self.dano_reserva=0
        self.dano_sofrido=0
        self.tipo='barreira'

    def desenhar(self):
        for i in range(1,9-int(self.dano_reserva)):
            self.formar_barreira(i)

    def formar_barreira(self,i):
        if i == 1:
            glPushMatrix()
            glTranslatef(self.x,self.y,self.z)
            glScalef(0.3,0.3,0.3)
            cube(self.color)
            glPopMatrix()
        if i == 2:
            glPushMatrix()
            glTranslatef(self.x-0.3,self.y,self.z)
            glScalef(0.3,0.3,0.3)
            cube(self.color)
            glPopMatrix()
        if i == 3:
            glPushMatrix()
            glTranslatef(self.x-0.3,self.y,self.z-0.3)
            glScalef(0.3,0.3,0.3)
            cube(self.color)
            glPopMatrix()
        if i == 4:
            glPushMatrix()
            glTranslatef(self.x,self.y,self.z-0.3)
            glScalef(0.3,0.3,0.3)
            cube(self.color)
            glPopMatrix()
        if i == 5:
            glPushMatrix()
            glTranslatef(self.x,self.y+0.3,self.z)
            glScalef(0.3,0.3,0.3)
            cube(self.color)
            glPopMatrix()
        if i == 6:
            glPushMatrix()
            glTranslatef(self.x-0.3,self.y+0.3,self.z)
            glScalef(0.3,0.3,0.3)
            cube(self.color)
            glPopMatrix()
        if i == 7:
            glPushMatrix()
            glTranslatef(self.x-0.3,self.y+0.3,self.z-0.3)
            glScalef(0.3,0.3,0.3)
            cube(self.color)
            glPopMatrix()
        if i == 8:
            glPushMatrix()
            glTranslatef(self.x,self.y+0.3,self.z-0.3)
            glScalef(0.3,0.3,0.3)
            cube(self.color)
            glPopMatrix()

    def sofrer_dano(self,dano):
        self.dano_sofrido+=dano
        if self.dano_sofrido >= 5:
            self.dano_reserva+=dano
            if self.dano_reserva >= 5:
                self.viva = False
        return self.viva
        

    