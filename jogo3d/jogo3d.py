import glfw
from cenario import *
from camera import *
import time

menu=False


def keyboard(window, key, scancode, action, mods):
    global menu,plantas,girasol
    rotacaoDaCamera=get_rotacao_camera()
    if action == glfw.PRESS:
        if rotacaoDaCamera == True:

                if key == glfw.KEY_LEFT:
                    selector("ParaEsquerda",rotacaoDaCamera)
                if key == glfw.KEY_RIGHT:
                    selector("ParaDireita",rotacaoDaCamera)
                if key == glfw.KEY_UP:
                    selector("ParaCima",rotacaoDaCamera)
                if key ==glfw.KEY_DOWN:
                    selector("ParaBaixo",rotacaoDaCamera)
        if rotacaoDaCamera == False:
            if menu == False:
                if key == glfw.KEY_LEFT:
                    selector("ParaEsquerda",rotacaoDaCamera)
                if key == glfw.KEY_RIGHT:
                    selector("ParaDireita",rotacaoDaCamera)
                if key == glfw.KEY_UP:
                    selector("ParaCima",rotacaoDaCamera)
                if key ==glfw.KEY_DOWN:
                    selector("ParaBaixo",rotacaoDaCamera)
            
            if menu == True:
                if key == glfw.KEY_LEFT:
                    selector_Menu("ParaEsquerda")
                if key == glfw.KEY_RIGHT:
                    selector_Menu("ParaDireita") 
            
            if key == glfw.KEY_ENTER:
                    if menu==False:
                        menu=True
                    else:
                        num=get_selector_Menu()
                        x,y,z=cordenadasDoSeletor()
                        if num ==0:   
                            plantas.append(Planta(x,y,z))
                        if num == 1:
                            girasol.append(Girasol(x,y,z))
                        menu=False 

        if key == glfw.KEY_SPACE:
            process_input()

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
    if menu==True:
        Menu()
    
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