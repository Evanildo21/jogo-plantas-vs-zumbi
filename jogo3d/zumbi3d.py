from OpenGL.GL import *
from formas import *
from cenario import *

class Zumbi:
    def desenhar(self):
        """Desenha o zumbi como um retângulo."""
        if self.vivo:
            glPushMatrix()
            glTranslatef(self.x, self.y,self.z)
            glScalef(0.3,1,0.3)
            cube(self.color)
            glPopMatrix()
            return True
        else:
            return False

    def verificar_colisao_Projeteis(self, projeteis):
        """Verifica se algum projétil colidiu com o zumbi."""
        if self.vivo==True:
            for proj,i in zip(projeteis,range(len(projeteis))):
                if self.x < proj.x < self.x + 0.55 and self.z <= proj.z <= self.z +0.5 :
                    projeteis.remove(proj)
                    self.dano_sofrido += 1
                    if self.dano_sofrido == 5:
                        self.vivo = False

    def verificar_colisao_Planta(self, planta):
        if planta != None:
            distancia = ((planta.x - self.x) ** 2 + (planta.z - self.z) ** 2) ** 0.5
            return distancia < 0.5  # Considerando um raio de colisão
        
    def encontrar_planta_mais_proxima(self, plantas):
        if not plantas:
            return None
        return min(plantas, key=lambda p: (p.x - self.x) ** 2 + (p.z - self.z) ** 2)

class Zumbi_normal(Zumbi):
    def __init__(self, x, y, z):  
        self.x = x
        self.y = y
        self.z = z
        self.color = [[0.8, 0.0, 0.0]]*6  # Vermelho
        self.velocidade = 0.05
        self.vivo = True
        self.dano_sofrido = 0
    
    def mover(self,planta):
        """Move o zumbi para a esquerda."""
        if self.vivo:   
            if len(planta):
                auvo=self.planta_no_mesmo_eixo_x(planta)
                if auvo and self.verificar_colisao_Planta(auvo):
                    self.atacar(auvo)       
                else:
                    self.x -= self.velocidade
            else:
                self.x -= self.velocidade
   
    def planta_no_mesmo_eixo_x(self, plantas):
        lista=[]
        for i in plantas:
            if int(i.z) == int(self.z):  
                lista.append(i)
        if len(lista):
            return max(lista, key=lambda p:p.x)
        else: 
            return None
        
    def atacar(self,auvo):
        atack =0.05
        atacar_planta(chave(auvo.x,auvo.y,auvo.z),atack)

   
            
    def get_x(self):
        return self.x
    
class Zumbi_inteligente(Zumbi):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.color = [[1, 0.0, 1]]*6  # Vermelho
        self.velocidade = 0.05
        self.vivo = True
        self.dano_sofrido = 0

    def mover(self, plantas):
        if self.vivo:
            alvo = self.encontrar_planta_mais_proxima(plantas)
            if alvo:
                self.velocidade=0.1
                dx = alvo.x - self.x
                dz = alvo.z - self.z
                distancia = (dx**2 + dz**2) ** 0.5
                if distancia > 0:
                    self.x += self.velocidade * (dx / distancia)
                    self.z += self.velocidade * (dz / distancia)
            else:
                self.x-=self.velocidade

    
