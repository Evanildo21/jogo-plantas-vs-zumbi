from OpenGL.GL import *

class Zumbi:
    def __init__(self, x, y):
        """Inicializa um zumbi na posição dada."""
        self.x = x
        self.y = y
        self.color = (0.8, 0.0, 0.0)  # Vermelho
        self.velocidade = 0.005
        self.vivo = True
        self.dano_sofrido = 0

    def desenhar(self):
        """Desenha o zumbi como um retângulo."""
        if self.vivo:
            vetor = [
                [ 0 , 0 ],
                [1, 0 ],
                [1,1 ],
                [ 0 ,1],
            ]
            glPushMatrix()
            glTranslatef(self.x, self.y,0)
            glColor3f(*self.color)
            glBegin(GL_QUADS)
            for i in vetor:
                glVertex2f(i[0],i[1])
                
            glEnd()
            glPopMatrix()

    def mover(self):
        """Move o zumbi para a esquerda."""
        if self.vivo:
            self.x -= self.velocidade

    def verificar_colisao_Projeteis(self, projeteis):
        """Verifica se algum projétil colidiu com o zumbi."""
        if self.vivo==True:
            for proj in projeteis:
                if self.x < proj.x < self.x + 0.1 and self.y < proj.y < self.y + 0.2:
                    self.dano_sofrido = self.dano_sofrido + 1
                    if self.dano_sofrido == 5:
                        self.vivo = False
                        projeteis.remove(proj)
                        break

    def verificar_colisao_Planta(self, Planta):
        pass

    def verificar_colisao_casa(self):
        pass
            
    def get_x(self):
        return self.x
    
