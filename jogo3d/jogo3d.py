import glfw
from planta3d import *
from cenario import *
from camera import *
import time
angle = 0


def keyboard(window, key, scancode, action, mods):
    global angle,plantas,girasol
    if action == glfw.PRESS:
        if key == glfw.KEY_LEFT:
            selector("ParaEsquerda")
        if key == glfw.KEY_RIGHT:
            selector("ParaDireita")
        if key == glfw.KEY_UP:
            selector("ParaCima")
        if key ==glfw.KEY_DOWN:
            selector("ParaBaixo")
        if key == glfw.KEY_SPACE:
            process_input()
        if key == glfw.KEY_ENTER:
            x,y,z=cordenadasDoSeletor()
            plantas.append(Planta(x,y,z))
        if key == glfw.KEY_BACKSPACE:
            x,y,z=cordenadasDoSeletor()
            girasol.append(Girasol(x,y,z))
        
    elif action == glfw.RELEASE: pass

if not glfw.init():
    raise Exception("Falha ao iniciar")

width, height = 800, 600
window = glfw.create_window(width, height, "Aula 3", None, None)
if not window:
    raise Exception("Falha ao criar a janela")



glfw.make_context_current(window)
glfw.set_key_callback(window,keyboard)
glEnable(GL_DEPTH_TEST)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, width / height, 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)




glClearColor(1, 1, 0.8, 1)



plantas=[]  
girasol=[]
tempo_de_criar_zumbi = tempo_anterior = time.time()


while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    camera()
    cenario()
    
    for planta in plantas:
        planta.desenhar()
        planta.atualizar_projeteis()
        
    for g in girasol:
        g.desenha()
        g.printSol()
    
    # Faz a planta disparar a cada 1 segundo
    
    tempo_atual = time.time()
   
    if (tempo_atual - tempo_anterior) > 3 : 
        for planta in plantas:
            planta.disparar()
        for plantagirasol in girasol:
            plantagirasol.absorverLuzDoSol()
            plantagirasol.atualisarSol()
           
                
        

        tempo_anterior = tempo_atual
        
    


     
    glfw.swap_buffers(window)    
    time.sleep(1/60)
    glfw.poll_events()
    
glfw.terminate()