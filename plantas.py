from OpenGL.GL import *
import numpy as np

class Planta:
    def __init__(self, x, y):
        """Inicializa uma planta na posição dada."""
        self.x = x
        self.y = y
        self.color = (0.0, 0.8, 0.0)  # Verde
        self.projeteis = []  # Lista de projéteis disparados
        self.viva = True

    def desenhar(self):
        """Desenha a planta como um retângulo."""
        if self.viva:
            vetor=[
                [0.0 ,0.0 ],
                [0.5, 0.0],
                [0.5 , 0.8],
                [0.0 , 0.8],
                ] 
            glColor3f(*self.color)
            glPushMatrix()
            glTranslatef(self.x, self.y,0)
            glBegin(GL_QUADS)
            
            for i in vetor:
                glVertex2f(i[0],i[1])

            glEnd()
            glPopMatrix()

            glColor3f(0.5,1,0)
            glPushMatrix() 
            glTranslatef(self.x, self.y+0.3, 0)
            glScale(0.9,0.4,0)
            glBegin(GL_QUADS)
            for vertice in vetor:
                glVertex2f(vertice[0], vertice[1])
            glEnd()
            glPopMatrix()

            glColor3f(0,1,0)
            glPushMatrix() 
            glTranslatef(self.x, self.y+0.3, 0)
            glRotatef(180,0,1,0)
            glScale(0.5,0.2,0)
            glBegin(GL_TRIANGLES)
            for vertice in vetor:
                glVertex2f(vertice[0], vertice[1])
            glEnd()
            glPopMatrix()
            
           
        
    def disparar(self):
        """Dispara um projétil."""
        self.projeteis.append(Projeteis(self.x + 1, self.y + 0.5))

    def atualizar_projeteis(self):
        """Atualiza e desenha os projéteis."""
        for proj in self.projeteis:
            proj.mover()
            proj.desenhar()
        # Remove projéteis que saíram da tela
        self.projeteis = [proj for proj in self.projeteis if proj.x < 12]


class Projeteis:
    def __init__(self, x, y):
        """Inicializa o projétil."""
        self.x = x
        self.y = y
        self.velocidade = 0.1
        self.color = (0.0, 1.0, 0.3)  # Amarelo

    def desenhar(self):
        """Desenha o projétil."""
        vetor=[
            [0    , - 0.1],
            [0.2 , - 0.1],
            [0.2 , 0.1],
            [0    , 0.1],
        ]
        
        glPushMatrix()
        segments=50
        raio=0.1
        glTranslatef(self.x,self.y+0.8,0)
        glColor3f(*self.color)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(0,0)
        for i in range(segments+1):
            angulo = 2 * np.pi * i / segments
            glVertex2f(0+ np.cos(angulo)*raio,0 + np.sin(angulo) * raio)

        glEnd()
        glPopMatrix()

    def mover(self):
        """Move o projétil para a direita."""
        self.x += self.velocidade


class girassol:
    def __init__(self, x, y):
        """Inicializa uma planta na posição dada."""
        self.x = x
        self.y = y
        self.color = (0.59,0.41,0.30)  # marrom
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
            glScale(-0.5,0,0)
            glBegin(GL_QUADS)
            for i in vetor:
                glVertex2f(i[0],i[1])
            glEnd()
            glPopMatrix()

           
    def petala(self):
        glPushMatrix()
        segments=50
        raio=0.5
        glTranslatef(self.x,self.y+0.8,0)
        glColor3f(1,1,0)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(0,0)
        for i in range(segments+1):
            angulo = 2 * np.pi * i / segments
            glVertex2f(0+ np.cos(angulo)*raio,0 + np.sin(angulo) * raio)
        glEnd()
        glPopMatrix()
        
    def desenharSol():
        pass

    def gerarsol():
        pass