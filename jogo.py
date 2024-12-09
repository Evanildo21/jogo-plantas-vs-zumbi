import glfw
from OpenGL.GL import *
import random
import time


class Planta:
    def __init__(self, x, y):
        """Inicializa uma planta na posição dada."""
        self.x = x
        self.y = y
        self.color = (0.0, 0.8, 0.0)  # Verde
        self.projeteis = []  # Lista de projéteis disparados

    def desenhar(self):
        """Desenha a planta como um retângulo."""
        glColor3f(*self.color)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + 0.1, self.y)
        glVertex2f(self.x + 0.1, self.y + 0.2)
        glVertex2f(self.x, self.y + 0.2)
        glEnd()

    def disparar(self):
        """Dispara um projétil."""
        self.projeteis.append(Projeteis(self.x + 0.1, self.y + 0.1))

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
        glColor3f(*self.color)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y - 0.01)
        glVertex2f(self.x + 0.02, self.y - 0.01)
        glVertex2f(self.x + 0.02, self.y + 0.01)
        glVertex2f(self.x, self.y + 0.01)
        glEnd()

    def mover(self):
        """Move o projétil para a direita."""
        self.x += self.velocidade


class Zumbi:
    def __init__(self, x, y):
        """Inicializa um zumbi na posição dada."""
        self.x = x
        self.y = y
        self.color = (0.8, 0.0, 0.0)  # Vermelho
        self.velocidade = 0.0005
        self.vivo = True

    def desenhar(self):
        """Desenha o zumbi como um retângulo."""
        if self.vivo:
            glColor3f(*self.color)
            glBegin(GL_QUADS)
            glVertex2f(self.x, self.y)
            glVertex2f(self.x + 0.1, self.y)
            glVertex2f(self.x + 0.1, self.y + 0.2)
            glVertex2f(self.x, self.y + 0.2)
            glEnd()

    def mover(self):
        """Move o zumbi para a esquerda."""
        if self.vivo:
            self.x -= self.velocidade

    def verificar_colisao(self, projeteis):
        """Verifica se algum projétil colidiu com o zumbi."""
        for proj in projeteis:
            if self.x < proj.x < self.x + 0.1 and self.y < proj.y < self.y + 0.2:
                self.vivo = False
                projeteis.remove(proj)
                break
            
    def get_x(self):
        return self.x
    
     



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
    glClearColor(0.5, 0.7, 1.0, 1.0)
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
    return janela


def loop_principal(janela):
    """Executa o loop principal do jogo."""
    planta = Planta(0.1, 0.4)
    zumbis = [Zumbi(0.9, random.uniform(0.1, 0.7)) for _ in range(3)]
    tempo_de_criar_zumbi = tempo_anterior = time.time()

    while not glfw.window_should_close(janela):
        glClear(GL_COLOR_BUFFER_BIT)

        # Atualiza e desenha a planta e seus projéteis
        planta.desenhar()
        planta.atualizar_projeteis()

        # Atualiza e desenha os zumbis
        for zumbi in zumbis:
            zumbi.mover()
            zumbi.verificar_colisao(planta.projeteis)
            zumbi.desenhar()

        # Faz a planta disparar a cada 1 segundo
        tempo_atual = time.time()
        
        if tempo_atual - tempo_anterior > 1:
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
