import glfw
from cenario import *
from camera import *
import time
from zumbi3d import *
menu=False


def keyboard(window, key, scancode, action, mods):
    global menu,plantas,girasol
    rotacaoDaCamera=get_rotacao_camera()
    if action == glfw.PRESS:

        if menu == False:
            if key == glfw.KEY_LEFT:
                selector("ParaEsquerda",rotacaoDaCamera)
            if key == glfw.KEY_RIGHT:
                selector("ParaDireita",rotacaoDaCamera)
            if key == glfw.KEY_UP:
                selector("ParaCima",rotacaoDaCamera)
            if key ==glfw.KEY_DOWN:
                selector("ParaBaixo",rotacaoDaCamera)
        if rotacaoDaCamera == False: 
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
                        if num == 2:
                            defesa.append(planta_barreira(x,y,z))
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


defesa=[]
plantas=[]  
girasol=[]
tempo_inteligente=0
tempo_de_criar_zumbi = tempo_anterior = time.time()
zumbis = []
posicaoz=[-1,0.1,1.2,2.3,3.3]
i = int(random.uniform(0,4))
zumbis.append(Zumbi_normal(10,0.6,posicaoz[i]))
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    camera()
    cenario()
    if menu==True:
        Menu()
  
    for zumbi in zumbis:
        zumbi.desenhar()
        for planta in plantas:
           zumbi.verificar_colisao_Projeteis(planta.projeteis)
        zumbi.mover(plantas)
        
    for planta in defesa:
        planta.desenhar()

    for planta in plantas:
        planta.desenhar()
        planta.atualizar_projeteis()
        
    for g in girasol:
        g.desenhar()
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

    
    if tempo_atual - tempo_de_criar_zumbi > 6:
        i = int(random.uniform(0,4))
        zumbis.append(Zumbi_normal(10,0.6,i))
        tempo_de_criar_zumbi = tempo_atual
        tempo_inteligente+=1

    if tempo_inteligente == 6:
        i = int(random.uniform(0,4))
        zumbis.append(Zumbi_inteligente(10,0.6,i))
        tempo_inteligente=0

             
    glfw.swap_buffers(window)    
    time.sleep(1/60)
    glfw.poll_events()
    
glfw.terminate()