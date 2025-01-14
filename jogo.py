import glfw
from OpenGL.GL import *
import random
import time

class seleção:
    def __init__(self,x,y):
        self.x= x
        self.y= y
        self.color = (1, 1, 0)

    def desenha(self):
        vetor=[ [ 0 , 0 ],
                [1, 0 ],
                [1,0.8],
                [ 0 ,0.8,]]
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
                self.y=self.y-1.6
        if key == "ParaCima":
            if self.y < 7:
                self.y=self.y+1.6

        
class gramado:
    def __init__(self,x,y):
        self.x= x
        self.y= y
        self.color = (0.81, 0.6, 0.41)

    def desenha(self):
        vetor=[ [ 0 , 0 ],
                [1, 0 ],
                [1,0.8],
                [ 0 ,0.8,]] 
        glPushMatrix()
        glTranslatef(self.x, self.y,0)
        glColor3f(*self.color)
        glBegin(GL_QUADS)
        for i in vetor:
            glVertex2f(i[0],i[1]) 
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.x, self.y,0)
        glColor3f(0,0,0)
        glBegin(GL_LINE_LOOP)
        for i in vetor:
            glVertex2f(i[0],i[1]) 
        glEnd()
        glPopMatrix()



class girassol:
    def __init__(self, x, y):
        """Inicializa uma planta na posição dada."""
        self.x = x
        self.y = y
        self.color = (0.0, 0.8, 0.0)  # Verde
        self.viva = True
    def p():
        GLUT_LEFT_BUTTON
        

    def desenhar(self):
        """Desenha a planta como um retângulo."""
        if self.viva:
            vetor=[
                [0.0 ,0.0 ],
                [0.1 , 0.0],
                [0.1 , 0.1],
                [0.0 , 0.1],
                ] 
            glColor3f(*self.color)
            glPushMatrix()
            glTranslatef(self.x, self.y,0)
            glBegin(GL_QUADS)
            
            for i in vetor:
                glVertex2f(i[0],i[1])

            glEnd()
            glPopMatrix()
        

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
                [0.6 , 0.0],
                [0.6 , 0.5],
                [0.0 , 0.5],
                ] 
            glColor3f(*self.color)
            glPushMatrix()
            glTranslatef(self.x, self.y,0)
            glBegin(GL_QUADS)
            
            for i in vetor:
                glVertex2f(i[0],i[1])

            glEnd()
            glPopMatrix()
        
    def disparar(self):
        """Dispara um projétil."""
        self.projeteis.append(Projeteis(self.x+1 , self.y+1 ))

    def atualizar_projeteis(self):
        """Atualiza e desenha os projéteis."""
        for proj in self.projeteis:
            proj.mover()
            proj.desenhar()
        # Remove projéteis que saíram da tela
        self.projeteis = [proj for proj in self.projeteis if proj.x < 1.0]
        

class Projeteis:
    def __init__(self, x, y):
        """Inicializa o projétil."""
        self.x = x
        self.y = y
        self.velocidade = 0.02
        self.color = (1.0, 1.0, 0.0)  # Amarelo

    def desenhar(self):
        """Desenha o projétil."""
        vetor=[
            [0    , - 0.1],
            [0.2 , - 0.1],
            [0.2 , 0.1],
            [0    , 0.1],
        ]
        glPushMatrix()
        glTranslatef(self.x, self.y,0)
        glColor3f(*self.color)
        glBegin(GL_QUADS)
        for i in vetor:
            glVertex2f(i[0] , i[1])
        
        glEnd()
        glPopMatrix()
    def mover(self):
        """Move o projétil para a direita."""
        self.x += self.velocidade


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
                [1,2],
                [ 0 ,2],
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
    

plantas=[]    


def selecionador():
    pass


# callback function pressionar de uma tecla
def keyboard(window, key, scancode, action, mods):
    global select,plantas
    if action == glfw.PRESS:   
        if key == glfw.KEY_LEFT:
            select.mudar("ParaEsquerda")
        elif key == glfw.KEY_RIGHT:
            select.mudar("ParaDireita")
        elif key == glfw.KEY_UP:
            select.mudar("ParaCima")
        elif key ==glfw.KEY_DOWN:
            select.mudar("ParaBaixo")
        if key == glfw.KEY_ENTER:
            plantas.append(Planta(select.cordenada_X(),select.cordenada_Y()))
 
    elif action == glfw.RELEASE: pass

def inicializar_janela():
    """Inicializa a janela usando GLFW."""
    if not glfw.init():
        print("Falha ao inicializar GLFW.")
        return None

    janela = glfw.create_window(800, 600, "Plantas vs. Zumbis - GLFW", None, None)
    if not janela:
        glfw.terminate()
        print("Falha ao criar a janela.")
        return None

    glfw.make_context_current(janela)
    glfw.set_key_callback(janela,keyboard)
    glClearColor(0.5, 0.7, 1.0, 1.0)
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
    return janela

select = seleção(-10,1)

def cenario():
    global select
    gramado1=[]
    x=-10
    y=1
    for i in range(5):
        for j in range(9):
            gramado1.append(gramado(x,y))
            x=x+2
        y=y+1.6
        x=-10
        
    for i in gramado1:
       i.desenha()

    select.desenha()





def loop_principal(janela):
    """Executa o loop principal do jogo."""
    #planta = Planta(0.1, 0.4)
    global plantas
    zumbis = [Zumbi(12, random.randrange(1,5)) for _ in range(1)]
    tempo_de_criar_zumbi = tempo_anterior = time.time()


    while not glfw.window_should_close(janela):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)    # modo de matriz: matriz de projeÃ§Ã£o
        glLoadIdentity()               # carregando a matriz identidade
        glOrtho(-12, 12, 0, 12, -1,1)  # definindo a matriz de projeÃ§Ã£o ortogrÃ¡fica (paralela)
                                   # glOrtho(left, right, bottom, top, near, far)
        cenario()
        
        # Atualiza e desenha a planta e seus projéteis
        for planta in plantas:
            planta.desenhar()
            planta.atualizar_projeteis()

        # Atualiza e desenha os zumbis
        for zumbi in zumbis:
            zumbi.mover()
            for planta in plantas:
                zumbi.verificar_colisao_Projeteis(planta.projeteis)

            zumbi.desenhar()

        # Faz a planta disparar a cada 1 segundo
        tempo_atual = time.time()
        
        if tempo_atual - tempo_anterior > 1:
            for planta in plantas:
                planta.disparar()


            tempo_anterior = tempo_atual

        if tempo_atual - tempo_de_criar_zumbi > 6:
            zumbis.append(Zumbi(0.9, random.uniform(0.1, 0.7)))
            tempo_de_criar_zumbi = tempo_atual

        glfw.swap_buffers(janela)
        glfw.poll_events()
        time.sleep(1 / 60)
        
    glfw.terminate()


def main():
    janela = inicializar_janela()
    if janela: 
        loop_principal(janela)


if __name__ == "__main__":
    main()
