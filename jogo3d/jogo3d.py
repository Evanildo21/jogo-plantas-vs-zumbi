import glfw
from cenario import *
from camera import *
import time
from zumbi3d import *
from iluminacao import iluminacao
menu=False
seletor=False

def chave(x,y,z)->float:
    return  x*z

plantas={}
def keyboard(window, key, scancode, action, mods):
    global menu,plantas,girasol,cam,seletor
    rotacaoDaCamera=cam.get_rotacao_camera()
    if action == glfw.PRESS:
        if rotacaoDaCamera == True: 
            if key == glfw.KEY_ENTER:
                modo_de_atack()
                seletor= not seletor
                x,y,z=cordenadasDoSeletor(1)
                plantas[chave(x,y,z)].controlar()

        if menu == False:
            if key == glfw.KEY_LEFT:
                selector("ParaEsquerda",rotacaoDaCamera,seletor)
            if key == glfw.KEY_RIGHT:
                selector("ParaDireita",rotacaoDaCamera,seletor)
            if key == glfw.KEY_UP:
                selector("ParaCima",rotacaoDaCamera,seletor)
            if key ==glfw.KEY_DOWN:
                selector("ParaBaixo",rotacaoDaCamera,seletor)
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
                        x,y,z=cordenadasDoSeletor(1)
                        if num ==0:   
                            plantas[chave(x,y,z)]=Planta(x,y,z)
                        if num == 1:
                            girasol.append(Girasol(x,y,z))
                        if num == 2:
                            defesa.append(planta_barreira(x,y,z))
                        menu=False 

        if key == glfw.KEY_SPACE:
            cam.process_input()

    elif action == glfw.RELEASE: pass 


if not glfw.init():
    raise Exception("Falha ao iniciar")

width, height = 800, 600
window = glfw.create_window(width, height, "Planta vs zumbi", None, None)
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
 
girasol=[]
tempo_inteligente=0
tempo_de_criar_zumbi = tempo_anterior = time.time()
zumbis = []
posicaoz=[-1,0.1,1.2,2.3,3.3]
luz = iluminacao()
cam=Camera()

i = int(random.uniform(0,4))
zumbis.append(Zumbi_normal(10,0.6,posicaoz[i]))
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    cam.exibir_camera()
    cenario()
    luz.configurar_luz_potual(GL_LIGHT1, [3, 6, 14], [1, 1, 1], 0.5)
    

    if menu==True:
        Menu()
  
    for zumbi in zumbis:
        zumbi.desenhar()
        for _,planta in plantas.items():
           zumbi.verificar_colisao_Projeteis(planta.projeteis)
        zumbi.mover(list(plantas.values()))
        
    for planta in defesa:
        planta.desenhar()

    for _,planta in plantas.items():
        planta.desenhar()
        if planta.controle:
            planta.atualizar_projeteis(cordenadasDoSeletor(2))
        else:
            planta.atualizar_projeteis()
        
    for g in girasol:
        g.desenhar()
        g.printSol() 
    # Faz a planta disparar a cada 1 segundo
    
    tempo_atual = time.time()
   
    if (tempo_atual - tempo_anterior) > 3 : 
        for _,planta in plantas.items():
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